#!/usr/bin/env python3
"""
Script kiểm thử FFC với authentication
Test login flow và kiểm tra FFC feature sau khi đăng nhập
"""

import requests
import sys
from urllib.parse import urljoin

class FFCTester:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        
    def test_page(self, url, description=""):
        """Test một trang và trả về thông tin"""
        print(f"\n{'='*60}")
        if description:
            print(f"🔍 {description}")
        print(f"📄 URL: {url}")
        print('='*60)
        
        try:
            response = self.session.get(url, timeout=10, allow_redirects=True)
            
            print(f"✅ Status: {response.status_code}")
            print(f"📍 Final URL: {response.url}")
            
            # Check if redirected
            if response.url != url:
                print(f"🔄 Redirected from: {url}")
            
            # Check content
            content_lower = response.text.lower()
            
            # Check for FFC references
            ffc_indicators = ['ffc', 'feature flag', 'feature-flag', 'featureflag']
            found_ffc = [ind for ind in ffc_indicators if ind in content_lower]
            
            if found_ffc:
                print(f"🎯 Tìm thấy FFC indicators: {', '.join(found_ffc)}")
            else:
                print(f"⚠️  Không tìm thấy FFC indicators trong HTML")
            
            # Check for error messages
            error_keywords = ['error', 'failed', 'unauthorized', 'forbidden', 'not found']
            found_errors = [kw for kw in error_keywords if any(err in content_lower for err in [f' {kw} ', f'{kw} ', f' {kw}'])]
            if found_errors:
                print(f"❌ Có thể có lỗi: {', '.join(found_errors[:3])}")
            
            # Check for login forms
            if 'login' in content_lower or 'password' in content_lower or 'email' in content_lower:
                if 'form' in content_lower:
                    print(f"🔐 Có form login/password trong trang")
            
            return {
                'success': response.status_code == 200,
                'status': response.status_code,
                'url': response.url,
                'has_ffc': len(found_ffc) > 0,
                'content_length': len(response.text)
            }
            
        except Exception as e:
            print(f"❌ Lỗi: {str(e)}")
            return {'success': False, 'error': str(e)}
    
    def test_login(self, email, password, is_admin=False):
        """Test login flow"""
        login_url = f"{self.base_url}/admin/login" if is_admin else f"{self.base_url}/login"
        
        print(f"\n\n{'='*60}")
        print(f"🔐 TESTING LOGIN FLOW")
        print(f"{'='*60}")
        print(f"📧 Email: {email}")
        print(f"🔑 Password: {'*' * len(password)}")
        print(f"👤 Type: {'Admin' if is_admin else 'User'}")
        
        # First, get login page to check CSRF tokens, etc.
        print(f"\n1️⃣ Lấy trang login...")
        login_page = self.test_page(login_url, "Login Page")
        
        if not login_page['success']:
            print(f"❌ Không thể truy cập trang login!")
            return False
        
        # Try to find login form action and inputs
        login_html = self.session.get(login_url).text.lower()
        
        # Common form patterns
        form_methods = ['post', 'put']
        api_endpoints = ['/api/auth', '/api/login', '/auth/login', '/login']
        
        print(f"\n2️⃣ Thử login...")
        print(f"   (Đang tìm form action và endpoint)...")
        
        # Try common login endpoints
        login_attempted = False
        for endpoint in api_endpoints:
            full_url = urljoin(self.base_url, endpoint)
            try:
                response = self.session.post(
                    full_url,
                    json={'email': email, 'password': password},
                    timeout=10,
                    allow_redirects=True
                )
                
                print(f"\n   📤 POST {full_url}")
                print(f"   📊 Status: {response.status_code}")
                
                if response.status_code in [200, 302, 303, 307]:
                    print(f"   ✅ Có phản hồi")
                    login_attempted = True
                    
                    # Check if redirected (successful login)
                    if response.url != full_url:
                        print(f"   🔄 Redirected to: {response.url}")
                        print(f"   ✅ Có thể đã login thành công!")
                        
                        # Test the redirected page
                        final_page = self.test_page(response.url, "Page after login")
                        return final_page['success']
                    
            except:
                continue
        
        # If no API endpoint worked, try form submission
        if not login_attempted:
            print(f"\n   ⚠️  Không tìm thấy API endpoint, thử form submission...")
            try:
                # Try standard form submission
                response = self.session.post(
                    login_url,
                    data={'email': email, 'password': password},
                    timeout=10,
                    allow_redirects=True
                )
                
                print(f"   📤 POST {login_url}")
                print(f"   📊 Status: {response.status_code}")
                
                if response.url != login_url:
                    print(f"   ✅ Redirected to: {response.url}")
                    final_page = self.test_page(response.url, "Page after login")
                    return final_page['success']
                else:
                    print(f"   ⚠️  Vẫn ở trang login - có thể sai credentials hoặc cần thông tin thêm")
                    
            except Exception as e:
                print(f"   ❌ Lỗi: {str(e)}")
        
        return False
    
    def test_ffc_after_login(self):
        """Test các endpoint có thể liên quan đến FFC sau khi login"""
        print(f"\n\n{'='*60}")
        print(f"🎯 TESTING FFC ENDPOINTS")
        print(f"{'='*60}")
        
        # Common FFC endpoints
        ffc_endpoints = [
            '/ffc',
            '/feature-flag',
            '/feature-flags',
            '/api/ffc',
            '/api/feature-flag',
            '/admin/ffc',
            '/admin/feature-flag',
            '/settings/ffc',
            '/dashboard/ffc'
        ]
        
        results = []
        for endpoint in ffc_endpoints:
            url = urljoin(self.base_url, endpoint)
            result = self.test_page(url, f"FFC Endpoint: {endpoint}")
            results.append(result)
            
            # If found something interesting, report it
            if result.get('has_ffc'):
                print(f"   🎯 Tìm thấy FFC tại endpoint này!")
        
        return results

def main():
    base_url = "https://etaxfinal.vercel.app"
    admin_email = "phuctran123@gmail.com"
    admin_password = "123456"
    
    print("🚀 FFC TESTER WITH AUTHENTICATION")
    print("="*60)
    print(f"🌐 Base URL: {base_url}")
    print(f"👤 Admin: {admin_email}")
    
    tester = FFCTester(base_url)
    
    # Test pages without login
    print(f"\n\n{'='*60}")
    print("1️⃣ TESTING PAGES (KHÔNG LOGIN)")
    print('='*60)
    
    tester.test_page(f"{base_url}/", "Home/Login Redirect")
    tester.test_page(f"{base_url}/login", "User Login Page")
    tester.test_page(f"{base_url}/admin/login", "Admin Login Page")
    
    # Test login
    print(f"\n\n{'='*60}")
    print("2️⃣ TESTING LOGIN")
    print('='*60)
    
    login_success = tester.test_login(admin_email, admin_password, is_admin=True)
    
    if login_success:
        print(f"\n✅ Login thành công!")
    else:
        print(f"\n⚠️  Không chắc chắn login có thành công không")
        print(f"   (Có thể cần kiểm tra thủ công)")
    
    # Test FFC endpoints
    print(f"\n\n{'='*60}")
    print("3️⃣ TESTING FFC ENDPOINTS")
    print('='*60)
    
    tester.test_ffc_after_login()
    
    # Test common admin pages
    print(f"\n\n{'='*60}")
    print("4️⃣ TESTING ADMIN PAGES")
    print('='*60)
    
    admin_pages = [
        '/admin',
        '/admin/dashboard',
        '/admin/settings',
        '/dashboard',
        '/settings'
    ]
    
    for page in admin_pages:
        tester.test_page(urljoin(base_url, page), f"Admin Page: {page}")
    
    print(f"\n\n{'='*60}")
    print("✅ HOÀN THÀNH KIỂM TRA")
    print('='*60)
    print(f"\n💡 Lưu ý:")
    print(f"   - Nếu không tìm thấy FFC, có thể:")
    print(f"     + FFC chỉ hiện sau khi login thành công")
    print(f"     + FFC ở một route/endpoint khác")
    print(f"     + FFC là một tính năng trong UI cần kiểm tra thủ công")
    print(f"   - Hãy thử login thủ công và kiểm tra trong browser")

if __name__ == "__main__":
    main()
