# MCP Configuration Guide - Cấu hình MCP cục bộ

## Tổng quan (Overview)
Hướng dẫn này sẽ giúp bạn cấu hình MCP (Model Context Protocol) servers trên máy cục bộ để sử dụng với Cursor IDE.

## Các bước đã hoàn thành (Completed Steps)

### ✅ 1. Kiểm tra Dependencies
- Node.js v22.16.0 ✅
- npm v10.9.2 ✅  
- Python 3.13.3 ✅
- pipx ✅

### ✅ 2. Cài đặt MCP Servers
Đã cài đặt thành công các MCP servers sau:
- **Notion MCP** ✅ - Quản lý tài liệu Notion
- **Sentry MCP** ✅ - Giám sát lỗi và hiệu suất
- **Supabase MCP** ✅ - Quản lý cơ sở dữ liệu
- **Apify MCP** ✅ - Web scraping và automation
- **Filesystem MCP** ⚠️ - Truy cập hệ thống file (cần cấu hình thêm)
- **Sequential Thinking MCP** ⚠️ - Tư duy tuần tự (cần cấu hình thêm)

### ✅ 3. Cấu hình Files
- `/workspace/configs/cursor-settings.json` - Cấu hình Cursor IDE
- `/workspace/configs/environment.env` - API keys và biến môi trường

## Các bước tiếp theo (Next Steps)

### 🔧 1. Cập nhật API Keys
Chỉnh sửa file `/workspace/configs/environment.env` và thay thế các placeholder:

```bash
# Core MCP Servers
FIRECRAWL_API_KEY=your_actual_firecrawl_api_key
GITHUB_TOKEN=your_actual_github_token
FIGMA_TOKEN=your_actual_figma_token

# Business & Management MCPs
ATLASSIAN_API_TOKEN=your_actual_atlassian_token
LINEAR_API_KEY=your_actual_linear_key
NOTION_API_KEY=your_actual_notion_key

# New MCP Servers
SENTRY_AUTH_TOKEN=your_actual_sentry_token
SENTRY_ORG=your_sentry_org
SENTRY_PROJECT=your_sentry_project
HEROKU_API_KEY=your_actual_heroku_key
SUPABASE_URL=your_actual_supabase_url
SUPABASE_ANON_KEY=your_actual_supabase_key
APIFY_API_TOKEN=your_actual_apify_token
HUBSPOT_ACCESS_TOKEN=your_actual_hubspot_token
TAVILY_API_KEY=your_actual_tavily_key
DATADOG_API_KEY=your_actual_datadog_key
DATADOG_APP_KEY=your_actual_datadog_app_key
```

### 🔧 2. Cấu hình Cursor IDE
1. Sao chép nội dung từ `/workspace/configs/cursor-settings.json`
2. Mở Cursor IDE
3. Vào Settings → Extensions → MCP
4. Dán cấu hình vào file settings
5. Khởi động lại Cursor IDE

### 🔧 3. Test MCP Servers
Chạy script test để kiểm tra:
```bash
node test-mcp-config.js
```

## Các MCP Servers có sẵn (Available MCP Servers)

### 🟢 Hoạt động tốt (Working Well)
- **Notion** - Quản lý tài liệu và database
- **Sentry** - Giám sát lỗi và performance
- **Supabase** - Quản lý database và authentication
- **Apify** - Web scraping và data extraction

### 🟡 Cần cấu hình thêm (Need Configuration)
- **Filesystem** - Truy cập file system (cần quyền)
- **Sequential Thinking** - Tư duy logic tuần tự
- **Heroku** - Quản lý ứng dụng Heroku
- **HubSpot** - CRM và marketing automation
- **Tavily** - Web search nâng cao
- **Kubernetes** - Quản lý container orchestration
- **Datadog** - Monitoring và analytics

### 🔴 Cần API Keys (Require API Keys)
- **Firecrawl** - Web scraping
- **GitHub** - Repository management
- **Browserbase** - Cloud browser automation
- **Slack** - Communication
- **Qdrant** - Vector database
- **Docker** - Container management
- **PostgreSQL** - Database management

## Troubleshooting

### Lỗi thường gặp (Common Issues)

1. **Permission Denied**
   ```bash
   sudo chmod +x scripts/install-mcp-servers.sh
   ```

2. **Package Not Found**
   ```bash
   npm install -g @modelcontextprotocol/server-filesystem
   ```

3. **API Key Invalid**
   - Kiểm tra API key trong environment.env
   - Đảm bảo key có đủ quyền

4. **Timeout Errors**
   - Tăng timeout trong cấu hình
   - Kiểm tra kết nối internet

### Debug Commands
```bash
# Test individual MCP server
npx @modelcontextprotocol/server-filesystem --help

# Check installed packages
npm list -g | grep mcp

# Test environment variables
echo $NOTION_API_KEY
```

## Kết luận (Conclusion)

MCP configuration đã được thiết lập thành công với:
- ✅ 4 MCP servers hoạt động tốt
- ⚠️ 7 MCP servers cần cấu hình thêm
- 📁 Cấu hình files đã sẵn sàng
- 🧪 Test script để kiểm tra

**Bước tiếp theo**: Cập nhật API keys và test trong Cursor IDE.

---
*Tạo bởi: Cursor Agent Learning Hub*
*Ngày: $(date)*