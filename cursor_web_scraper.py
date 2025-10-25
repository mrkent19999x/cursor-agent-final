#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script cào web cursor.com để thu thập thông tin về AI
Tác giả: Cursor Assistant cho anh Nghĩa
Ngày: 25/10/2025
"""

import requests
from bs4 import BeautifulSoup
import json
import time
import os
from datetime import datetime
import re
from urllib.parse import urljoin, urlparse
import logging

# Thiết lập logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('cursor_scraping.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

class CursorWebScraper:
    def __init__(self):
        self.base_url = "https://cursor.com"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        self.scraped_data = {
            'main_page': {},
            'features': [],
            'pricing': {},
            'documentation': [],
            'blog_posts': [],
            'ai_insights': [],
            'metadata': {
                'scraped_at': datetime.now().isoformat(),
                'total_pages': 0,
                'successful_pages': 0
            }
        }
        
    def get_page_content(self, url):
        """Lấy nội dung trang web"""
        try:
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            return response.text
        except Exception as e:
            logging.error(f"Lỗi khi lấy nội dung từ {url}: {str(e)}")
            return None
    
    def scrape_main_page(self):
        """Cào trang chủ cursor.com"""
        logging.info("🚀 Bắt đầu cào trang chủ cursor.com...")
        
        content = self.get_page_content(self.base_url)
        if not content:
            return
            
        soup = BeautifulSoup(content, 'html.parser')
        
        # Thu thập thông tin chính
        main_data = {
            'title': soup.find('title').text if soup.find('title') else '',
            'description': '',
            'headlines': [],
            'features_overview': [],
            'cta_buttons': [],
            'testimonials': [],
            'ai_mentions': []
        }
        
        # Tìm description
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        if meta_desc:
            main_data['description'] = meta_desc.get('content', '')
        
        # Tìm các tiêu đề chính
        for tag in ['h1', 'h2', 'h3']:
            for headline in soup.find_all(tag):
                text = headline.get_text().strip()
                if text and len(text) > 10:
                    main_data['headlines'].append({
                        'tag': tag,
                        'text': text
                    })
        
        # Tìm các tính năng
        feature_sections = soup.find_all(['div', 'section'], class_=re.compile(r'feature|benefit|capability', re.I))
        for section in feature_sections:
            feature_text = section.get_text().strip()
            if feature_text and len(feature_text) > 20:
                main_data['features_overview'].append(feature_text)
        
        # Tìm các nút CTA
        for button in soup.find_all(['button', 'a'], class_=re.compile(r'cta|button|download|get|start', re.I)):
            button_text = button.get_text().strip()
            if button_text:
                main_data['cta_buttons'].append(button_text)
        
        # Tìm các testimonial
        for testimonial in soup.find_all(['div', 'blockquote'], class_=re.compile(r'testimonial|review|quote', re.I)):
            testimonial_text = testimonial.get_text().strip()
            if testimonial_text and len(testimonial_text) > 30:
                main_data['testimonials'].append(testimonial_text)
        
        # Tìm các mention về AI
        ai_keywords = ['AI', 'artificial intelligence', 'machine learning', 'neural', 'GPT', 'assistant', 'intelligent']
        for element in soup.find_all(text=re.compile('|'.join(ai_keywords), re.I)):
            if element.parent:
                ai_text = element.parent.get_text().strip()
                if ai_text and len(ai_text) > 20:
                    main_data['ai_mentions'].append(ai_text)
        
        self.scraped_data['main_page'] = main_data
        logging.info(f"✅ Đã cào xong trang chủ: {len(main_data['headlines'])} tiêu đề, {len(main_data['features_overview'])} tính năng")
    
    def find_and_scrape_subpages(self):
        """Tìm và cào các trang con quan trọng"""
        logging.info("🔍 Tìm kiếm các trang con quan trọng...")
        
        content = self.get_page_content(self.base_url)
        if not content:
            return
            
        soup = BeautifulSoup(content, 'html.parser')
        
        # Tìm các link quan trọng
        important_links = []
        for link in soup.find_all('a', href=True):
            href = link['href']
            text = link.get_text().strip().lower()
            
            # Các từ khóa quan trọng
            important_keywords = [
                'features', 'pricing', 'docs', 'documentation', 'blog', 
                'about', 'ai', 'intelligence', 'capabilities', 'how-it-works',
                'tutorial', 'guide', 'help', 'support'
            ]
            
            if any(keyword in text or keyword in href.lower() for keyword in important_keywords):
                full_url = urljoin(self.base_url, href)
                if full_url.startswith(self.base_url):
                    important_links.append({
                        'url': full_url,
                        'text': text,
                        'type': self.categorize_link(text, href)
                    })
        
        # Loại bỏ duplicate
        unique_links = []
        seen_urls = set()
        for link in important_links:
            if link['url'] not in seen_urls:
                unique_links.append(link)
                seen_urls.add(link['url'])
        
        logging.info(f"📋 Tìm thấy {len(unique_links)} trang con quan trọng")
        
        # Cào từng trang con
        for i, link in enumerate(unique_links[:10]):  # Giới hạn 10 trang để tránh quá tải
            logging.info(f"📄 Cào trang {i+1}/{min(10, len(unique_links))}: {link['text']}")
            self.scrape_subpage(link)
            time.sleep(2)  # Nghỉ 2 giây giữa các request
    
    def categorize_link(self, text, href):
        """Phân loại link"""
        text_lower = text.lower()
        href_lower = href.lower()
        
        if any(word in text_lower for word in ['feature', 'capability', 'function']):
            return 'features'
        elif any(word in text_lower for word in ['price', 'cost', 'plan', 'subscription']):
            return 'pricing'
        elif any(word in text_lower for word in ['doc', 'guide', 'tutorial', 'help']):
            return 'documentation'
        elif any(word in text_lower for word in ['blog', 'news', 'article']):
            return 'blog'
        elif any(word in text_lower for word in ['ai', 'intelligence', 'smart']):
            return 'ai_insights'
        else:
            return 'general'
    
    def scrape_subpage(self, link_info):
        """Cào một trang con cụ thể"""
        url = link_info['url']
        page_type = link_info['type']
        
        content = self.get_page_content(url)
        if not content:
            return
            
        soup = BeautifulSoup(content, 'html.parser')
        
        page_data = {
            'url': url,
            'title': soup.find('title').text if soup.find('title') else '',
            'content': soup.get_text().strip(),
            'headings': [],
            'ai_related_content': [],
            'scraped_at': datetime.now().isoformat()
        }
        
        # Thu thập các heading
        for tag in ['h1', 'h2', 'h3', 'h4']:
            for heading in soup.find_all(tag):
                heading_text = heading.get_text().strip()
                if heading_text:
                    page_data['headings'].append({
                        'level': tag,
                        'text': heading_text
                    })
        
        # Tìm nội dung liên quan đến AI
        ai_keywords = ['AI', 'artificial intelligence', 'machine learning', 'neural', 'GPT', 'assistant', 'intelligent', 'smart', 'automated']
        for element in soup.find_all(text=re.compile('|'.join(ai_keywords), re.I)):
            if element.parent:
                ai_content = element.parent.get_text().strip()
                if ai_content and len(ai_content) > 30:
                    page_data['ai_related_content'].append(ai_content)
        
        # Lưu vào cấu trúc dữ liệu phù hợp
        if page_type == 'features':
            self.scraped_data['features'].append(page_data)
        elif page_type == 'pricing':
            self.scraped_data['pricing'] = page_data
        elif page_type == 'documentation':
            self.scraped_data['documentation'].append(page_data)
        elif page_type == 'blog':
            self.scraped_data['blog_posts'].append(page_data)
        elif page_type == 'ai_insights':
            self.scraped_data['ai_insights'].append(page_data)
        
        self.scraped_data['metadata']['successful_pages'] += 1
        logging.info(f"✅ Đã cào xong: {page_data['title']}")
    
    def save_data(self):
        """Lưu dữ liệu đã cào được"""
        # Tạo thư mục lưu trữ
        os.makedirs('cursor_ai_library', exist_ok=True)
        
        # Lưu dữ liệu JSON
        with open('cursor_ai_library/raw_data.json', 'w', encoding='utf-8') as f:
            json.dump(self.scraped_data, f, ensure_ascii=False, indent=2)
        
        # Tạo báo cáo tổng hợp
        self.create_summary_report()
        
        logging.info("💾 Đã lưu dữ liệu vào cursor_ai_library/")
    
    def create_summary_report(self):
        """Tạo báo cáo tổng hợp"""
        report = f"""
# BÁO CÁO TỔNG HỢP - CURSOR.COM AI LIBRARY
Ngày tạo: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}

## 📊 THỐNG KÊ TỔNG QUAN
- Tổng số trang đã cào: {self.scraped_data['metadata']['successful_pages']}
- Số tính năng tìm thấy: {len(self.scraped_data['features'])}
- Số bài blog: {len(self.scraped_data['blog_posts'])}
- Số tài liệu: {len(self.scraped_data['documentation'])}
- Số insight về AI: {len(self.scraped_data['ai_insights'])}

## 🎯 THÔNG TIN CHÍNH TỪ TRANG CHỦ
**Tiêu đề:** {self.scraped_data['main_page'].get('title', 'N/A')}
**Mô tả:** {self.scraped_data['main_page'].get('description', 'N/A')}

### Các tiêu đề quan trọng:
"""
        
        for headline in self.scraped_data['main_page'].get('headlines', [])[:10]:
            report += f"- {headline['text']}\n"
        
        report += f"""
### Tính năng chính:
"""
        for feature in self.scraped_data['main_page'].get('features_overview', [])[:10]:
            report += f"- {feature}\n"
        
        report += f"""
### Các mention về AI:
"""
        for ai_mention in self.scraped_data['main_page'].get('ai_mentions', [])[:10]:
            report += f"- {ai_mention}\n"
        
        # Lưu báo cáo
        with open('cursor_ai_library/SUMMARY_REPORT.md', 'w', encoding='utf-8') as f:
            f.write(report)
    
    def run(self):
        """Chạy toàn bộ quá trình cào web"""
        logging.info("🚀 Bắt đầu cào web cursor.com...")
        
        try:
            # Cào trang chủ
            self.scrape_main_page()
            
            # Tìm và cào các trang con
            self.find_and_scrape_subpages()
            
            # Lưu dữ liệu
            self.save_data()
            
            logging.info("✅ Hoàn thành cào web! Dữ liệu đã được lưu vào cursor_ai_library/")
            
        except Exception as e:
            logging.error(f"❌ Lỗi trong quá trình cào web: {str(e)}")

if __name__ == "__main__":
    scraper = CursorWebScraper()
    scraper.run()