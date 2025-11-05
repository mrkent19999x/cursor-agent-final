#!/usr/bin/env python3
"""
E2E Test tự động cho FFC Feature
Tự động test sau khi deploy
"""

import asyncio
import sys
from datetime import datetime
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError

# Config
BASE_URL = "https://etaxfinal.vercel.app"
ADMIN_EMAIL = "phuctran123@gmail.com"
ADMIN_PASSWORD = "123456"
FFC_URL = f"{BASE_URL}/admin/ffc"

class FFCTester:
    def __init__(self):
        self.results = {
            'start_time': datetime.now().isoformat(),
            'tests': [],
            'screenshots': []
        }
        
    def log_test(self, name, status, message=""):
        """Log test result"""
        test_result = {
            'name': name,
            'status': status,
            'message': message,
            'timestamp': datetime.now().isoformat()
        }
        self.results['tests'].append(test_result)
        
        status_emoji = {'passed': '✅', 'failed': '❌', 'warning': '⚠️'}
        print(f"\n{status_emoji.get(status, '⚪')} {name}: {status.upper()}")
        if message:
            print(f"   {message}")
    
    async def take_screenshot(self, page, name):
        """Take screenshot"""
        try:
            from pathlib import Path
            screenshot_dir = Path('/workspace/e2e_screenshots')
            screenshot_dir.mkdir(exist_ok=True)
            screenshot_path = screenshot_dir / f"{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            await page.screenshot(path=str(screenshot_path), full_page=True)
            self.results['screenshots'].append(str(screenshot_path))
            return screenshot_path
        except Exception as e:
            print(f"   ⚠️  Cannot take screenshot: {e}")
            return None
    
    async def test_login(self, page):
        """Test login"""
        try:
            print(f"\n{'='*60}")
            print("1️⃣ TESTING LOGIN")
            print('='*60)
            
            await page.goto(f"{BASE_URL}/admin/login", wait_until='networkidle', timeout=30000)
            
            await page.fill('input[type="email"]', ADMIN_EMAIL)
            await page.fill('input[type="password"]', ADMIN_PASSWORD)
            await page.click('button[type="submit"]')
            
            try:
                await page.wait_for_load_state('networkidle', timeout=15000)
            except PlaywrightTimeoutError:
                await asyncio.sleep(3)
            
            current_url = page.url
            if 'login' not in current_url.lower():
                self.log_test("Login", "passed", f"Logged in successfully. URL: {current_url}")
                await self.take_screenshot(page, "after_login")
                return True
            else:
                self.log_test("Login", "failed", "Still on login page")
                await self.take_screenshot(page, "login_failed")
                return False
                
        except Exception as e:
            self.log_test("Login", "failed", f"Error: {str(e)}")
            return False
    
    async def test_ffc_page_accessible(self, page):
        """Test FFC page có accessible không"""
        try:
            print(f"\n{'='*60}")
            print("2️⃣ TESTING FFC PAGE ACCESSIBLE")
            print('='*60)
            
            await page.goto(FFC_URL, wait_until='networkidle', timeout=15000)
            current_url = page.url
            
            if 'login' in current_url.lower():
                self.log_test("FFC Page Accessible", "failed", "Redirected to login")
                return False
            
            # Check for 404
            page_content = await page.content()
            if '404' in page_content or 'not found' in page_content.lower():
                self.log_test("FFC Page Accessible", "failed", "404 Not Found")
                return False
            
            self.log_test("FFC Page Accessible", "passed", f"Page loaded: {current_url}")
            await self.take_screenshot(page, "ffc_page")
            return True
            
        except PlaywrightTimeoutError:
            self.log_test("FFC Page Accessible", "failed", "Timeout loading page")
            return False
        except Exception as e:
            self.log_test("FFC Page Accessible", "failed", f"Error: {str(e)}")
            return False
    
    async def test_ffc_content(self, page):
        """Test FFC content có hiển thị không"""
        try:
            print(f"\n{'='*60}")
            print("3️⃣ TESTING FFC CONTENT")
            print('='*60)
            
            page_content = await page.content()
            page_text = await page.inner_text('body')
            
            # Check for FFC keywords
            ffc_keywords = ['feature flag', 'featureflag', 'ffc', 'feature flags']
            found_keywords = [kw for kw in ffc_keywords if kw in page_content.lower()]
            
            if found_keywords:
                self.log_test("FFC Content - Keywords", "passed", f"Found: {', '.join(found_keywords)}")
            else:
                self.log_test("FFC Content - Keywords", "warning", "No FFC keywords found")
            
            # Check for title
            try:
                title = await page.query_selector('h1, h2, [class*="title"]')
                if title:
                    title_text = await title.text_content()
                    self.log_test("FFC Content - Title", "passed", f"Found title: {title_text[:50]}")
                else:
                    self.log_test("FFC Content - Title", "warning", "No title found")
            except:
                self.log_test("FFC Content - Title", "warning", "Could not check title")
            
            # Check for Add/Create button
            try:
                add_selectors = [
                    'button:has-text("Thêm")',
                    'button:has-text("Add")',
                    'button:has-text("Tạo")',
                    'button:has-text("Create")',
                    'a:has-text("Thêm")',
                    'a:has-text("Add")'
                ]
                
                add_button_found = False
                for selector in add_selectors:
                    try:
                        button = await page.wait_for_selector(selector, timeout=2000)
                        if button:
                            button_text = await button.text_content()
                            self.log_test("FFC Content - Add Button", "passed", f"Found: {button_text.strip()}")
                            add_button_found = True
                            break
                    except:
                        continue
                
                if not add_button_found:
                    self.log_test("FFC Content - Add Button", "warning", "No Add button found")
            except:
                self.log_test("FFC Content - Add Button", "warning", "Could not check Add button")
            
            # Check for table/list
            try:
                table = await page.query_selector('table, [class*="table"], [class*="list"]')
                if table:
                    self.log_test("FFC Content - Table/List", "passed", "Found data table/list")
                else:
                    self.log_test("FFC Content - Table/List", "warning", "No table/list found")
            except:
                self.log_test("FFC Content - Table/List", "warning", "Could not check table")
            
            return True
            
        except Exception as e:
            self.log_test("FFC Content", "failed", f"Error: {str(e)}")
            return False
    
    async def test_ffc_functionality(self, page):
        """Test FFC functionality"""
        try:
            print(f"\n{'='*60}")
            print("4️⃣ TESTING FFC FUNCTIONALITY")
            print('='*60)
            
            # Try to click Add button
            add_selectors = [
                'button:has-text("Thêm Feature Flag")',
                'button:has-text("Thêm")',
                'button:has-text("Add Feature Flag")',
                'button:has-text("Add")',
                'a:has-text("Thêm")',
                'a:has-text("Add")'
            ]
            
            modal_opened = False
            for selector in add_selectors:
                try:
                    button = await page.wait_for_selector(selector, timeout=2000)
                    if button:
                        await button.click()
                        await asyncio.sleep(1)
                        
                        # Check if modal opened
                        modal = await page.query_selector('[class*="modal"], [class*="Modal"], [role="dialog"]')
                        if modal:
                            modal_opened = True
                            self.log_test("FFC Functionality - Add Modal", "passed", "Add modal opened")
                            
                            # Close modal
                            close_button = await page.query_selector('button:has-text("Hủy"), button:has-text("Cancel"), [aria-label="Close"]')
                            if close_button:
                                await close_button.click()
                            break
                except:
                    continue
            
            if not modal_opened:
                self.log_test("FFC Functionality - Add Modal", "warning", "Could not test Add functionality")
            
            return True
            
        except Exception as e:
            self.log_test("FFC Functionality", "warning", f"Error: {str(e)}")
            return True  # Not critical
    
    async def run_all_tests(self):
        """Run all tests"""
        print("🚀 FFC E2E TEST")
        print("="*60)
        print(f"🌐 Base URL: {BASE_URL}")
        print(f"🎯 FFC URL: {FFC_URL}")
        print(f"⏰ Start: {self.results['start_time']}")
        print("="*60)
        
        async with async_playwright() as p:
            browser = await p.chromium.launch(
                headless=True,
                args=['--no-sandbox', '--disable-setuid-sandbox']
            )
            
            context = await browser.new_context(
                viewport={'width': 1920, 'height': 1080}
            )
            
            page = await context.new_page()
            
            try:
                # Test login
                login_success = await self.test_login(page)
                
                if login_success:
                    # Test FFC page
                    ffc_accessible = await self.test_ffc_page_accessible(page)
                    
                    if ffc_accessible:
                        await self.test_ffc_content(page)
                        await self.test_ffc_functionality(page)
                
            except Exception as e:
                print(f"\n❌ Fatal error: {str(e)}")
                self.log_test("Fatal Error", "failed", str(e))
                await self.take_screenshot(page, "fatal_error")
            
            finally:
                await browser.close()
        
        # Finalize
        self.results['end_time'] = datetime.now().isoformat()
        self.results['summary'] = {
            'total': len(self.results['tests']),
            'passed': len([t for t in self.results['tests'] if t['status'] == 'passed']),
            'failed': len([t for t in self.results['tests'] if t['status'] == 'failed']),
            'warnings': len([t for t in self.results['tests'] if t['status'] == 'warning'])
        }
        
        return self.results
    
    def print_summary(self):
        """Print test summary"""
        print(f"\n{'='*60}")
        print("📊 TEST SUMMARY")
        print('='*60)
        print(f"Total: {self.results['summary']['total']}")
        print(f"✅ Passed: {self.results['summary']['passed']}")
        print(f"❌ Failed: {self.results['summary']['failed']}")
        print(f"⚠️  Warnings: {self.results['summary']['warnings']}")
        print('='*60)

async def main():
    tester = FFCTester()
    results = await tester.run_all_tests()
    tester.print_summary()
    
    # Exit code
    if results['summary']['failed'] == 0:
        return 0
    else:
        return 1

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
