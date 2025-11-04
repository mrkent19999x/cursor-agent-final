# 🚀 HƯỚNG DẪN SETUP CUSTOM MODES & SLASH COMMANDS

## 📋 TÓM TẮT

Em đã tạo cho anh:
- ✅ **3 Custom Modes:** Manager, Automation, Research
- ✅ **5 Slash Commands:** setup-project, analyze, research, deploy, report
- ✅ **Proposal document:** CUSTOM_MODES_PROPOSAL.md

---

## 🎯 BƯỚC 1: SETUP CUSTOM MODES

### 1️⃣ Manager Mode
**File:** `CUSTOM_MODE_MANAGER.md`

**Cách setup:**
1. Mở Cursor Settings → Chat → Custom Modes
2. Click "Create New Mode"
3. Tên: `Manager`
4. Copy toàn bộ nội dung từ `CUSTOM_MODE_MANAGER.md`
5. Paste vào "Instructions"
6. Tools: Chọn "All Search", "Terminal", "Edit & Reapply"
7. Save

**Khi nào dùng:**
- Cần báo cáo tiến độ dự án
- Phân tích risks và opportunities
- Review performance của team
- Tạo executive summary

---

### 2️⃣ Automation Mode
**File:** `CUSTOM_MODE_AUTOMATION.md`

**Cách setup:**
1. Mở Cursor Settings → Chat → Custom Modes
2. Click "Create New Mode"
3. Tên: `Automation`
4. Copy toàn bộ nội dung từ `CUSTOM_MODE_AUTOMATION.md`
5. Paste vào "Instructions"
6. Tools: Chọn "Terminal", "Edit & Reapply", "All Search"
7. Save

**Khi nào dùng:**
- Setup project mới
- Deploy ứng dụng
- Monitor hệ thống
- Tự động hóa tasks

---

### 3️⃣ Research Mode
**File:** `CUSTOM_MODE_RESEARCH.md`

**Cách setup:**
1. Mở Cursor Settings → Chat → Custom Modes
2. Click "Create New Mode"
3. Tên: `Research`
4. Copy toàn bộ nội dung từ `CUSTOM_MODE_RESEARCH.md`
5. Paste vào "Instructions"
6. Tools: Chọn "Web Search", "Browser", "Terminal", "Edit & Reapply"
7. Save

**Khi nào dùng:**
- Tìm hiểu về Cursor features
- Research best practices
- Cache documentation
- Tìm giải pháp cho vấn đề

---

## ⚡ BƯỚC 2: SETUP SLASH COMMANDS

### 📁 Location
Slash Commands đã được tạo trong:
```
.cursor/commands/
├── setup-project.md
├── analyze.md
├── research.md
├── deploy.md
└── report.md
```

### ✅ Cách sử dụng
1. Trong Cursor chat, gõ `/`
2. Cursor sẽ hiển thị danh sách commands
3. Chọn command cần dùng
4. Nhập parameters (nếu có)

### 📋 Commands Available

#### 1. `/setup-project <name> [type]`
**Ví dụ:**
```
/setup-project my-web-app web
/setup-project api-service api
```

**Chức năng:**
- Tự động setup project hoàn chỉnh
- Tạo structure, README, package.json, scripts
- Init git repository

---

#### 2. `/analyze [path]`
**Ví dụ:**
```
/analyze
/analyze ./src
/analyze ../my-project
```

**Chức năng:**
- Phân tích codebase
- Tạo báo cáo Executive Summary
- Phân tích risks và opportunities

---

#### 3. `/research <topic>`
**Ví dụ:**
```
/research custom modes
/research slash commands
/research MCP servers integration
```

**Chức năng:**
- Research từ nhiều nguồn
- Cache vào repo
- Push lên GitHub

---

#### 4. `/deploy <project> [env]`
**Ví dụ:**
```
/deploy my-web-app staging
/deploy api-service production
```

**Chức năng:**
- Deploy project tự động
- Run tests và build
- Monitor deployment

---

#### 5. `/report <type> [project]`
**Ví dụ:**
```
/report progress my-web-app
/report performance api-service
/report risks automation-tool
/report summary
```

**Chức năng:**
- Tạo báo cáo quản lý
- Executive Summary
- Risk assessment

---

## 🌐 GLOBAL COMMANDS (Optional)

Nếu muốn dùng commands ở **mọi project**, copy vào:
```
~/.cursor/commands/
```

**Cách làm:**
```bash
# Copy commands vào global folder
cp -r .cursor/commands/* ~/.cursor/commands/
```

**Lưu ý:**
- Global commands sẽ có sẵn ở mọi project
- Project commands chỉ có trong project này

---

## 🧪 TEST

### Test Custom Modes:
1. Chọn mode từ dropdown (Agent → Custom Mode)
2. Test với một câu hỏi:
   - **Manager Mode:** "Phân tích tiến độ dự án này"
   - **Automation Mode:** "Setup project test-project"
   - **Research Mode:** "Tìm hiểu về Cursor custom modes"

### Test Slash Commands:
1. Gõ `/` trong chat
2. Xem danh sách commands
3. Test một command:
   ```
   /setup-project test-project
   /analyze
   /research custom modes
   ```

---

## 📊 SO SÁNH MODES

| Tính năng | Manager | Automation | Research |
|-----------|---------|-------------|----------|
| **Focus** | Báo cáo, phân tích | Tự động hóa | Nghiên cứu |
| **Tools** | Search, Terminal, Edit | Terminal, Edit, Search | Web, Browser, Terminal |
| **Output** | Executive Summary | Project structure | Research report |
| **Khi nào dùng** | Báo cáo sếp | Setup/Deploy | Tìm hiểu features |

---

## 💡 TIPS

### 1. Switch Mode Nhanh
- Dùng keyboard shortcut (nếu có)
- Hoặc chọn từ dropdown

### 2. Combine Commands
- `/setup-project` → `/analyze` → `/report`
- Tự động hóa workflow hoàn chỉnh

### 3. Cache Research
- Dùng `/research` để cache docs
- Tái sử dụng sau này

---

## ❓ TROUBLESHOOTING

### Commands không hiện?
- Check `.cursor/commands/` folder có đúng không
- Restart Cursor
- Check file format (phải là `.md`)

### Mode không hoạt động?
- Check Instructions đã copy đúng chưa
- Check Tools đã chọn chưa
- Restart Cursor

### Scripts không chạy?
- Check permissions: `chmod +x scripts/*.sh`
- Check paths trong scripts
- Check environment variables

---

## 📚 TÀI LIỆU THAM KHẢO

- **Proposal:** `CUSTOM_MODES_PROPOSAL.md`
- **Manager Mode:** `CUSTOM_MODE_MANAGER.md`
- **Automation Mode:** `CUSTOM_MODE_AUTOMATION.md`
- **Research Mode:** `CUSTOM_MODE_RESEARCH.md`
- **Commands:** `.cursor/commands/*.md`

---

## ✅ CHECKLIST

- [ ] Đã setup Manager Mode
- [ ] Đã setup Automation Mode
- [ ] Đã setup Research Mode
- [ ] Đã test Slash Commands
- [ ] Đã test Custom Modes
- [ ] Đã setup Global Commands (optional)
- [ ] Đã đọc Proposal document

---

**Tạo bởi:** Cipher Assistant  
**Ngày:** 2025-01-11  
**Version:** 1.0

