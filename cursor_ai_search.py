#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hệ thống tìm kiếm thông minh cho Cursor AI Library
Tác giả: Cursor Assistant cho anh Nghĩa
Ngày: 25/10/2025
"""

import os
import json
import re
from datetime import datetime
from collections import defaultdict

class CursorAISearch:
    def __init__(self, library_path="cursor_ai_library_organized"):
        self.library_path = library_path
        self.index = {}
        self.load_library_index()
    
    def load_library_index(self):
        """Tải chỉ mục thư viện"""
        try:
            with open(f'{self.library_path}/library_data.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.index = data
        except Exception as e:
            print(f"❌ Lỗi khi tải chỉ mục: {e}")
            self.index = {}
    
    def search_text_in_file(self, file_path, search_terms):
        """Tìm kiếm văn bản trong file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read().lower()
            
            results = []
            for term in search_terms:
                if term.lower() in content:
                    # Tìm context xung quanh từ khóa
                    pattern = f".{{0,100}}{re.escape(term.lower())}.{{0,100}}"
                    matches = re.findall(pattern, content, re.IGNORECASE)
                    results.extend(matches)
            
            return results
        except Exception as e:
            print(f"❌ Lỗi khi đọc file {file_path}: {e}")
            return []
    
    def search(self, query, search_type="all"):
        """Tìm kiếm trong toàn bộ thư viện"""
        print(f"🔍 Tìm kiếm: '{query}'")
        print("=" * 50)
        
        # Chia query thành các từ khóa
        search_terms = query.lower().split()
        
        results = {
            'query': query,
            'timestamp': datetime.now().isoformat(),
            'matches': [],
            'summary': {
                'total_matches': 0,
                'files_searched': 0,
                'categories_found': set()
            }
        }
        
        # Tìm kiếm trong tất cả file markdown
        for root, dirs, files in os.walk(self.library_path):
            for file in files:
                if file.endswith('.md'):
                    file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(file_path, self.library_path)
                    
                    # Tìm kiếm trong file
                    matches = self.search_text_in_file(file_path, search_terms)
                    
                    if matches:
                        category = relative_path.split('/')[0] if '/' in relative_path else 'root'
                        results['summary']['categories_found'].add(category)
                        results['summary']['files_searched'] += 1
                        
                        file_result = {
                            'file': relative_path,
                            'category': category,
                            'matches': matches[:5],  # Giới hạn 5 kết quả mỗi file
                            'match_count': len(matches)
                        }
                        
                        results['matches'].append(file_result)
                        results['summary']['total_matches'] += len(matches)
        
        # Sắp xếp kết quả theo số lượng match
        results['matches'].sort(key=lambda x: x['match_count'], reverse=True)
        results['summary']['categories_found'] = list(results['summary']['categories_found'])
        
        return results
    
    def display_results(self, results):
        """Hiển thị kết quả tìm kiếm"""
        print(f"📊 Tìm thấy {results['summary']['total_matches']} kết quả trong {results['summary']['files_searched']} file")
        print(f"📁 Danh mục: {', '.join(results['summary']['categories_found'])}")
        print()
        
        if not results['matches']:
            print("❌ Không tìm thấy kết quả nào!")
            return
        
        for i, match in enumerate(results['matches'][:10], 1):  # Hiển thị tối đa 10 kết quả
            print(f"📄 {i}. {match['file']} ({match['match_count']} kết quả)")
            print(f"   📁 Danh mục: {match['category']}")
            
            for j, text_match in enumerate(match['matches'][:3], 1):  # Hiển thị tối đa 3 đoạn văn
                # Làm sạch và rút gọn văn bản
                clean_text = re.sub(r'\s+', ' ', text_match.strip())
                if len(clean_text) > 150:
                    clean_text = clean_text[:150] + "..."
                print(f"   {j}. {clean_text}")
            print()
    
    def search_by_category(self, query, category):
        """Tìm kiếm trong một danh mục cụ thể"""
        print(f"🔍 Tìm kiếm trong danh mục '{category}': '{query}'")
        print("=" * 50)
        
        search_terms = query.lower().split()
        results = []
        
        category_path = os.path.join(self.library_path, category)
        if not os.path.exists(category_path):
            print(f"❌ Không tìm thấy danh mục: {category}")
            return
        
        for file in os.listdir(category_path):
            if file.endswith('.md'):
                file_path = os.path.join(category_path, file)
                matches = self.search_text_in_file(file_path, search_terms)
                
                if matches:
                    results.append({
                        'file': f"{category}/{file}",
                        'matches': matches[:5],
                        'match_count': len(matches)
                    })
        
        if results:
            results.sort(key=lambda x: x['match_count'], reverse=True)
            for i, result in enumerate(results[:5], 1):
                print(f"📄 {i}. {result['file']} ({result['match_count']} kết quả)")
                for j, text_match in enumerate(result['matches'][:2], 1):
                    clean_text = re.sub(r'\s+', ' ', text_match.strip())
                    if len(clean_text) > 100:
                        clean_text = clean_text[:100] + "..."
                    print(f"   {j}. {clean_text}")
                print()
        else:
            print("❌ Không tìm thấy kết quả nào trong danh mục này!")
    
    def list_categories(self):
        """Liệt kê các danh mục có sẵn"""
        print("📚 CÁC DANH MỤC CÓ SẴN:")
        print("=" * 30)
        
        categories = []
        for item in os.listdir(self.library_path):
            item_path = os.path.join(self.library_path, item)
            if os.path.isdir(item_path) and item.startswith(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')):
                categories.append(item)
        
        categories.sort()
        
        category_names = {
            '01_overview': 'Tổng quan về Cursor AI',
            '02_features': 'Tính năng và khả năng',
            '03_pricing': 'Bảng giá và gói dịch vụ',
            '04_technical': 'Thông tin kỹ thuật',
            '05_guides': 'Hướng dẫn sử dụng',
            '06_research': 'Nghiên cứu và phát triển',
            '07_resources': 'Tài nguyên bổ sung'
        }
        
        for category in categories:
            name = category_names.get(category, category)
            print(f"📁 {category} - {name}")
        
        print()
    
    def get_quick_facts(self):
        """Lấy các thông tin nhanh về Cursor"""
        print("⚡ THÔNG TIN NHANH VỀ CURSOR AI:")
        print("=" * 40)
        
        # Tìm kiếm các thông tin quan trọng
        key_facts = [
            "Cursor là gì",
            "tính năng chính",
            "giá cả",
            "AI capabilities",
            "cách sử dụng"
        ]
        
        for fact in key_facts:
            results = self.search(fact)
            if results['matches']:
                print(f"🔹 {fact.upper()}:")
                for match in results['matches'][:2]:
                    for text_match in match['matches'][:1]:
                        clean_text = re.sub(r'\s+', ' ', text_match.strip())
                        if len(clean_text) > 80:
                            clean_text = clean_text[:80] + "..."
                        print(f"   • {clean_text}")
                print()
    
    def interactive_search(self):
        """Chế độ tìm kiếm tương tác"""
        print("🚀 CURSOR AI LIBRARY - HỆ THỐNG TÌM KIẾM")
        print("=" * 50)
        print("Gõ 'help' để xem hướng dẫn")
        print("Gõ 'quit' để thoát")
        print()
        
        while True:
            try:
                command = input("🔍 Nhập từ khóa tìm kiếm: ").strip()
                
                if command.lower() == 'quit':
                    print("👋 Tạm biệt!")
                    break
                elif command.lower() == 'help':
                    self.show_help()
                elif command.lower() == 'categories':
                    self.list_categories()
                elif command.lower() == 'facts':
                    self.get_quick_facts()
                elif command.startswith('category:'):
                    parts = command.split(':', 1)
                    if len(parts) == 2:
                        category = parts[1].strip()
                        query = input(f"Tìm kiếm trong {category}: ").strip()
                        if query:
                            self.search_by_category(query, category)
                    else:
                        print("❌ Cú pháp: category:01_overview")
                elif command:
                    results = self.search(command)
                    self.display_results(results)
                else:
                    print("❌ Vui lòng nhập từ khóa tìm kiếm!")
                
                print()
                
            except KeyboardInterrupt:
                print("\n👋 Tạm biệt!")
                break
            except Exception as e:
                print(f"❌ Lỗi: {e}")
    
    def show_help(self):
        """Hiển thị hướng dẫn sử dụng"""
        print("📖 HƯỚNG DẪN SỬ DỤNG:")
        print("=" * 30)
        print("• Nhập từ khóa để tìm kiếm trong toàn bộ thư viện")
        print("• 'categories' - Xem danh sách các danh mục")
        print("• 'facts' - Xem thông tin nhanh về Cursor")
        print("• 'category:01_overview' - Tìm kiếm trong danh mục cụ thể")
        print("• 'help' - Hiển thị hướng dẫn này")
        print("• 'quit' - Thoát chương trình")
        print()

def main():
    """Hàm chính"""
    search_engine = CursorAISearch()
    
    # Kiểm tra xem thư viện có tồn tại không
    if not os.path.exists(search_engine.library_path):
        print(f"❌ Không tìm thấy thư viện tại: {search_engine.library_path}")
        print("Vui lòng chạy cursor_ai_library_organizer.py trước!")
        return
    
    # Chạy chế độ tương tác
    search_engine.interactive_search()

if __name__ == "__main__":
    main()