#!/usr/bin/env python3
"""
Script scan chi tiết Admin page để tìm FFC
Sau khi đã login thành công
"""

import asyncio
import json
from datetime import datetime
from playwright.async_api import async_playwright
from pathlib import Path

async def scan_admin_page():
    """Scan admin page chi tiết để tìm FFC"""
    base_url = "https://etaxfinal.vercel.app"
    email = "phuctran123@gmail.com"
    password = "123456"
    
    print("🔍 SCANNING ADMIN PAGE FOR FFC")
    print("="*60)
    
    results = {
        'urls_visited': [],
        'menu_items': [],
        'links_found': [],
        'buttons_found': [],
        'text_content': '',
        'ffc_indicators': []
    }
    
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
            # Login
            print("\n1️⃣ Logging in...")
            await page.goto(f"{base_url}/admin/login", wait_until='networkidle')
            
            await page.fill('input[type="email"]', email)
            await page.fill('input[type="password"]', password)
            await page.click('button[type="submit"]')
            await page.wait_for_load_state('networkidle', timeout=15000)
            
            current_url = page.url
            print(f"   ✅ Logged in, current URL: {current_url}")
            results['urls_visited'].append(current_url)
            
            # Wait for page to fully load
            await asyncio.sleep(3)
            
            # Get all text content
            print("\n2️⃣ Getting page content...")
            page_content = await page.content()
            page_text = await page.inner_text('body')
            results['text_content'] = page_text[:5000]  # First 5000 chars
            
            # Find all links
            print("\n3️⃣ Finding all links...")
            links = await page.query_selector_all('a')
            for link in links:
                try:
                    href = await link.get_attribute('href')
                    text = await link.text_content()
                    if href and text:
                        results['links_found'].append({
                            'text': text.strip(),
                            'href': href,
                            'full_url': f"{base_url}{href}" if href.startswith('/') else href
                        })
                        # Check if FFC related
                        if any(kw in (text + href).lower() for kw in ['ffc', 'feature', 'flag']):
                            results['ffc_indicators'].append({
                                'type': 'link',
                                'text': text.strip(),
                                'href': href
                            })
                            print(f"   🎯 FFC link found: {text.strip()} -> {href}")
                except:
                    continue
            
            print(f"   ✅ Found {len(results['links_found'])} links total")
            
            # Find all buttons
            print("\n4️⃣ Finding all buttons...")
            buttons = await page.query_selector_all('button')
            for button in buttons:
                try:
                    text = await button.text_content()
                    onclick = await button.get_attribute('onclick')
                    id_attr = await button.get_attribute('id')
                    class_attr = await button.get_attribute('class')
                    if text:
                        results['buttons_found'].append({
                            'text': text.strip(),
                            'id': id_attr,
                            'class': class_attr,
                            'onclick': onclick
                        })
                        # Check if FFC related
                        full_text = (text + (id_attr or '') + (class_attr or '')).lower()
                        if any(kw in full_text for kw in ['ffc', 'feature', 'flag']):
                            results['ffc_indicators'].append({
                                'type': 'button',
                                'text': text.strip(),
                                'id': id_attr,
                                'class': class_attr
                            })
                            print(f"   🎯 FFC button found: {text.strip()}")
                except:
                    continue
            
            print(f"   ✅ Found {len(results['buttons_found'])} buttons total")
            
            # Find menu items / navigation
            print("\n5️⃣ Finding menu/navigation items...")
            nav_selectors = [
                'nav a',
                'nav li',
                '.navbar a',
                '.menu a',
                '.sidebar a',
                '[role="navigation"] a',
                '[role="menubar"] a',
                'ul[class*="menu"] a',
                'ul[class*="nav"] a'
            ]
            
            for selector in nav_selectors:
                try:
                    items = await page.query_selector_all(selector)
                    for item in items:
                        try:
                            text = await item.text_content()
                            href = await item.get_attribute('href')
                            if text and text.strip():
                                results['menu_items'].append({
                                    'text': text.strip(),
                                    'href': href,
                                    'selector': selector
                                })
                                # Check if FFC related
                                if any(kw in text.lower() for kw in ['ffc', 'feature', 'flag']):
                                    results['ffc_indicators'].append({
                                        'type': 'menu',
                                        'text': text.strip(),
                                        'href': href
                                    })
                                    print(f"   🎯 FFC menu item found: {text.strip()}")
                        except:
                            continue
                except:
                    continue
            
            print(f"   ✅ Found {len(results['menu_items'])} menu items total")
            
            # Try clicking on different menu items to find FFC
            print("\n6️⃣ Exploring menu items...")
            unique_menu_texts = set()
            for item in results['menu_items']:
                if item['text'] and item['text'] not in unique_menu_texts:
                    unique_menu_texts.add(item['text'])
            
            for menu_text in list(unique_menu_texts)[:10]:  # Limit to 10 items
                try:
                    # Find and click menu item
                    menu_link = await page.query_selector(f'a:has-text("{menu_text}")')
                    if menu_link:
                        href = await menu_link.get_attribute('href')
                        if href and href.startswith('/'):
                            full_url = f"{base_url}{href}"
                            
                            # Navigate to this page
                            await page.goto(full_url, wait_until='networkidle', timeout=10000)
                            await asyncio.sleep(2)
                            
                            new_url = page.url
                            if new_url not in results['urls_visited']:
                                results['urls_visited'].append(new_url)
                                print(f"   📄 Visited: {menu_text} -> {new_url}")
                                
                                # Check for FFC in new page
                                new_content = await page.content()
                                if any(kw in new_content.lower() for kw in ['ffc', 'feature-flag', 'featureflag']):
                                    results['ffc_indicators'].append({
                                        'type': 'page',
                                        'menu_text': menu_text,
                                        'url': new_url
                                    })
                                    print(f"   🎯 FFC found on page: {menu_text} ({new_url})")
                            
                            # Go back
                            await page.go_back(wait_until='networkidle')
                            await asyncio.sleep(1)
                except Exception as e:
                    print(f"   ⚠️  Error exploring {menu_text}: {str(e)[:50]}")
                    continue
            
            # Check common FFC routes
            print("\n7️⃣ Testing common FFC routes...")
            ffc_routes = [
                '/admin/ffc',
                '/admin/feature-flags',
                '/admin/feature-flag',
                '/admin/settings/ffc',
                '/admin/config/ffc',
                '/admin/features',
                '/ffc',
                '/feature-flags'
            ]
            
            for route in ffc_routes:
                try:
                    full_url = f"{base_url}{route}"
                    response = await page.goto(full_url, wait_until='networkidle', timeout=10000)
                    
                    if response and response.status == 200:
                        final_url = page.url
                        if 'login' not in final_url.lower():
                            if final_url not in results['urls_visited']:
                                results['urls_visited'].append(final_url)
                            
                            page_content = await page.content()
                            if any(kw in page_content.lower() for kw in ['ffc', 'feature-flag']):
                                results['ffc_indicators'].append({
                                    'type': 'route',
                                    'route': route,
                                    'url': final_url
                                })
                                print(f"   🎯 FFC route found: {route} -> {final_url}")
                            
                            await asyncio.sleep(1)
                except Exception as e:
                    # Expected for non-existent routes
                    pass
            
            # Take screenshot
            screenshot_path = Path('/workspace/e2e_screenshots/admin_page_scan.png')
            screenshot_path.parent.mkdir(exist_ok=True)
            await page.screenshot(path=str(screenshot_path), full_page=True)
            print(f"\n   📸 Screenshot saved: {screenshot_path}")
            
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")
            results['error'] = str(e)
        
        finally:
            await browser.close()
    
    # Save results
    report_path = Path('/workspace/ADMIN_PAGE_SCAN_REPORT.json')
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    # Print summary
    print("\n" + "="*60)
    print("📊 SCAN SUMMARY")
    print("="*60)
    print(f"URLs visited: {len(results['urls_visited'])}")
    print(f"Links found: {len(results['links_found'])}")
    print(f"Buttons found: {len(results['buttons_found'])}")
    print(f"Menu items found: {len(results['menu_items'])}")
    print(f"FFC indicators found: {len(results['ffc_indicators'])}")
    
    if results['ffc_indicators']:
        print("\n🎯 FFC INDICATORS FOUND:")
        for indicator in results['ffc_indicators']:
            print(f"   - {indicator['type']}: {indicator.get('text') or indicator.get('route') or indicator.get('url')}")
    else:
        print("\n⚠️  No FFC indicators found")
        print("\n💡 Possible reasons:")
        print("   1. FFC feature not yet implemented")
        print("   2. FFC requires special permissions")
        print("   3. FFC is in a different location")
        print("   4. FFC name is different (not 'FFC')")
    
    print(f"\n📄 Full report: {report_path}")
    print("="*60)
    
    return results

if __name__ == "__main__":
    asyncio.run(scan_admin_page())
