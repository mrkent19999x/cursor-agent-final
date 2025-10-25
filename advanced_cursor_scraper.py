#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script cào web nâng cao để thu thập thông tin đầy đủ về Cursor AI
Bao gồm: website chính, blog, forum, cộng đồng, Reddit, Discord
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
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Thiết lập logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('advanced_cursor_scraping.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

class AdvancedCursorScraper:
    def __init__(self):
        self.base_url = "https://cursor.com"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        })
        
        # Các nguồn thông tin cần cào
        self.sources = {
            'main_website': {
                'urls': [
                    'https://cursor.com',
                    'https://cursor.com/features',
                    'https://cursor.com/pricing',
                    'https://cursor.com/docs',
                    'https://cursor.com/blog'
                ],
                'type': 'website'
            },
            'reddit': {
                'urls': [
                    'https://www.reddit.com/r/cursor/',
                    'https://www.reddit.com/r/cursorai/',
                    'https://www.reddit.com/r/MachineLearning/search/?q=cursor&restrict_sr=1&sort=new'
                ],
                'type': 'reddit'
            },
            'github': {
                'urls': [
                    'https://github.com/getcursor/cursor',
                    'https://github.com/topics/cursor-ai'
                ],
                'type': 'github'
            },
            'discord': {
                'urls': [
                    'https://discord.gg/cursor'
                ],
                'type': 'discord'
            },
            'youtube': {
                'urls': [
                    'https://www.youtube.com/results?search_query=cursor+ai+tutorial',
                    'https://www.youtube.com/results?search_query=cursor+ai+review'
                ],
                'type': 'youtube'
            }
        }
        
        self.scraped_data = {
            'main_website': {},
            'reddit_posts': [],
            'github_repos': [],
            'discord_info': {},
            'youtube_videos': [],
            'community_insights': [],
            'tutorials_guides': [],
            'user_reviews': [],
            'metadata': {
                'scraped_at': datetime.now().isoformat(),
                'total_sources': 0,
                'successful_sources': 0
            }
        }
        
        # Khởi tạo Selenium driver
        self.driver = None
        self.init_selenium()
    
    def init_selenium(self):
        """Khởi tạo Selenium WebDriver"""
        try:
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--window-size=1920,1080')
            chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
            
            self.driver = webdriver.Chrome(
                service=webdriver.chrome.service.Service(ChromeDriverManager().install()),
                options=chrome_options
            )
            logging.info("✅ Khởi tạo Selenium thành công")
        except Exception as e:
            logging.error(f"❌ Lỗi khởi tạo Selenium: {e}")
            self.driver = None
    
    def scrape_reddit(self, url):
        """Cào Reddit posts"""
        logging.info(f"🔍 Cào Reddit: {url}")
        
        try:
            if self.driver:
                self.driver.get(url)
                time.sleep(3)
                
                # Tìm các post
                posts = self.driver.find_elements(By.CSS_SELECTOR, '[data-testid="post-container"]')
                
                reddit_data = []
                for post in posts[:10]:  # Lấy 10 post đầu
                    try:
                        title_elem = post.find_element(By.CSS_SELECTOR, 'h3')
                        title = title_elem.text.strip()
                        
                        # Tìm nội dung post
                        content_elem = post.find_element(By.CSS_SELECTOR, '[data-testid="post-content"]')
                        content = content_elem.text.strip()
                        
                        # Tìm số upvote
                        upvote_elem = post.find_element(By.CSS_SELECTOR, '[data-testid="vote-arrows"]')
                        upvotes = upvote_elem.text.strip()
                        
                        reddit_data.append({
                            'title': title,
                            'content': content[:500],  # Giới hạn 500 ký tự
                            'upvotes': upvotes,
                            'url': url,
                            'scraped_at': datetime.now().isoformat()
                        })
                    except Exception as e:
                        logging.warning(f"Lỗi khi cào post Reddit: {e}")
                        continue
                
                return reddit_data
            else:
                # Fallback với requests
                response = self.session.get(url)
                soup = BeautifulSoup(response.content, 'html.parser')
                return []
                
        except Exception as e:
            logging.error(f"Lỗi cào Reddit {url}: {e}")
            return []
    
    def scrape_github(self, url):
        """Cào GitHub repositories"""
        logging.info(f"🔍 Cào GitHub: {url}")
        
        try:
            response = self.session.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            github_data = []
            
            # Tìm các repository
            repos = soup.find_all('article', class_='Box-row')
            
            for repo in repos[:10]:  # Lấy 10 repo đầu
                try:
                    title_elem = repo.find('h3', class_='wb-break-all')
                    if title_elem:
                        title = title_elem.get_text().strip()
                        
                        # Tìm mô tả
                        desc_elem = repo.find('p', class_='col-9')
                        description = desc_elem.get_text().strip() if desc_elem else ""
                        
                        # Tìm stars
                        stars_elem = repo.find('a', href=lambda x: x and '/stargazers' in x)
                        stars = stars_elem.get_text().strip() if stars_elem else "0"
                        
                        github_data.append({
                            'title': title,
                            'description': description,
                            'stars': stars,
                            'url': url,
                            'scraped_at': datetime.now().isoformat()
                        })
                except Exception as e:
                    logging.warning(f"Lỗi khi cào repo GitHub: {e}")
                    continue
            
            return github_data
            
        except Exception as e:
            logging.error(f"Lỗi cào GitHub {url}: {e}")
            return []
    
    def scrape_youtube(self, url):
        """Cào YouTube videos"""
        logging.info(f"🔍 Cào YouTube: {url}")
        
        try:
            if self.driver:
                self.driver.get(url)
                time.sleep(5)
                
                # Tìm các video
                videos = self.driver.find_elements(By.CSS_SELECTOR, 'ytd-video-renderer')
                
                youtube_data = []
                for video in videos[:10]:  # Lấy 10 video đầu
                    try:
                        title_elem = video.find_element(By.CSS_SELECTOR, '#video-title')
                        title = title_elem.get_attribute('title')
                        
                        # Tìm channel
                        channel_elem = video.find_element(By.CSS_SELECTOR, '#channel-name a')
                        channel = channel_elem.text.strip()
                        
                        # Tìm views
                        views_elem = video.find_element(By.CSS_SELECTOR, '#metadata-line span:first-child')
                        views = views_elem.text.strip()
                        
                        # Tìm link
                        link_elem = video.find_element(By.CSS_SELECTOR, '#video-title')
                        video_url = link_elem.get_attribute('href')
                        
                        youtube_data.append({
                            'title': title,
                            'channel': channel,
                            'views': views,
                            'url': video_url,
                            'scraped_at': datetime.now().isoformat()
                        })
                    except Exception as e:
                        logging.warning(f"Lỗi khi cào video YouTube: {e}")
                        continue
                
                return youtube_data
            else:
                return []
                
        except Exception as e:
            logging.error(f"Lỗi cào YouTube {url}: {e}")
            return []
    
    def scrape_main_website_advanced(self):
        """Cào website chính với thông tin chi tiết hơn"""
        logging.info("🚀 Cào website chính với thông tin nâng cao...")
        
        main_data = {
            'homepage': {},
            'features': {},
            'pricing': {},
            'docs': {},
            'blog': {}
        }
        
        for page_name, url in [
            ('homepage', 'https://cursor.com'),
            ('features', 'https://cursor.com/features'),
            ('pricing', 'https://cursor.com/pricing'),
            ('docs', 'https://cursor.com/docs'),
            ('blog', 'https://cursor.com/blog')
        ]:
            logging.info(f"📄 Cào trang: {page_name}")
            
            try:
                response = self.session.get(url, timeout=30)
                response.raise_for_status()
                soup = BeautifulSoup(response.content, 'html.parser')
                
                page_data = {
                    'url': url,
                    'title': soup.find('title').text if soup.find('title') else '',
                    'description': '',
                    'headings': [],
                    'content_sections': [],
                    'ai_mentions': [],
                    'code_examples': [],
                    'testimonials': [],
                    'cta_buttons': [],
                    'scraped_at': datetime.now().isoformat()
                }
                
                # Meta description
                meta_desc = soup.find('meta', attrs={'name': 'description'})
                if meta_desc:
                    page_data['description'] = meta_desc.get('content', '')
                
                # Headings
                for tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                    for heading in soup.find_all(tag):
                        text = heading.get_text().strip()
                        if text:
                            page_data['headings'].append({
                                'level': tag,
                                'text': text
                            })
                
                # Content sections
                for section in soup.find_all(['div', 'section'], class_=re.compile(r'content|section|feature|benefit', re.I)):
                    section_text = section.get_text().strip()
                    if section_text and len(section_text) > 50:
                        page_data['content_sections'].append(section_text)
                
                # AI mentions
                ai_keywords = ['AI', 'artificial intelligence', 'machine learning', 'neural', 'GPT', 'assistant', 'intelligent', 'smart', 'automated']
                for element in soup.find_all(text=re.compile('|'.join(ai_keywords), re.I)):
                    if element.parent:
                        ai_text = element.parent.get_text().strip()
                        if ai_text and len(ai_text) > 30:
                            page_data['ai_mentions'].append(ai_text)
                
                # Code examples
                for code_block in soup.find_all(['code', 'pre']):
                    code_text = code_block.get_text().strip()
                    if code_text and len(code_text) > 20:
                        page_data['code_examples'].append(code_text)
                
                # Testimonials
                for testimonial in soup.find_all(['div', 'blockquote'], class_=re.compile(r'testimonial|review|quote|feedback', re.I)):
                    testimonial_text = testimonial.get_text().strip()
                    if testimonial_text and len(testimonial_text) > 30:
                        page_data['testimonials'].append(testimonial_text)
                
                # CTA buttons
                for button in soup.find_all(['button', 'a'], class_=re.compile(r'cta|button|download|get|start|try', re.I)):
                    button_text = button.get_text().strip()
                    if button_text:
                        page_data['cta_buttons'].append(button_text)
                
                main_data[page_name] = page_data
                logging.info(f"✅ Đã cào xong {page_name}: {len(page_data['headings'])} headings, {len(page_data['content_sections'])} sections")
                
            except Exception as e:
                logging.error(f"❌ Lỗi cào {page_name}: {e}")
                main_data[page_name] = {'error': str(e)}
        
        self.scraped_data['main_website'] = main_data
    
    def scrape_community_sources(self):
        """Cào các nguồn cộng đồng"""
        logging.info("🌐 Bắt đầu cào các nguồn cộng đồng...")
        
        # Reddit
        for url in self.sources['reddit']['urls']:
            reddit_posts = self.scrape_reddit(url)
            self.scraped_data['reddit_posts'].extend(reddit_posts)
            time.sleep(2)
        
        # GitHub
        for url in self.sources['github']['urls']:
            github_repos = self.scrape_github(url)
            self.scraped_data['github_repos'].extend(github_repos)
            time.sleep(2)
        
        # YouTube
        for url in self.sources['youtube']['urls']:
            youtube_videos = self.scrape_youtube(url)
            self.scraped_data['youtube_videos'].extend(youtube_videos)
            time.sleep(3)
    
    def extract_community_insights(self):
        """Trích xuất insights từ cộng đồng"""
        logging.info("💡 Trích xuất insights từ cộng đồng...")
        
        insights = {
            'common_issues': [],
            'feature_requests': [],
            'user_tips': [],
            'tutorials': [],
            'reviews': [],
            'discussions': []
        }
        
        # Từ Reddit posts
        for post in self.scraped_data['reddit_posts']:
            title = post.get('title', '').lower()
            content = post.get('content', '').lower()
            
            if any(keyword in title for keyword in ['tutorial', 'guide', 'how to', 'tips']):
                insights['tutorials'].append(post)
            elif any(keyword in title for keyword in ['review', 'opinion', 'thoughts']):
                insights['reviews'].append(post)
            elif any(keyword in title for keyword in ['issue', 'problem', 'bug', 'error']):
                insights['common_issues'].append(post)
            elif any(keyword in title for keyword in ['request', 'suggestion', 'feature']):
                insights['feature_requests'].append(post)
            else:
                insights['discussions'].append(post)
        
        # Từ YouTube videos
        for video in self.scraped_data['youtube_videos']:
            title = video.get('title', '').lower()
            if any(keyword in title for keyword in ['tutorial', 'guide', 'how to', 'tips', 'review']):
                insights['tutorials'].append(video)
        
        self.scraped_data['community_insights'] = insights
    
    def save_advanced_data(self):
        """Lưu dữ liệu nâng cao"""
        # Tạo thư mục
        os.makedirs('cursor_ai_library_advanced', exist_ok=True)
        
        # Lưu dữ liệu JSON
        with open('cursor_ai_library_advanced/advanced_data.json', 'w', encoding='utf-8') as f:
            json.dump(self.scraped_data, f, ensure_ascii=False, indent=2)
        
        # Tạo báo cáo cộng đồng
        self.create_community_report()
        
        logging.info("💾 Đã lưu dữ liệu nâng cao vào cursor_ai_library_advanced/")
    
    def create_community_report(self):
        """Tạo báo cáo về cộng đồng"""
        report = f"""# CURSOR AI - BÁO CÁO CỘNG ĐỒNG

*Tài liệu được tạo tự động - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}*

## 🌐 CÁC NGUỒN CỘNG ĐỒNG ĐÃ CÀO

### Reddit Posts
- **Tổng số posts:** {len(self.scraped_data['reddit_posts'])}
- **Nguồn:** r/cursor, r/cursorai, r/MachineLearning

### GitHub Repositories
- **Tổng số repos:** {len(self.scraped_data['github_repos'])}
- **Nguồn:** github.com/getcursor/cursor, github.com/topics/cursor-ai

### YouTube Videos
- **Tổng số videos:** {len(self.scraped_data['youtube_videos'])}
- **Nguồn:** YouTube search results

## 💡 INSIGHTS TỪ CỘNG ĐỒNG

### Tutorials và Hướng dẫn
"""
        
        for tutorial in self.scraped_data['community_insights']['tutorials'][:10]:
            report += f"- {tutorial.get('title', 'N/A')}\n"
        
        report += f"""
### Reviews và Đánh giá
"""
        
        for review in self.scraped_data['community_insights']['reviews'][:10]:
            report += f"- {review.get('title', 'N/A')}\n"
        
        report += f"""
### Vấn đề thường gặp
"""
        
        for issue in self.scraped_data['community_insights']['common_issues'][:10]:
            report += f"- {issue.get('title', 'N/A')}\n"
        
        report += f"""
### Feature Requests
"""
        
        for request in self.scraped_data['community_insights']['feature_requests'][:10]:
            report += f"- {request.get('title', 'N/A')}\n"
        
        report += f"""
## 🔗 CÁC DIỄN ĐÀN VÀ CỘNG ĐỒNG QUAN TRỌNG

### 1. Reddit Communities
- **r/cursor** - Cộng đồng chính về Cursor
- **r/cursorai** - Thảo luận về Cursor AI
- **r/MachineLearning** - Thảo luận về AI/ML

### 2. GitHub
- **github.com/getcursor/cursor** - Repository chính
- **github.com/topics/cursor-ai** - Các project liên quan

### 3. YouTube Channels
- Tìm kiếm "cursor ai tutorial" để tìm hướng dẫn
- Tìm kiếm "cursor ai review" để tìm đánh giá

### 4. Discord
- **discord.gg/cursor** - Server Discord chính thức

## 📚 TÀI LIỆU HỌC TẬP

### Từ cộng đồng:
"""
        
        for tutorial in self.scraped_data['community_insights']['tutorials'][:15]:
            report += f"- {tutorial.get('title', 'N/A')}\n"
            if tutorial.get('url'):
                report += f"  Link: {tutorial['url']}\n"
        
        report += f"""
## 🎯 KHUYẾN NGHỊ CHO ANH NGHĨA

### Để học Cursor hiệu quả:
1. **Tham gia Reddit communities** - Cập nhật thông tin mới nhất
2. **Xem YouTube tutorials** - Học cách sử dụng thực tế
3. **Tham gia Discord** - Hỏi đáp trực tiếp với cộng đồng
4. **Theo dõi GitHub** - Cập nhật phiên bản mới
5. **Đọc user reviews** - Hiểu ưu nhược điểm

### Các chủ đề nên tìm hiểu:
- Cài đặt và setup Cursor
- Các tính năng AI chính
- Tips và tricks sử dụng
- Troubleshooting thường gặp
- So sánh với các công cụ khác

---
*Báo cáo được tạo tự động từ dữ liệu cộng đồng*
"""
        
        with open('cursor_ai_library_advanced/COMMUNITY_REPORT.md', 'w', encoding='utf-8') as f:
            f.write(report)
    
    def run_advanced_scraping(self):
        """Chạy cào web nâng cao"""
        logging.info("🚀 Bắt đầu cào web nâng cao...")
        
        try:
            # Cào website chính
            self.scrape_main_website_advanced()
            
            # Cào các nguồn cộng đồng
            self.scrape_community_sources()
            
            # Trích xuất insights
            self.extract_community_insights()
            
            # Lưu dữ liệu
            self.save_advanced_data()
            
            logging.info("✅ Hoàn thành cào web nâng cao!")
            
        except Exception as e:
            logging.error(f"❌ Lỗi trong quá trình cào web: {e}")
        finally:
            if self.driver:
                self.driver.quit()

if __name__ == "__main__":
    scraper = AdvancedCursorScraper()
    scraper.run_advanced_scraping()