#!/usr/bin/env python3
"""
Script để kiểm thử deployment FFC trên Vercel/Firebase
Sử dụng requests library để test các endpoints
"""

import requests
import sys
import json
from urllib.parse import urlparse

def test_url(url):
    """Test một URL và trả về thông tin chi tiết"""
    print(f"\n🔍 Đang kiểm tra: {url}")
    print("=" * 60)
    
    try:
        # Test GET request
        response = requests.get(url, timeout=10, allow_redirects=True)
        
        print(f"✅ Status Code: {response.status_code}")
        print(f"📄 Final URL: {response.url}")
        print(f"⏱️  Response Time: {response.elapsed.total_seconds():.2f}s")
        
        # Check headers
        print(f"\n📋 Headers quan trọng:")
        headers_to_check = ['content-type', 'server', 'x-vercel', 'cache-control']
        for header in headers_to_check:
            if header in response.headers:
                print(f"   {header}: {response.headers[header]}")
        
        # Check if it's HTML (web page)
        content_type = response.headers.get('content-type', '')
        if 'text/html' in content_type:
            print(f"\n🌐 Đây là trang web HTML")
            print(f"📏 Kích thước: {len(response.text)} bytes")
            
            # Check for FFC-related content
            content_lower = response.text.lower()
            ffc_keywords = ['ffc', 'feature', 'function', 'component']
            found_keywords = [kw for kw in ffc_keywords if kw in content_lower]
            if found_keywords:
                print(f"🔑 Tìm thấy keywords: {', '.join(found_keywords)}")
        
        # Check if it's JSON (API)
        elif 'application/json' in content_type:
            print(f"\n📊 Đây là API endpoint (JSON)")
            try:
                data = response.json()
                print(f"✅ JSON hợp lệ")
                print(f"📏 Số keys: {len(data) if isinstance(data, dict) else 'N/A'}")
            except:
                print(f"⚠️  Không parse được JSON")
        
        return {
            'success': True,
            'status': response.status_code,
            'url': response.url,
            'content_type': content_type
        }
        
    except requests.exceptions.Timeout:
        print(f"❌ Timeout - Website không phản hồi sau 10s")
        return {'success': False, 'error': 'Timeout'}
    
    except requests.exceptions.ConnectionError:
        print(f"❌ Connection Error - Không thể kết nối")
        return {'success': False, 'error': 'Connection Error'}
    
    except Exception as e:
        print(f"❌ Lỗi: {str(e)}")
        return {'success': False, 'error': str(e)}


def test_ffc_features(base_url):
    """Test các tính năng FFC cụ thể"""
    print(f"\n\n🎯 Kiểm tra tính năng FFC")
    print("=" * 60)
    
    # Common FFC endpoints/pages to test
    test_paths = [
        '/',
        '/api',
        '/api/ffc',
        '/ffc',
        '/feature',
        '/features',
        '/health',
        '/status'
    ]
    
    results = []
    for path in test_paths:
        test_url_full = base_url.rstrip('/') + path
        result = test_url(test_url_full)
        result['path'] = path
        results.append(result)
    
    return results


if __name__ == "__main__":
    print("🚀 Công cụ kiểm thử FFC Deployment")
    print("=" * 60)
    
    # Nếu có URL từ command line
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        # Nếu không có URL, hỏi user
        print("\n📝 Vui lòng nhập URL deployment:")
        print("   (Ví dụ: https://your-app.vercel.app hoặc https://your-app.firebaseapp.com)")
        url = input("URL: ").strip()
    
    if not url:
        print("❌ Không có URL để test!")
        sys.exit(1)
    
    # Đảm bảo có protocol
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    # Test URL chính
    main_result = test_url(url)
    
    # Test các paths phổ biến
    if main_result.get('success'):
        test_ffc_features(url)
    
    print("\n\n✅ Hoàn thành kiểm tra!")
    print("=" * 60)
