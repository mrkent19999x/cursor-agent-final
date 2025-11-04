# 🔑 Hướng dẫn cập nhật API Keys cho Cursor Agent Learning Hub

## 📋 Danh sách API Keys cần thiết

### 🟢 **API Keys có thể lấy miễn phí:**

#### 1. **Notion API** (Miễn phí)
- Truy cập: https://www.notion.so/my-integrations
- Tạo integration mới
- Copy API key
- **Thay thế**: `NOTION_API_KEY=your_notion_api_key_here`

#### 2. **Supabase** (Miễn phí)
- Truy cập: https://supabase.com/
- Tạo project mới
- Vào Settings → API
- Copy URL và anon key
- **Thay thế**: 
  - `SUPABASE_URL=your_supabase_url_here`
  - `SUPABASE_ANON_KEY=your_supabase_anon_key_here`

#### 3. **Tavily Search** (Miễn phí với giới hạn)
- Truy cập: https://tavily.com/
- Đăng ký tài khoản
- Lấy API key từ dashboard
- **Thay thế**: `TAVILY_API_KEY=your_tavily_api_key_here`

#### 4. **GitHub Token** (Miễn phí)
- Truy cập: https://github.com/settings/tokens
- Tạo Personal Access Token
- Chọn quyền: repo, user, admin:org
- **Thay thế**: `GITHUB_TOKEN=your_github_token_here`

### 🟡 **API Keys có thể test miễn phí:**

#### 5. **Sentry** (Miễn phí với giới hạn)
- Truy cập: https://sentry.io/
- Tạo project mới
- Vào Settings → Auth Tokens
- Tạo token mới
- **Thay thế**:
  - `SENTRY_AUTH_TOKEN=your_sentry_token_here`
  - `SENTRY_ORG=your_sentry_org_here`
  - `SENTRY_PROJECT=your_sentry_project_here`

#### 6. **Heroku** (Miễn phí với giới hạn)
- Truy cập: https://dashboard.heroku.com/account
- Vào Account Settings
- Tạo API Key
- **Thay thế**: `HEROKU_API_KEY=your_heroku_api_key_here`

#### 7. **Apify** (Miễn phí với giới hạn)
- Truy cập: https://apify.com/
- Đăng ký tài khoản
- Vào Account → Integrations
- Lấy API token
- **Thay thế**: `APIFY_API_TOKEN=your_apify_token_here`

### 🔴 **API Keys trả phí (có thể bỏ qua):**

#### 8. **HubSpot** (Trả phí)
- Truy cập: https://developers.hubspot.com/
- Tạo app và lấy access token
- **Thay thế**: `HUBSPOT_ACCESS_TOKEN=your_hubspot_token_here`

#### 9. **Datadog** (Trả phí)
- Truy cập: https://app.datadoghq.com/
- Vào Organization Settings → API Keys
- **Thay thế**:
  - `DATADOG_API_KEY=your_datadog_api_key_here`
  - `DATADOG_APP_KEY=your_datadog_app_key_here`

#### 10. **Browserbase** (Trả phí)
- Truy cập: https://www.browserbase.com/
- Tạo project và lấy API key
- **Thay thế**:
  - `BROWSERBASE_API_KEY=your_browserbase_api_key_here`
  - `BROWSERBASE_PROJECT_ID=your_browserbase_project_id_here`

#### 11. **Firecrawl** (Trả phí)
- Truy cập: https://firecrawl.dev/
- Đăng ký và lấy API key
- **Thay thế**: `FIRECRAWL_API_KEY=your_firecrawl_api_key_here`

## 🚀 **Cách cập nhật nhanh:**

### **Bước 1: Mở file environment.env**
```bash
nano /workspace/configs/environment.env
```

### **Bước 2: Thay thế các API keys**
Tìm và thay thế các dòng sau:

```bash
# Core MCP Servers (Required)
FIRECRAWL_API_KEY=your_firecrawl_api_key_here
GITHUB_TOKEN=your_github_token_here

# Business & Management MCPs
NOTION_API_KEY=your_notion_api_key_here
SENTRY_AUTH_TOKEN=your_sentry_auth_token_here
SENTRY_ORG=your_sentry_org_here
SENTRY_PROJECT=your_sentry_project_here
HEROKU_API_KEY=your_heroku_api_key_here
SUPABASE_URL=your_supabase_url_here
SUPABASE_ANON_KEY=your_supabase_anon_key_here
APIFY_API_TOKEN=your_apify_api_token_here
HUBSPOT_ACCESS_TOKEN=your_hubspot_access_token_here
TAVILY_API_KEY=your_tavily_api_key_here
DATADOG_API_KEY=your_datadog_api_key_here
DATADOG_APP_KEY=your_datadog_app_key_here

# Browser & Automation MCPs
BROWSERBASE_API_KEY=your_browserbase_api_key_here
BROWSERBASE_PROJECT_ID=your_browserbase_project_id_here
```

### **Bước 3: Lưu file**
- Nhấn `Ctrl + X`
- Nhấn `Y` để xác nhận
- Nhấn `Enter` để lưu

## 🎯 **API Keys tối thiểu để test:**

Để test hệ thống cơ bản, bạn chỉ cần:

1. **Notion API** - Để test Notion MCP
2. **Supabase** - Để test Supabase MCP  
3. **GitHub Token** - Để test GitHub MCP
4. **Tavily API** - Để test web search

## 📝 **Lưu ý quan trọng:**

- ✅ **Không chia sẻ API keys** với ai khác
- ✅ **Không commit API keys** vào Git
- ✅ **Sử dụng environment variables** để bảo mật
- ✅ **Test từng API key** sau khi cập nhật
- ✅ **Backup file environment.env** trước khi chỉnh sửa

## 🧪 **Test sau khi cập nhật:**

```bash
# Test MCP configuration
node test-mcp-config.js

# Test individual API keys
echo $NOTION_API_KEY
echo $SUPABASE_URL
echo $GITHUB_TOKEN
```

---

**🎉 Sau khi cập nhật API keys, hệ thống sẽ sẵn sàng để sử dụng với Cursor IDE!**