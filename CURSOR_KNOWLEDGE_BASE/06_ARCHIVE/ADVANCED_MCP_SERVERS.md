# 🚀 Danh sách MCP Servers hữu ích và công cụ thay thế Web Search

## 📋 MCP Servers hữu ích bổ sung

### 🔧 Core MCP Servers (Chính thức)
```bash
# Filesystem access - Truy cập file hệ thống
npm install -g @modelcontextprotocol/server-filesystem

# SQLite database - Cơ sở dữ liệu SQLite
npm install -g @modelcontextprotocol/server-sqlite

# Memory management - Quản lý bộ nhớ
npm install -g @modelcontextprotocol/server-memory

# Fetch HTTP requests - Gửi HTTP requests
npm install -g @modelcontextprotocol/server-fetch
```

### 🌐 Web & Search MCPs
```bash
# Tavily Search - Tìm kiếm web AI-powered
npm install -g tavily-mcp

# Brave Search - Tìm kiếm Brave
npm install -g brave-search-mcp-server

# DuckDuckGo Search - Tìm kiếm riêng tư
npm install -g duckduckgo-mcp-server

# Google Search - Tìm kiếm Google
npm install -g google-search-mcp-server
```

### 📅 Productivity MCPs
```bash
# Calendar integration - Tích hợp lịch
npm install -g calendar-mcp-server

# Email management - Quản lý email
npm install -g email-mcp-server

# Weather information - Thông tin thời tiết
npm install -g weather-mcp-server

# Time zone management - Quản lý múi giờ
npm install -g time-mcp-server
```

### 🎵 Media & Entertainment MCPs
```bash
# YouTube integration - Tích hợp YouTube
npm install -g youtube-mcp-server

# Spotify music - Âm nhạc Spotify
npm install -g spotify-mcp-server

# Podcast management - Quản lý podcast
npm install -g podcast-mcp-server
```

### 💼 Business & Finance MCPs
```bash
# Stock market data - Dữ liệu thị trường chứng khoán
npm install -g stock-mcp-server

# Cryptocurrency - Tiền điện tử
npm install -g crypto-mcp-server

# Banking integration - Tích hợp ngân hàng
npm install -g banking-mcp-server
```

### 🛠️ Development Tools MCPs
```bash
# Figma integration - Tích hợp Figma
npm install -g figma-mcp

# Ref tools - Công cụ Ref
npm install -g ref-tools-mcp

# Puppeteer browser automation - Tự động hóa trình duyệt
npm install -g puppeteer-mcp-server

# Git operations - Thao tác Git
npm install -g git-mcp-server
```

### 📊 Analytics & Monitoring MCPs
```bash
# OneUptime monitoring - Giám sát OneUptime
npm install -g @oneuptime/mcp-server

# Google Analytics - Phân tích Google
npm install -g google-analytics-mcp-server

# Performance monitoring - Giám sát hiệu suất
npm install -g performance-mcp-server
```

## 🔄 Công cụ thay thế Web Search

### 1. **Tavily Search API** (Khuyến nghị)
```bash
# Cài đặt Tavily MCP
npm install -g tavily-mcp

# Cấu hình API key
export TAVILY_API_KEY="your_tavily_api_key"
```

**Ưu điểm:**
- AI-powered search
- Kết quả chính xác hơn
- Tích hợp tốt với AI models
- Real-time data

### 2. **Brave Search API**
```bash
# Cài đặt Brave Search MCP
npm install -g brave-search-mcp-server

# Cấu hình API key
export BRAVE_SEARCH_API_KEY="your_brave_api_key"
```

**Ưu điểm:**
- Không tracking
- Kết quả không bias
- API miễn phí với giới hạn

### 3. **DuckDuckGo Instant Answer API**
```bash
# Cài đặt DuckDuckGo MCP
npm install -g duckduckgo-mcp-server
```

**Ưu điểm:**
- Hoàn toàn riêng tư
- Không lưu trữ dữ liệu
- Instant answers

### 4. **Google Custom Search API**
```bash
# Cài đặt Google Search MCP
npm install -g google-search-mcp-server

# Cấu hình API keys
export GOOGLE_SEARCH_API_KEY="your_google_api_key"
export GOOGLE_SEARCH_ENGINE_ID="your_search_engine_id"
```

**Ưu điểm:**
- Kết quả từ Google
- Customizable search
- Rich snippets

## 🎯 Cấu hình API Keys cho tài khoản của bạn

### File `.env` được cập nhật:
```bash
# Web Search APIs
TAVILY_API_KEY=your_tavily_api_key_here
BRAVE_SEARCH_API_KEY=your_brave_api_key_here
GOOGLE_SEARCH_API_KEY=your_google_api_key_here
GOOGLE_SEARCH_ENGINE_ID=your_search_engine_id_here

# Media APIs
YOUTUBE_API_KEY=your_youtube_api_key_here
SPOTIFY_CLIENT_ID=your_spotify_client_id_here
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret_here

# Productivity APIs
GOOGLE_CALENDAR_API_KEY=your_google_calendar_api_key_here
GMAIL_API_KEY=your_gmail_api_key_here
WEATHER_API_KEY=your_weather_api_key_here

# Business APIs
ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key_here
COINMARKETCAP_API_KEY=your_coinmarketcap_api_key_here

# Development APIs
FIGMA_ACCESS_TOKEN=your_figma_access_token_here
GITHUB_TOKEN=your_github_token_here
```

## 🚀 Script cài đặt tự động

Tạo file `install-additional-mcp.sh`:

```bash
#!/bin/bash
echo "🔧 Installing additional MCP servers..."

# Core MCPs
npm install -g @modelcontextprotocol/server-filesystem
npm install -g @modelcontextprotocol/server-sqlite
npm install -g @modelcontextprotocol/server-memory
npm install -g @modelcontextprotocol/server-fetch

# Web Search MCPs
npm install -g tavily-mcp
npm install -g brave-search-mcp-server
npm install -g duckduckgo-mcp-server

# Productivity MCPs
npm install -g calendar-mcp-server
npm install -g email-mcp-server
npm install -g weather-mcp-server
npm install -g time-mcp-server

# Media MCPs
npm install -g youtube-mcp-server
npm install -g spotify-mcp-server

# Development MCPs
npm install -g figma-mcp
npm install -g ref-tools-mcp
npm install -g puppeteer-mcp-server

# Analytics MCPs
npm install -g @oneuptime/mcp-server

echo "✅ Additional MCP servers installed!"
```

## 📝 Cấu hình Cursor Settings mở rộng

Cập nhật `cursor-settings.json`:

```json
{
  "mcp.servers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/workspace"]
    },
    "sqlite": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sqlite", "--db-path", "/workspace/data.db"]
    },
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    },
    "fetch": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-fetch"]
    },
    "tavily": {
      "command": "npx",
      "args": ["-y", "tavily-mcp"],
      "env": {
        "TAVILY_API_KEY": "${env:TAVILY_API_KEY}"
      }
    },
    "brave-search": {
      "command": "npx",
      "args": ["-y", "brave-search-mcp-server"],
      "env": {
        "BRAVE_SEARCH_API_KEY": "${env:BRAVE_SEARCH_API_KEY}"
      }
    },
    "weather": {
      "command": "npx",
      "args": ["-y", "weather-mcp-server"],
      "env": {
        "WEATHER_API_KEY": "${env:WEATHER_API_KEY}"
      }
    },
    "youtube": {
      "command": "npx",
      "args": ["-y", "youtube-mcp-server"],
      "env": {
        "YOUTUBE_API_KEY": "${env:YOUTUBE_API_KEY}"
      }
    },
    "spotify": {
      "command": "npx",
      "args": ["-y", "spotify-mcp-server"],
      "env": {
        "SPOTIFY_CLIENT_ID": "${env:SPOTIFY_CLIENT_ID}",
        "SPOTIFY_CLIENT_SECRET": "${env:SPOTIFY_CLIENT_SECRET}"
      }
    },
    "figma": {
      "command": "npx",
      "args": ["-y", "figma-mcp"],
      "env": {
        "FIGMA_ACCESS_TOKEN": "${env:FIGMA_ACCESS_TOKEN}"
      }
    }
  }
}
```

## 🎯 Lợi ích của việc sử dụng API trực tiếp

### 1. **Tốc độ nhanh hơn**
- Không cần qua web browser
- Direct API calls
- Ít latency

### 2. **Kiểm soát tốt hơn**
- Custom parameters
- Filtered results
- Structured data

### 3. **Tích hợp tốt hơn**
- JSON responses
- Error handling
- Rate limiting

### 4. **Chi phí thấp hơn**
- API calls rẻ hơn web scraping
- Có free tiers
- Predictable pricing

## 📞 Hướng dẫn lấy API Keys

### Tavily API:
1. Truy cập: https://tavily.com/
2. Đăng ký tài khoản
3. Lấy API key từ dashboard

### Brave Search API:
1. Truy cập: https://brave.com/search/api/
2. Đăng ký developer account
3. Tạo API key

### YouTube API:
1. Truy cập: https://console.developers.google.com/
2. Enable YouTube Data API v3
3. Tạo credentials

### Spotify API:
1. Truy cập: https://developer.spotify.com/
2. Tạo app
3. Lấy Client ID và Secret

---

**🎉 Với cấu hình này, bạn sẽ có một hệ thống MCP mạnh mẽ và linh hoạt hơn nhiều!**