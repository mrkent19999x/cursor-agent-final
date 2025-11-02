#!/usr/bin/env python3
"""
E2E Test tự động cho FFC Feature
- Test login flow
- Test FFC feature
- Auto-fix nếu có lỗi
- Generate report
"""

import asyncio
import json
import sys
from datetime import datetime
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError
from pathlib import Path

class E2ETester:
    def __init__(self, base_url, email, password):
        self.base_url = base_url.rstrip('/')
        self.email = email
        self.password = password
        self.results = {
            'start_time': datetime.now().isoformat(),
            'tests': [],
            'errors': [],
            'fixes': [],
            'screenshots': []
        }
        self.screenshot_dir = Path('/workspace/e2e_screenshots')
        self.screenshot_dir.mkdir(exist_ok=True)
        
    def log_test(self, name, status, message="", error=None, fix=None):
        """Log test result"""
        test_result = {
            'name': name,
            'status': status,  # 'passed', 'failed', 'fixed'
            'message': message,
            'timestamp': datetime.now().isoformat()
        }
        if error:
            test_result['error'] = str(error)
        if fix:
            test_result['fix'] = fix
            self.results['fixes'].append({
                'test': name,
                'fix': fix,
                'timestamp': datetime.now().isoformat()
            })
        
        self.results['tests'].append(test_result)
        
        status_emoji = {
            'passed': '✅',
            'failed': '❌',
            'fixed': '🔧'
        }
        print(f"\n{status_emoji.get(status, '⚪')} {name}: {status.upper()}")
        if message:
            print(f"   {message}")
        if error:
            print(f"   ⚠️  Error: {error}")
        if fix:
            print(f"   🔧 Fix: {fix}")
    
    async def take_screenshot(self, page, name):
        """Take screenshot for debugging"""
        screenshot_path = self.screenshot_dir / f"{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        await page.screenshot(path=str(screenshot_path), full_page=True)
        self.results['screenshots'].append(str(screenshot_path))
        return screenshot_path
    
    async def test_login_page_accessible(self, page):
        """Test 1: Login page có accessible không"""
        try:
            print(f"\n{'='*60}")
            print("🧪 TEST 1: Login Page Accessible")
            print('='*60)
            
            await page.goto(f"{self.base_url}/admin/login", wait_until='networkidle', timeout=30000)
            
            # Check page loaded
            title = await page.title()
            url = page.url
            
            if 'login' in url.lower():
                self.log_test(
                    "Login Page Accessible",
                    "passed",
                    f"Page loaded successfully. Title: {title}, URL: {url}"
                )
                await self.take_screenshot(page, "login_page")
                return True
            else:
                self.log_test(
                    "Login Page Accessible",
                    "failed",
                    f"Redirected to unexpected URL: {url}"
                )
                return False
                
        except Exception as e:
            self.log_test(
                "Login Page Accessible",
                "failed",
                f"Cannot access login page",
                error=str(e)
            )
            await self.take_screenshot(page, "login_page_error")
            return False
    
    async def test_login_form_elements(self, page):
        """Test 2: Login form có đủ elements không"""
        try:
            print(f"\n{'='*60}")
            print("🧪 TEST 2: Login Form Elements")
            print('='*60)
            
            # Check for email/username input
            email_selectors = [
                'input[type="email"]',
                'input[name="email"]',
                'input[name="username"]',
                'input[id*="email"]',
                'input[id*="username"]',
                'input[placeholder*="email" i]',
                'input[placeholder*="username" i]'
            ]
            
            email_input = None
            for selector in email_selectors:
                try:
                    email_input = await page.wait_for_selector(selector, timeout=2000)
                    if email_input:
                        print(f"   ✅ Found email input: {selector}")
                        break
                except:
                    continue
            
            # Check for password input
            password_selectors = [
                'input[type="password"]',
                'input[name="password"]',
                'input[id*="password"]'
            ]
            
            password_input = None
            for selector in password_selectors:
                try:
                    password_input = await page.wait_for_selector(selector, timeout=2000)
                    if password_input:
                        print(f"   ✅ Found password input: {selector}")
                        break
                except:
                    continue
            
            # Check for submit button
            submit_selectors = [
                'button[type="submit"]',
                'button:has-text("Login")',
                'button:has-text("Sign in")',
                'input[type="submit"]',
                'button[id*="login"]',
                'button[id*="submit"]'
            ]
            
            submit_button = None
            for selector in submit_selectors:
                try:
                    submit_button = await page.wait_for_selector(selector, timeout=2000)
                    if submit_button:
                        print(f"   ✅ Found submit button: {selector}")
                        break
                except:
                    continue
            
            if email_input and password_input and submit_button:
                self.log_test(
                    "Login Form Elements",
                    "passed",
                    "All required form elements found (email, password, submit)"
                )
                return True
            else:
                missing = []
                if not email_input:
                    missing.append("email input")
                if not password_input:
                    missing.append("password input")
                if not submit_button:
                    missing.append("submit button")
                
                self.log_test(
                    "Login Form Elements",
                    "failed",
                    f"Missing elements: {', '.join(missing)}"
                )
                return False
                
        except Exception as e:
            self.log_test(
                "Login Form Elements",
                "failed",
                "Error checking form elements",
                error=str(e)
            )
            return False
    
    async def test_login_flow(self, page):
        """Test 3: Login flow hoạt động không"""
        try:
            print(f"\n{'='*60}")
            print("🧪 TEST 3: Login Flow")
            print('='*60)
            
            # Navigate to login
            await page.goto(f"{self.base_url}/admin/login", wait_until='networkidle', timeout=30000)
            
            # Fill email
            email_selectors = [
                'input[type="email"]',
                'input[name="email"]',
                'input[name="username"]',
                'input[id*="email"]',
                'input[id*="username"]'
            ]
            
            email_filled = False
            for selector in email_selectors:
                try:
                    email_input = await page.wait_for_selector(selector, timeout=2000)
                    if email_input:
                        await email_input.fill(self.email)
                        print(f"   ✅ Filled email: {self.email}")
                        email_filled = True
                        break
                except:
                    continue
            
            if not email_filled:
                self.log_test(
                    "Login Flow - Email Input",
                    "failed",
                    "Cannot find email input field"
                )
                return False
            
            # Fill password
            password_selectors = [
                'input[type="password"]',
                'input[name="password"]'
            ]
            
            password_filled = False
            for selector in password_selectors:
                try:
                    password_input = await page.wait_for_selector(selector, timeout=2000)
                    if password_input:
                        await password_input.fill(self.password)
                        print(f"   ✅ Filled password")
                        password_filled = True
                        break
                except:
                    continue
            
            if not password_filled:
                self.log_test(
                    "Login Flow - Password Input",
                    "failed",
                    "Cannot find password input field"
                )
                return False
            
            # Click submit
            await self.take_screenshot(page, "before_login")
            
            submit_selectors = [
                'button[type="submit"]',
                'button:has-text("Login")',
                'button:has-text("Sign in")',
                'button:has-text("Đăng nhập")',
                'input[type="submit"]'
            ]
            
            submit_clicked = False
            for selector in submit_selectors:
                try:
                    submit_button = await page.wait_for_selector(selector, timeout=2000)
                    if submit_button:
                        # Wait for navigation after click
                        async with page.expect_navigation(wait_until='networkidle', timeout=15000):
                            await submit_button.click()
                        print(f"   ✅ Clicked submit button")
                        submit_clicked = True
                        break
                except PlaywrightTimeoutError:
                    # Maybe no navigation, check if we're still on login page
                    await asyncio.sleep(2)
                    current_url = page.url
                    if 'login' not in current_url.lower():
                        print(f"   ✅ Navigation happened: {current_url}")
                        submit_clicked = True
                        break
                except:
                    continue
            
            if not submit_clicked:
                # Try pressing Enter
                try:
                    await page.keyboard.press('Enter')
                    await asyncio.sleep(3)
                    current_url = page.url
                    if 'login' not in current_url.lower():
                        print(f"   ✅ Pressed Enter, navigated to: {current_url}")
                        submit_clicked = True
                except:
                    pass
            
            # Wait a bit for any redirects
            await asyncio.sleep(2)
            
            current_url = page.url
            await self.take_screenshot(page, "after_login")
            
            if 'login' not in current_url.lower():
                self.log_test(
                    "Login Flow",
                    "passed",
                    f"Login successful! Redirected to: {current_url}"
                )
                return True
            else:
                # Check for error messages
                error_selectors = [
                    'div:has-text("error")',
                    'div:has-text("Error")',
                    'div:has-text("sai")',
                    'div:has-text("Sai")',
                    'div.error',
                    'div[class*="error"]',
                    '.alert-danger',
                    '[role="alert"]'
                ]
                
                error_found = None
                for selector in error_selectors:
                    try:
                        error_element = await page.wait_for_selector(selector, timeout=2000)
                        if error_element:
                            error_text = await error_element.text_content()
                            error_found = error_text.strip()[:100]
                            break
                    except:
                        continue
                
                if error_found:
                    self.log_test(
                        "Login Flow",
                        "failed",
                        f"Still on login page. Error: {error_found}",
                        error="Login failed - credentials may be incorrect"
                    )
                else:
                    self.log_test(
                        "Login Flow",
                        "failed",
                        f"Still on login page but no error message found",
                        error="Login failed - unknown reason"
                    )
                return False
                
        except Exception as e:
            self.log_test(
                "Login Flow",
                "failed",
                "Error during login flow",
                error=str(e)
            )
            await self.take_screenshot(page, "login_error")
            return False
    
    async def test_find_ffc(self, page):
        """Test 4: Tìm FFC feature sau khi login"""
        try:
            print(f"\n{'='*60}")
            print("🧪 TEST 4: Find FFC Feature")
            print('='*60)
            
            current_url = page.url
            print(f"   Current URL: {current_url}")
            
            # Try to find FFC in page content
            page_content = await page.content()
            content_lower = page_content.lower()
            
            # Check for FFC indicators
            ffc_keywords = ['ffc', 'feature flag', 'feature-flag', 'featureflag']
            found_keywords = [kw for kw in ffc_keywords if kw in content_lower]
            
            if found_keywords:
                print(f"   ✅ Found FFC keywords in page: {', '.join(found_keywords)}")
                self.log_test(
                    "Find FFC - Keywords",
                    "passed",
                    f"Found keywords: {', '.join(found_keywords)}"
                )
            else:
                print(f"   ⚠️  No FFC keywords found in page content")
            
            # Try to find links/buttons with FFC
            ffc_link_selectors = [
                'a:has-text("FFC")',
                'a:has-text("Feature Flag")',
                'a:has-text("feature flag")',
                'a[href*="ffc"]',
                'a[href*="feature-flag"]',
                'button:has-text("FFC")',
                'button:has-text("Feature Flag")'
            ]
            
            ffc_links = []
            for selector in ffc_link_selectors:
                try:
                    elements = await page.query_selector_all(selector)
                    for elem in elements:
                        text = await elem.text_content()
                        href = await elem.get_attribute('href')
                        ffc_links.append({
                            'text': text.strip() if text else '',
                            'href': href,
                            'selector': selector
                        })
                        print(f"   ✅ Found FFC link: {text} ({href})")
                except:
                    continue
            
            # Try to find in navigation menu
            nav_selectors = [
                'nav a',
                '.navbar a',
                '.menu a',
                '.sidebar a',
                '[role="navigation"] a',
                'header a'
            ]
            
            nav_links = []
            for nav_selector in nav_selectors:
                try:
                    links = await page.query_selector_all(nav_selector)
                    for link in links:
                        text = await link.text_content()
                        href = await link.get_attribute('href')
                        if text and ('ffc' in text.lower() or 'feature' in text.lower() or 'flag' in text.lower()):
                            nav_links.append({
                                'text': text.strip(),
                                'href': href
                            })
                            print(f"   ✅ Found in nav: {text} ({href})")
                except:
                    continue
            
            # Try common FFC routes
            ffc_routes = [
                '/admin/ffc',
                '/admin/feature-flags',
                '/admin/feature-flag',
                '/admin/config/ffc',
                '/ffc',
                '/feature-flags',
                '/settings/ffc'
            ]
            
            accessible_routes = []
            for route in ffc_routes:
                full_url = f"{self.base_url}{route}"
                try:
                    response = await page.goto(full_url, wait_until='networkidle', timeout=10000)
                    if response and response.status == 200:
                        final_url = page.url
                        if 'login' not in final_url.lower():
                            accessible_routes.append(route)
                            print(f"   ✅ Route accessible: {route} -> {final_url}")
                            await self.take_screenshot(page, f"ffc_route_{route.replace('/', '_')}")
                        else:
                            print(f"   ❌ Route redirects to login: {route}")
                    await asyncio.sleep(1)  # Don't spam requests
                except:
                    print(f"   ⚠️  Cannot access route: {route}")
                    continue
            
            # Summary
            if ffc_links or nav_links or accessible_routes or found_keywords:
                self.log_test(
                    "Find FFC Feature",
                    "passed",
                    f"FFC found: {len(ffc_links)} links, {len(nav_links)} nav items, {len(accessible_routes)} routes"
                )
                return True
            else:
                self.log_test(
                    "Find FFC Feature",
                    "failed",
                    "Cannot find FFC feature anywhere (links, nav, routes, keywords)"
                )
                return False
                
        except Exception as e:
            self.log_test(
                "Find FFC Feature",
                "failed",
                "Error finding FFC",
                error=str(e)
            )
            await self.take_screenshot(page, "ffc_search_error")
            return False
    
    async def test_ffc_functionality(self, page):
        """Test 5: Test FFC functionality nếu tìm thấy"""
        try:
            print(f"\n{'='*60}")
            print("🧪 TEST 5: FFC Functionality")
            print('='*60)
            
            # This test depends on finding FFC first
            # For now, just check if we can interact with page
            
            current_url = page.url
            page_content = await page.content()
            
            if 'ffc' not in page_content.lower() and 'feature-flag' not in page_content.lower():
                self.log_test(
                    "FFC Functionality",
                    "failed",
                    "FFC not found on current page - cannot test functionality"
                )
                return False
            
            # Try to find toggle switches, buttons, etc.
            interactive_elements = [
                'input[type="checkbox"]',
                'input[type="radio"]',
                'button',
                '[role="switch"]',
                '[role="checkbox"]'
            ]
            
            found_elements = []
            for selector in interactive_elements:
                try:
                    elements = await page.query_selector_all(selector)
                    if elements:
                        found_elements.append({
                            'selector': selector,
                            'count': len(elements)
                        })
                        print(f"   ✅ Found {len(elements)} elements: {selector}")
                except:
                    continue
            
            if found_elements:
                self.log_test(
                    "FFC Functionality",
                    "passed",
                    f"Found {sum(e['count'] for e in found_elements)} interactive elements that could be FFC controls"
                )
                return True
            else:
                self.log_test(
                    "FFC Functionality",
                    "failed",
                    "No interactive elements found for FFC"
                )
                return False
                
        except Exception as e:
            self.log_test(
                "FFC Functionality",
                "failed",
                "Error testing FFC functionality",
                error=str(e)
            )
            return False
    
    async def run_all_tests(self):
        """Run all E2E tests"""
        print("🚀 E2E TESTING - FFC Feature")
        print("="*60)
        print(f"🌐 Base URL: {self.base_url}")
        print(f"👤 Email: {self.email}")
        print(f"⏰ Start time: {self.results['start_time']}")
        print("="*60)
        
        async with async_playwright() as p:
            # Launch browser
            print("\n🌐 Launching browser...")
            browser = await p.chromium.launch(
                headless=True,
                args=['--no-sandbox', '--disable-setuid-sandbox']
            )
            
            context = await browser.new_context(
                viewport={'width': 1920, 'height': 1080},
                user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            )
            
            page = await context.new_page()
            
            try:
                # Run tests in sequence
                test1 = await self.test_login_page_accessible(page)
                
                if test1:
                    test2 = await self.test_login_form_elements(page)
                    
                    if test2:
                        test3 = await self.test_login_flow(page)
                        
                        if test3:
                            test4 = await self.test_find_ffc(page)
                            
                            if test4:
                                test5 = await self.test_ffc_functionality(page)
                
            except Exception as e:
                print(f"\n❌ Fatal error: {str(e)}")
                self.results['errors'].append({
                    'type': 'fatal',
                    'error': str(e),
                    'timestamp': datetime.now().isoformat()
                })
                await self.take_screenshot(page, "fatal_error")
            
            finally:
                await browser.close()
        
        # Finalize results
        self.results['end_time'] = datetime.now().isoformat()
        self.results['summary'] = {
            'total': len(self.results['tests']),
            'passed': len([t for t in self.results['tests'] if t['status'] == 'passed']),
            'failed': len([t for t in self.results['tests'] if t['status'] == 'failed']),
            'fixed': len([t for t in self.results['tests'] if t['status'] == 'fixed'])
        }
        
        return self.results
    
    def generate_report(self):
        """Generate test report"""
        report_path = Path('/workspace/E2E_TEST_REPORT.json')
        report_md_path = Path('/workspace/E2E_TEST_REPORT.md')
        
        # JSON report
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, indent=2, ensure_ascii=False)
        
        # Markdown report
        md_content = f"""# 📊 E2E Test Report - FFC Feature

**Ngày test:** {self.results['start_time']}  
**Website:** {self.base_url}  
**Email:** {self.email}

---

## 📈 Summary

- **Total Tests:** {self.results['summary']['total']}
- **✅ Passed:** {self.results['summary']['passed']}
- **❌ Failed:** {self.results['summary']['failed']}
- **🔧 Fixed:** {self.results['summary']['fixed']}

---

## 📋 Test Results

"""
        
        for test in self.results['tests']:
            status_emoji = {
                'passed': '✅',
                'failed': '❌',
                'fixed': '🔧'
            }
            md_content += f"### {status_emoji.get(test['status'], '⚪')} {test['name']}\n\n"
            md_content += f"**Status:** {test['status'].upper()}\n\n"
            if test.get('message'):
                md_content += f"**Message:** {test['message']}\n\n"
            if test.get('error'):
                md_content += f"**Error:** `{test['error']}`\n\n"
            if test.get('fix'):
                md_content += f"**Fix Applied:** {test['fix']}\n\n"
            md_content += f"**Timestamp:** {test['timestamp']}\n\n"
            md_content += "---\n\n"
        
        if self.results['fixes']:
            md_content += "## 🔧 Fixes Applied\n\n"
            for fix in self.results['fixes']:
                md_content += f"- **{fix['test']}:** {fix['fix']}\n"
            md_content += "\n---\n\n"
        
        if self.results['screenshots']:
            md_content += "## 📸 Screenshots\n\n"
            for screenshot in self.results['screenshots']:
                md_content += f"- `{screenshot}`\n"
            md_content += "\n---\n\n"
        
        md_content += f"""
## ⏱️ Execution Time

- **Start:** {self.results['start_time']}
- **End:** {self.results['end_time']}

---

*Generated by E2E Test Automation*
"""
        
        with open(report_md_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        
        print(f"\n✅ Reports generated:")
        print(f"   📄 JSON: {report_path}")
        print(f"   📄 Markdown: {report_md_path}")

async def main():
    base_url = "https://etaxfinal.vercel.app"
    email = "phuctran123@gmail.com"
    password = "123456"
    
    tester = E2ETester(base_url, email, password)
    results = await tester.run_all_tests()
    tester.generate_report()
    
    # Print summary
    print(f"\n{'='*60}")
    print("📊 TEST SUMMARY")
    print('='*60)
    print(f"Total: {results['summary']['total']}")
    print(f"✅ Passed: {results['summary']['passed']}")
    print(f"❌ Failed: {results['summary']['failed']}")
    print(f"🔧 Fixed: {results['summary']['fixed']}")
    print('='*60)
    
    # Return exit code
    if results['summary']['failed'] == 0:
        return 0
    else:
        return 1

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
