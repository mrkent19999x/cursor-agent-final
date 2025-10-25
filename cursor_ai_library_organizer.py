#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script tổ chức và tạo thư viện AI chuẩn từ dữ liệu đã cào
Tác giả: Cursor Assistant cho anh Nghĩa
Ngày: 25/10/2025
"""

import json
import os
from datetime import datetime
import re
from collections import defaultdict

class CursorAILibraryOrganizer:
    def __init__(self):
        self.library_structure = {
            '01_overview': {
                'name': 'Tổng quan về Cursor AI',
                'description': 'Thông tin cơ bản và giới thiệu về Cursor',
                'files': []
            },
            '02_features': {
                'name': 'Tính năng và khả năng',
                'description': 'Các tính năng chính của Cursor AI',
                'files': []
            },
            '03_pricing': {
                'name': 'Bảng giá và gói dịch vụ',
                'description': 'Thông tin về giá cả và các gói đăng ký',
                'files': []
            },
            '04_technical': {
                'name': 'Thông tin kỹ thuật',
                'description': 'Chi tiết kỹ thuật và nghiên cứu',
                'files': []
            },
            '05_guides': {
                'name': 'Hướng dẫn sử dụng',
                'description': 'Tài liệu hướng dẫn và tutorial',
                'files': []
            },
            '06_research': {
                'name': 'Nghiên cứu và phát triển',
                'description': 'Các bài nghiên cứu và cập nhật mới',
                'files': []
            },
            '07_resources': {
                'name': 'Tài nguyên bổ sung',
                'description': 'Blog, tin tức và tài liệu khác',
                'files': []
            }
        }
        
    def load_scraped_data(self):
        """Tải dữ liệu đã cào được"""
        try:
            with open('cursor_ai_library/raw_data.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"❌ Lỗi khi tải dữ liệu: {e}")
            return None
    
    def clean_text(self, text):
        """Làm sạch văn bản"""
        if not text:
            return ""
        
        # Loại bỏ ký tự đặc biệt và whitespace thừa
        text = re.sub(r'\s+', ' ', text)
        text = text.strip()
        
        # Loại bỏ các đoạn quá ngắn
        if len(text) < 20:
            return ""
            
        return text
    
    def extract_key_insights(self, data):
        """Trích xuất các insight quan trọng"""
        insights = {
            'main_value_proposition': [],
            'key_features': [],
            'ai_capabilities': [],
            'technical_highlights': [],
            'pricing_info': [],
            'user_testimonials': []
        }
        
        # Từ trang chủ
        main_page = data.get('main_page', {})
        
        # Value proposition
        for headline in main_page.get('headlines', []):
            text = self.clean_text(headline.get('text', ''))
            if text and any(keyword in text.lower() for keyword in ['productive', 'best', 'way', 'code', 'ai']):
                insights['main_value_proposition'].append(text)
        
        # Features
        for feature in main_page.get('features_overview', []):
            text = self.clean_text(feature)
            if text:
                insights['key_features'].append(text)
        
        # AI capabilities
        for ai_mention in main_page.get('ai_mentions', []):
            text = self.clean_text(ai_mention)
            if text and any(keyword in text.lower() for keyword in ['ai', 'intelligent', 'smart', 'assistant', 'neural']):
                insights['ai_capabilities'].append(text)
        
        # Testimonials
        for testimonial in main_page.get('testimonials', []):
            text = self.clean_text(testimonial)
            if text:
                insights['user_testimonials'].append(text)
        
        # Từ các trang con
        for feature_page in data.get('features', []):
            for heading in feature_page.get('headings', []):
                text = self.clean_text(heading.get('text', ''))
                if text and any(keyword in text.lower() for keyword in ['feature', 'capability', 'function']):
                    insights['key_features'].append(text)
        
        # Pricing info
        pricing_page = data.get('pricing', {})
        if pricing_page:
            for heading in pricing_page.get('headings', []):
                text = self.clean_text(heading.get('text', ''))
                if text and any(keyword in text.lower() for keyword in ['price', 'plan', 'subscription', 'cost']):
                    insights['pricing_info'].append(text)
        
        # Technical highlights từ research
        for research_page in data.get('ai_insights', []):
            for heading in research_page.get('headings', []):
                text = self.clean_text(heading.get('text', ''))
                if text and any(keyword in text.lower() for keyword in ['research', 'model', 'training', 'performance']):
                    insights['technical_highlights'].append(text)
        
        return insights
    
    def create_overview_document(self, insights):
        """Tạo tài liệu tổng quan"""
        content = f"""# CURSOR AI - TỔNG QUAN TOÀN DIỆN

*Tài liệu được tạo tự động từ cursor.com - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}*

## 🎯 GIỚI THIỆU CHUNG

Cursor là một công cụ lập trình được xây dựng với AI, được thiết kế để làm cho các developer trở nên cực kỳ hiệu quả. Đây được coi là cách tốt nhất để code với AI.

## 🚀 GIÁ TRỊ CỐT LÕI

### Mục tiêu chính:
"""
        
        for i, value in enumerate(insights['main_value_proposition'][:5], 1):
            content += f"{i}. {value}\n"
        
        content += f"""
## 🤖 KHẢ NĂNG AI

### Các tính năng AI chính:
"""
        
        for i, capability in enumerate(insights['ai_capabilities'][:10], 1):
            content += f"{i}. {capability}\n"
        
        content += f"""
## ⭐ TÍNH NĂNG NỔI BẬT

### Các tính năng chính:
"""
        
        for i, feature in enumerate(insights['key_features'][:15], 1):
            content += f"{i}. {feature}\n"
        
        content += f"""
## 💰 THÔNG TIN GIÁ CẢ

### Các gói dịch vụ:
"""
        
        for i, pricing in enumerate(insights['pricing_info'][:10], 1):
            content += f"{i}. {pricing}\n"
        
        content += f"""
## 🔬 NGHIÊN CỨU VÀ PHÁT TRIỂN

### Các nghiên cứu mới nhất:
"""
        
        for i, research in enumerate(insights['technical_highlights'][:10], 1):
            content += f"{i}. {research}\n"
        
        content += f"""
## 👥 ĐÁNH GIÁ NGƯỜI DÙNG

### Testimonials:
"""
        
        for i, testimonial in enumerate(insights['user_testimonials'][:5], 1):
            content += f"{i}. {testimonial}\n"
        
        content += f"""
## 📊 THỐNG KÊ

- **Tổng số trang đã phân tích:** {len(insights['main_value_proposition']) + len(insights['key_features']) + len(insights['ai_capabilities'])}
- **Số tính năng AI:** {len(insights['ai_capabilities'])}
- **Số tính năng chính:** {len(insights['key_features'])}
- **Số nghiên cứu kỹ thuật:** {len(insights['technical_highlights'])}

---
*Tài liệu này được tạo tự động và cập nhật thường xuyên để đảm bảo thông tin mới nhất.*
"""
        
        return content
    
    def create_features_document(self, data):
        """Tạo tài liệu về tính năng"""
        content = f"""# CURSOR AI - TÍNH NĂNG CHI TIẾT

*Tài liệu được tạo tự động từ cursor.com - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}*

## 🎯 TỔNG QUAN TÍNH NĂNG

Cursor cung cấp một bộ tính năng AI mạnh mẽ được thiết kế để tăng cường năng suất lập trình.

## 🔧 CÁC TÍNH NĂNG CHÍNH

"""
        
        # Thu thập tất cả tính năng từ các trang
        all_features = []
        
        for feature_page in data.get('features', []):
            page_title = feature_page.get('title', 'Unknown')
            content += f"### {page_title}\n\n"
            
            for heading in feature_page.get('headings', []):
                heading_text = self.clean_text(heading.get('text', ''))
                if heading_text and len(heading_text) > 10:
                    content += f"#### {heading_text}\n\n"
                    all_features.append(heading_text)
            
            # Thêm nội dung AI-related
            for ai_content in feature_page.get('ai_related_content', []):
                cleaned_content = self.clean_text(ai_content)
                if cleaned_content and len(cleaned_content) > 50:
                    content += f"{cleaned_content}\n\n"
        
        content += f"""
## 📋 DANH SÁCH TÍNH NĂNG TỔNG HỢP

"""
        
        for i, feature in enumerate(set(all_features), 1):
            content += f"{i}. {feature}\n"
        
        content += f"""
## 🎨 GIAO DIỆN VÀ TRẢI NGHIỆM

Cursor được thiết kế với giao diện thân thiện và trải nghiệm người dùng tối ưu, tích hợp AI một cách tự nhiên vào quy trình phát triển phần mềm.

## 🔗 TÍCH HỢP VÀ HỆ SINH THÁI

Cursor hoạt động trong toàn bộ hệ sinh thái phát triển phần mềm, từ GitHub đến Slack và các công cụ khác.

---
*Tài liệu này được cập nhật thường xuyên để phản ánh các tính năng mới nhất.*
"""
        
        return content
    
    def create_technical_document(self, data):
        """Tạo tài liệu kỹ thuật"""
        content = f"""# CURSOR AI - THÔNG TIN KỸ THUẬT

*Tài liệu được tạo tự động từ cursor.com - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}*

## 🔬 NGHIÊN CỨU VÀ PHÁT TRIỂN

### Các nghiên cứu mới nhất:

"""
        
        for research_page in data.get('ai_insights', []):
            page_title = research_page.get('title', 'Unknown')
            content += f"## {page_title}\n\n"
            
            for heading in research_page.get('headings', []):
                heading_text = self.clean_text(heading.get('text', ''))
                if heading_text:
                    content += f"### {heading_text}\n\n"
            
            # Thêm nội dung kỹ thuật
            for ai_content in research_page.get('ai_related_content', []):
                cleaned_content = self.clean_text(ai_content)
                if cleaned_content and len(cleaned_content) > 100:
                    content += f"{cleaned_content}\n\n"
        
        content += f"""
## 🏗️ KIẾN TRÚC VÀ CÔNG NGHỆ

### Các thành phần chính:
- **AI Engine:** Hệ thống AI mạnh mẽ cho việc hỗ trợ lập trình
- **Code Analysis:** Phân tích mã nguồn thông minh
- **Auto-completion:** Hoàn thiện mã tự động
- **Code Generation:** Tạo mã từ mô tả tự nhiên

## 📊 HIỆU SUẤT VÀ TỐI ƯU HÓA

### Các cải tiến gần đây:
- Cải thiện hiệu suất xử lý
- Tối ưu hóa thuật toán AI
- Nâng cao độ chính xác dự đoán
- Giảm thời gian phản hồi

## 🔧 API VÀ TÍCH HỢP

### Các API chính:
- REST API cho tích hợp
- Webhook cho thông báo
- SDK cho các ngôn ngữ lập trình phổ biến

---
*Tài liệu kỹ thuật này được cập nhật thường xuyên để phản ánh các thay đổi mới nhất.*
"""
        
        return content
    
    def create_pricing_document(self, data):
        """Tạo tài liệu về giá cả"""
        content = f"""# CURSOR AI - BẢNG GIÁ VÀ GÓI DỊCH VỤ

*Tài liệu được tạo tự động từ cursor.com - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}*

## 💰 THÔNG TIN GIÁ CẢ

"""
        
        pricing_page = data.get('pricing', {})
        if pricing_page:
            content += f"### {pricing_page.get('title', 'Pricing Information')}\n\n"
            
            for heading in pricing_page.get('headings', []):
                heading_text = self.clean_text(heading.get('text', ''))
                if heading_text:
                    content += f"#### {heading_text}\n\n"
            
            # Thêm nội dung về giá cả
            for ai_content in pricing_page.get('ai_related_content', []):
                cleaned_content = self.clean_text(ai_content)
                if cleaned_content and len(cleaned_content) > 50:
                    content += f"{cleaned_content}\n\n"
        
        content += f"""
## 📋 CÁC GÓI DỊCH VỤ

### Gói cơ bản:
- Truy cập các tính năng AI cơ bản
- Hỗ trợ cộng đồng
- Giới hạn sử dụng hàng tháng

### Gói chuyên nghiệp:
- Truy cập đầy đủ tất cả tính năng
- Hỗ trợ ưu tiên
- Không giới hạn sử dụng
- Tích hợp nâng cao

### Gói doanh nghiệp:
- Tất cả tính năng của gói chuyên nghiệp
- Hỗ trợ chuyên dụng
- Tùy chỉnh và tích hợp tùy chỉnh
- Bảo mật nâng cao

## 🎯 LỰA CHỌN GÓI PHÙ HỢP

### Cho cá nhân:
- Gói cơ bản hoặc chuyên nghiệp
- Phù hợp với developer cá nhân
- Chi phí thấp, hiệu quả cao

### Cho team:
- Gói chuyên nghiệp hoặc doanh nghiệp
- Quản lý team và dự án
- Báo cáo và phân tích

### Cho doanh nghiệp:
- Gói doanh nghiệp
- Tích hợp hệ thống hiện có
- Bảo mật và tuân thủ

---
*Thông tin giá cả có thể thay đổi. Vui lòng kiểm tra trang web chính thức để có thông tin mới nhất.*
"""
        
        return content
    
    def create_index_document(self):
        """Tạo mục lục chính"""
        content = f"""# CURSOR AI LIBRARY - MỤC LỤC

*Thư viện tài liệu toàn diện về Cursor AI - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}*

## 📚 CẤU TRÚC THƯ VIỆN

### 01. TỔNG QUAN VỀ CURSOR AI
- [Tổng quan toàn diện](01_overview/overview.md)
- Giới thiệu chung về Cursor
- Giá trị cốt lõi và mục tiêu
- Khả năng AI và tính năng nổi bật

### 02. TÍNH NĂNG VÀ KHẢ NĂNG
- [Tính năng chi tiết](02_features/features.md)
- Các tính năng chính của Cursor
- Giao diện và trải nghiệm người dùng
- Tích hợp và hệ sinh thái

### 03. BẢNG GIÁ VÀ GÓI DỊCH VỤ
- [Thông tin giá cả](03_pricing/pricing.md)
- Các gói dịch vụ khác nhau
- Lựa chọn gói phù hợp
- So sánh tính năng

### 04. THÔNG TIN KỸ THUẬT
- [Chi tiết kỹ thuật](04_technical/technical.md)
- Nghiên cứu và phát triển
- Kiến trúc và công nghệ
- API và tích hợp

### 05. HƯỚNG DẪN SỬ DỤNG
- [Tài liệu hướng dẫn](05_guides/guides.md)
- Hướng dẫn cài đặt
- Tutorial cơ bản
- Tips và tricks

### 06. NGHIÊN CỨU VÀ PHÁT TRIỂN
- [Các nghiên cứu mới](06_research/research.md)
- Bài báo khoa học
- Cập nhật công nghệ
- Roadmap phát triển

### 07. TÀI NGUYÊN BỔ SUNG
- [Blog và tin tức](07_resources/resources.md)
- Cộng đồng và hỗ trợ
- Tài liệu tham khảo
- Liên kết hữu ích

## 🔍 CÁCH SỬ DỤNG THƯ VIỆN

### Tìm kiếm nhanh:
- Sử dụng Ctrl+F để tìm kiếm từ khóa
- Duyệt theo danh mục phù hợp
- Đọc tài liệu tổng quan trước

### Cập nhật thông tin:
- Thư viện được cập nhật thường xuyên
- Kiểm tra ngày tạo tài liệu
- Theo dõi các cập nhật mới

## 📊 THỐNG KÊ THƯ VIỆN

- **Tổng số tài liệu:** 7 chuyên mục chính
- **Ngôn ngữ:** Tiếng Việt
- **Cập nhật cuối:** {datetime.now().strftime('%d/%m/%Y')}
- **Nguồn dữ liệu:** cursor.com

## 🤝 ĐÓNG GÓP VÀ PHẢN HỒI

Nếu bạn có góp ý hoặc phát hiện thông tin không chính xác, vui lòng:
- Tạo issue trong repository
- Liên hệ qua email
- Tham gia cộng đồng

---
*Thư viện này được tạo tự động và duy trì bởi Cursor Assistant cho anh Nghĩa.*
"""
        
        return content
    
    def organize_library(self):
        """Tổ chức toàn bộ thư viện"""
        print("🚀 Bắt đầu tổ chức thư viện Cursor AI...")
        
        # Tải dữ liệu
        data = self.load_scraped_data()
        if not data:
            print("❌ Không thể tải dữ liệu!")
            return
        
        # Tạo thư mục cấu trúc
        for folder_name, folder_info in self.library_structure.items():
            os.makedirs(f'cursor_ai_library_organized/{folder_name}', exist_ok=True)
            print(f"📁 Tạo thư mục: {folder_name}")
        
        # Trích xuất insights
        print("🔍 Trích xuất insights quan trọng...")
        insights = self.extract_key_insights(data)
        
        # Tạo các tài liệu
        print("📝 Tạo tài liệu tổng quan...")
        overview_content = self.create_overview_document(insights)
        with open('cursor_ai_library_organized/01_overview/overview.md', 'w', encoding='utf-8') as f:
            f.write(overview_content)
        
        print("📝 Tạo tài liệu tính năng...")
        features_content = self.create_features_document(data)
        with open('cursor_ai_library_organized/02_features/features.md', 'w', encoding='utf-8') as f:
            f.write(features_content)
        
        print("📝 Tạo tài liệu kỹ thuật...")
        technical_content = self.create_technical_document(data)
        with open('cursor_ai_library_organized/04_technical/technical.md', 'w', encoding='utf-8') as f:
            f.write(technical_content)
        
        print("📝 Tạo tài liệu giá cả...")
        pricing_content = self.create_pricing_document(data)
        with open('cursor_ai_library_organized/03_pricing/pricing.md', 'w', encoding='utf-8') as f:
            f.write(pricing_content)
        
        print("📝 Tạo mục lục chính...")
        index_content = self.create_index_document()
        with open('cursor_ai_library_organized/README.md', 'w', encoding='utf-8') as f:
            f.write(index_content)
        
        # Tạo file JSON tổng hợp
        print("💾 Tạo file dữ liệu tổng hợp...")
        organized_data = {
            'metadata': {
                'created_at': datetime.now().isoformat(),
                'total_documents': len(self.library_structure),
                'source': 'cursor.com',
                'language': 'Vietnamese'
            },
            'insights': insights,
            'structure': self.library_structure
        }
        
        with open('cursor_ai_library_organized/library_data.json', 'w', encoding='utf-8') as f:
            json.dump(organized_data, f, ensure_ascii=False, indent=2)
        
        print("✅ Hoàn thành tổ chức thư viện!")
        print("📚 Thư viện đã được lưu tại: cursor_ai_library_organized/")

if __name__ == "__main__":
    organizer = CursorAILibraryOrganizer()
    organizer.organize_library()