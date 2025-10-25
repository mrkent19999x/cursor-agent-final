#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Launcher chính cho Cursor AI Library
Tác giả: Cursor Assistant cho anh Nghĩa
Ngày: 25/10/2025
"""

import os
import subprocess
import webbrowser
from datetime import datetime

class CursorLibraryLauncher:
    def __init__(self):
        self.library_path = "/workspace"
        
    def show_main_menu(self):
        """Hiển thị menu chính"""
        print("🚀 CURSOR AI LIBRARY - LAUNCHER CHÍNH")
        print("=" * 50)
        print(f"📅 Ngày: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print()
        print("📚 THƯ VIỆN CÓ SẴN:")
        print("1. 📖 Xem tổng quan thư viện")
        print("2. 🔍 Tìm kiếm thông tin")
        print("3. 🌐 Xem hướng dẫn cộng đồng")
        print("4. 📊 Xem báo cáo chi tiết")
        print("5. 🔄 Cập nhật thư viện")
        print("6. 🌍 Mở các cộng đồng quan trọng")
        print("7. 📁 Xem cấu trúc thư mục")
        print("8. ❓ Hướng dẫn sử dụng")
        print("9. 🚪 Thoát")
        print()
    
    def view_library_overview(self):
        """Xem tổng quan thư viện"""
        print("📖 TỔNG QUAN THƯ VIỆN CURSOR AI")
        print("=" * 40)
        
        try:
            with open(f"{self.library_path}/cursor_ai_library_organized/README.md", 'r', encoding='utf-8') as f:
                content = f.read()
                print(content[:1000] + "..." if len(content) > 1000 else content)
        except Exception as e:
            print(f"❌ Lỗi khi đọc file: {e}")
        
        print("\n📁 Các tài liệu chính:")
        print("- 01_overview/overview.md - Tổng quan Cursor AI")
        print("- 02_features/features.md - Tính năng chi tiết")
        print("- 03_pricing/pricing.md - Bảng giá và gói dịch vụ")
        print("- 04_technical/technical.md - Thông tin kỹ thuật")
        print("- CURSOR_COMMUNITY_GUIDE.md - Hướng dẫn cộng đồng")
    
    def search_information(self):
        """Tìm kiếm thông tin"""
        print("🔍 HỆ THỐNG TÌM KIẾM THÔNG MINH")
        print("=" * 40)
        print("Đang khởi động hệ thống tìm kiếm...")
        
        try:
            subprocess.run(['python3', f"{self.library_path}/cursor_ai_search.py"])
        except Exception as e:
            print(f"❌ Lỗi khi chạy hệ thống tìm kiếm: {e}")
            print("Vui lòng chạy thủ công: python3 cursor_ai_search.py")
    
    def view_community_guide(self):
        """Xem hướng dẫn cộng đồng"""
        print("🌐 HƯỚNG DẪN CỘNG ĐỒNG CURSOR AI")
        print("=" * 40)
        
        try:
            with open(f"{self.library_path}/CURSOR_COMMUNITY_GUIDE.md", 'r', encoding='utf-8') as f:
                content = f.read()
                print(content[:1500] + "..." if len(content) > 1500 else content)
        except Exception as e:
            print(f"❌ Lỗi khi đọc file: {e}")
    
    def view_detailed_report(self):
        """Xem báo cáo chi tiết"""
        print("📊 BÁO CÁO CHI TIẾT")
        print("=" * 30)
        print("1. Báo cáo tổng hợp cuối cùng")
        print("2. Báo cáo cộng đồng")
        print("3. Báo cáo cào web")
        
        choice = input("Chọn báo cáo (1-3): ").strip()
        
        files = {
            '1': 'ULTIMATE_CURSOR_AI_LIBRARY_REPORT.md',
            '2': 'cursor_ai_library_advanced/COMMUNITY_REPORT.md',
            '3': 'cursor_ai_library/SUMMARY_REPORT.md'
        }
        
        if choice in files:
            try:
                with open(f"{self.library_path}/{files[choice]}", 'r', encoding='utf-8') as f:
                    content = f.read()
                    print(content[:2000] + "..." if len(content) > 2000 else content)
            except Exception as e:
                print(f"❌ Lỗi khi đọc file: {e}")
        else:
            print("❌ Lựa chọn không hợp lệ!")
    
    def update_library(self):
        """Cập nhật thư viện"""
        print("🔄 CẬP NHẬT THƯ VIỆN")
        print("=" * 30)
        print("Đang cập nhật thư viện...")
        
        try:
            subprocess.run(['bash', f"{self.library_path}/update_cursor_library.sh"])
        except Exception as e:
            print(f"❌ Lỗi khi cập nhật: {e}")
            print("Vui lòng chạy thủ công: bash update_cursor_library.sh")
    
    def open_communities(self):
        """Mở các cộng đồng quan trọng"""
        print("🌍 MỞ CÁC CỘNG ĐỒNG QUAN TRỌNG")
        print("=" * 40)
        print("1. Reddit r/cursor")
        print("2. Discord chính thức")
        print("3. YouTube @cursor-ai")
        print("4. GitHub chính thức")
        print("5. Cộng đồng AI Việt Nam")
        
        choice = input("Chọn cộng đồng (1-5): ").strip()
        
        urls = {
            '1': 'https://www.reddit.com/r/cursor/',
            '2': 'https://discord.gg/cursor',
            '3': 'https://www.youtube.com/@cursor-ai',
            '4': 'https://github.com/getcursor/cursor',
            '5': 'https://www.facebook.com/groups/aivietnam'
        }
        
        if choice in urls:
            try:
                webbrowser.open(urls[choice])
                print(f"✅ Đã mở: {urls[choice]}")
            except Exception as e:
                print(f"❌ Lỗi khi mở browser: {e}")
                print(f"Vui lòng truy cập thủ công: {urls[choice]}")
        else:
            print("❌ Lựa chọn không hợp lệ!")
    
    def view_directory_structure(self):
        """Xem cấu trúc thư mục"""
        print("📁 CẤU TRÚC THƯ MỤC")
        print("=" * 30)
        
        def print_tree(path, prefix="", max_depth=3, current_depth=0):
            if current_depth >= max_depth:
                return
            
            try:
                items = sorted(os.listdir(path))
                for i, item in enumerate(items):
                    if item.startswith('.'):
                        continue
                    
                    item_path = os.path.join(path, item)
                    is_last = i == len(items) - 1
                    
                    current_prefix = "└── " if is_last else "├── "
                    print(f"{prefix}{current_prefix}{item}")
                    
                    if os.path.isdir(item_path) and current_depth < max_depth - 1:
                        next_prefix = prefix + ("    " if is_last else "│   ")
                        print_tree(item_path, next_prefix, max_depth, current_depth + 1)
            except Exception as e:
                print(f"❌ Lỗi khi đọc thư mục {path}: {e}")
        
        print_tree(self.library_path)
    
    def show_help(self):
        """Hiển thị hướng dẫn sử dụng"""
        print("❓ HƯỚNG DẪN SỬ DỤNG")
        print("=" * 30)
        print("""
🎯 MỤC ĐÍCH:
Thư viện Cursor AI này được tạo để anh Nghĩa có thể:
- Hiểu rõ về Cursor AI
- Học cách sử dụng hiệu quả
- Tham gia cộng đồng
- Cập nhật thông tin mới

📚 CÁCH SỬ DỤNG:
1. Chọn menu để xem thông tin
2. Sử dụng tìm kiếm để tìm thông tin cụ thể
3. Tham gia cộng đồng để học hỏi
4. Cập nhật thường xuyên để có thông tin mới

🔍 TÌM KIẾM:
- Gõ từ khóa để tìm thông tin
- Sử dụng 'categories' để xem danh mục
- Sử dụng 'facts' để xem thông tin nhanh

🌐 CỘNG ĐỒNG:
- Reddit: Thảo luận chung
- Discord: Hỗ trợ trực tiếp
- YouTube: Học qua video
- GitHub: Theo dõi phát triển

📞 HỖ TRỢ:
Nếu cần hỗ trợ, hãy:
1. Sử dụng hệ thống tìm kiếm
2. Tham gia cộng đồng
3. Hỏi em trực tiếp
        """)
    
    def run(self):
        """Chạy launcher chính"""
        while True:
            try:
                self.show_main_menu()
                choice = input("Chọn chức năng (1-9): ").strip()
                
                if choice == '1':
                    self.view_library_overview()
                elif choice == '2':
                    self.search_information()
                elif choice == '3':
                    self.view_community_guide()
                elif choice == '4':
                    self.view_detailed_report()
                elif choice == '5':
                    self.update_library()
                elif choice == '6':
                    self.open_communities()
                elif choice == '7':
                    self.view_directory_structure()
                elif choice == '8':
                    self.show_help()
                elif choice == '9':
                    print("👋 Tạm biệt anh Nghĩa! Chúc anh học tập hiệu quả!")
                    break
                else:
                    print("❌ Lựa chọn không hợp lệ! Vui lòng chọn 1-9.")
                
                input("\n⏸️  Nhấn Enter để tiếp tục...")
                print("\n" + "="*50 + "\n")
                
            except KeyboardInterrupt:
                print("\n👋 Tạm biệt anh Nghĩa!")
                break
            except Exception as e:
                print(f"❌ Lỗi: {e}")
                input("Nhấn Enter để tiếp tục...")

if __name__ == "__main__":
    launcher = CursorLibraryLauncher()
    launcher.run()