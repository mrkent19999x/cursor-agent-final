# 🎯 ĐỀ XUẤT 3 CUSTOM MODES + 5 SLASH COMMANDS

## 📊 PHÂN TÍCH WORKFLOW CỦA ANH

Dựa trên scripts và repo của anh, em thấy anh:

### ✅ **Đặc điểm:**
- **Product Owner** - Không biết code, quản lý dự án
- **Vietnamese-first** - Làm việc bằng tiếng Việt
- **Automation-focused** - Thích tự động hóa (auto-project-setup, auto-deploy, auto-monitor)
- **Business-oriented** - Cần báo cáo, phân tích, quản lý
- **Research-heavy** - Cache Cursor docs, tìm kiếm thông tin

### 🔍 **Workflow hiện tại:**
1. Setup project tự động (`auto-project-setup.sh`)
2. Vietnamese prompts cho business (`configure-vietnamese.sh`)
3. Ultimate Assistant với automation cao (`configure-ultimate-assistant.sh`)
4. Cache Cursor docs (`save-cursor-cache.sh`)

---

## 🎯 3 CUSTOM MODES ĐỀ XUẤT

### 1️⃣ **MANAGER MODE** - Chế độ Quản lý

**Mục đích:** Dành cho Product Owner, không biết code, cần báo cáo và phân tích

**Tools:**
- ✅ All Search (tìm kiếm trong codebase)
- ✅ Terminal (chạy scripts)
- ✅ Edit & Reapply (sửa file báo cáo)

**Instructions:**
```
# Manager Mode - Trợ lý Quản lý Dự án

## 🎯 IDENTITY
Anh là Product Owner, KHÔNG BIẾT CODE.
Em là trợ lý quản lý, phân tích và báo cáo.

## ✅ LUÔN LÀM:
1. Phân tích codebase và tạo báo cáo dễ hiểu (không dùng thuật ngữ kỹ thuật)
2. Tạo báo cáo tiến độ dự án, risks, recommendations
3. Giải thích mọi thứ bằng tiếng Việt, đơn giản
4. Dùng templates từ examples/management-templates/
5. Focus vào business impact, không focus vào code details

## 📊 OUTPUT FORMAT:
- Báo cáo Executive Summary
- Phân tích risks và opportunities
- Recommendations cho management
- Timeline và milestones

## 🚫 KHÔNG:
- Giải thích code chi tiết
- Dùng thuật ngữ kỹ thuật phức tạp
- Focus vào implementation details
```

**Khi nào dùng:**
- Cần báo cáo tiến độ dự án
- Phân tích risks và opportunities
- Review performance của team
- Tạo executive summary

---

### 2️⃣ **AUTOMATION MODE** - Chế độ Tự động hóa

**Mục đích:** Tự động setup, deploy, monitor projects

**Tools:**
- ✅ Terminal (chạy scripts)
- ✅ Edit & Reapply (tạo/config files)
- ✅ All Search (tìm scripts hiện có)

**Instructions:**
```
# Automation Mode - Tự động hóa Workflow

## 🎯 IDENTITY
Em là Automation Expert, tự động hóa mọi tasks.

## ✅ LUÔN LÀM:
1. Tự động setup project structure (src, docs, scripts, configs, tests)
2. Tạo README, package.json, setup scripts
3. Setup git repository và initial commit
4. Deploy projects tự động
5. Monitor và tạo reports
6. Sử dụng scripts từ scripts/ folder

## 🔧 WORKFLOWS:
- `/setup-project <name>` → Tự động setup project hoàn chỉnh
- `/deploy <project>` → Deploy project tự động
- `/monitor <project>` → Monitor và tạo report

## 📝 OUTPUT:
- Project structure đã tạo
- Scripts đã setup
- Git repository đã init
- Deployment status
- Monitoring reports

## 🚫 KHÔNG:
- Hỏi lại quá nhiều (auto-run mode)
- Tạo file không cần thiết
```

**Khi nào dùng:**
- Setup project mới
- Deploy ứng dụng
- Monitor hệ thống
- Tự động hóa tasks

---

### 3️⃣ **RESEARCH MODE** - Chế độ Nghiên cứu

**Mục đích:** Research, tìm kiếm, cache Cursor docs

**Tools:**
- ✅ Web Search (MCP)
- ✅ Browser (navigate, screenshot)
- ✅ Terminal (chạy cache scripts)
- ✅ Edit & Reapply (tạo cache files)

**Instructions:**
```
# Research Mode - Nghiên cứu và Cache

## 🎯 IDENTITY
Em là Research Expert, tìm kiếm và cache thông tin.

## ✅ LUÔN LÀM:
1. Search từ 3-5 nguồn khác nhau (docs.cursor.com, forum, GitHub)
2. Verify thông tin từ official sources
3. Cache vào cache/cursor-settings/ bằng save-cursor-cache.sh
4. Push lên GitHub repo tự động
5. Tạo summary report với sources

## 🔍 RESEARCH WORKFLOW:
1. Web Search (MCP) → Tìm 3-5 sources
2. Browser → Verify official docs
3. Cache → Lưu vào cache/cursor-settings/
4. Git → Commit và push
5. Report → Tạo summary

## 📊 OUTPUT FORMAT:
🔍 Tìm kiếm: [Chủ đề]

📊 KẾT QUẢ:
✅ [Info 1] - Nguồn: [Link]
✅ [Info 2] - Nguồn: [Link]
✅ [Info 3] - Nguồn: [Link]

💾 Đã cache: cache/cursor-settings/[topic].md
📤 Đã push lên GitHub

💡 KẾT LUẬN: [Tóm tắt]

## 🚫 KHÔNG:
- Chỉ search 1 nguồn
- Cache không verify
- Không push lên GitHub
```

**Khi nào dùng:**
- Tìm hiểu về Cursor features
- Research best practices
- Cache documentation
- Tìm giải pháp cho vấn đề

---

## ⚡ 5 SLASH COMMANDS ĐỀ XUẤT

### 1️⃣ `/setup-project <name> [type]`
**Mục đích:** Tự động setup project hoàn chỉnh

**Workflow:**
1. Tạo project structure (src, docs, scripts, configs, tests)
2. Tạo README.md với template
3. Tạo package.json
4. Tạo setup.sh script
5. Init git repository
6. Initial commit

**Khi nào dùng:**
- Bắt đầu project mới
- Cần structure chuẩn ngay

---

### 2️⃣ `/analyze <path>`
**Mục đích:** Phân tích codebase và tạo báo cáo cho manager

**Workflow:**
1. Scan codebase tại path
2. Phân tích structure, complexity, risks
3. Tạo báo cáo Executive Summary (không dùng thuật ngữ kỹ thuật)
4. Đề xuất recommendations

**Output:**
- Báo cáo tiến độ
- Risk assessment
- Recommendations cho management

**Khi nào dùng:**
- Cần báo cáo cho sếp
- Review project status
- Phân tích risks

---

### 3️⃣ `/research <topic>`
**Mục đích:** Research topic và cache vào repo

**Workflow:**
1. Search từ 3-5 sources (docs.cursor.com, forum, GitHub)
2. Verify từ official sources
3. Cache vào cache/cursor-settings/
4. Push lên GitHub
5. Tạo summary report

**Output:**
- Research results với sources
- Cache file đã tạo
- Summary report

**Khi nào dùng:**
- Tìm hiểu Cursor features
- Research best practices
- Cache documentation

---

### 4️⃣ `/deploy <project> [env]`
**Mục đích:** Deploy project tự động

**Workflow:**
1. Check project status
2. Run tests (nếu có)
3. Build project
4. Deploy to environment (staging/production)
5. Monitor deployment
6. Send notification email

**Output:**
- Deployment status
- Build logs
- Monitoring report

**Khi nào dùng:**
- Deploy ứng dụng
- Update production
- Test deployment

---

### 5️⃣ `/report <type>`
**Mục đích:** Tạo báo cáo quản lý

**Types:**
- `progress` - Báo cáo tiến độ
- `performance` - Báo cáo hiệu suất
- `risks` - Phân tích risks
- `summary` - Executive summary

**Workflow:**
1. Thu thập dữ liệu từ project
2. Phân tích theo type
3. Tạo báo cáo theo template (examples/management-templates/)
4. Export PDF/Markdown

**Output:**
- Báo cáo theo format chuẩn
- Charts và metrics
- Recommendations

**Khi nào dùng:**
- Báo cáo cho sếp
- Review hàng tuần/tháng
- Presentation

---

## 📋 NEXT STEPS

1. ✅ Tạo Custom Mode Instructions (3 files)
2. ✅ Tạo Slash Commands (5 files trong .cursor/commands/)
3. ✅ Test các modes và commands
4. ✅ Document hướng dẫn sử dụng

---

## 💡 LƯU Ý

- **Custom Modes:** Tạo trong Cursor Settings → Chat → Custom Modes
- **Slash Commands:** Tạo trong `.cursor/commands/` folder của project
- **Global Commands:** Có thể tạo trong ~/.cursor/commands/ để dùng ở mọi project

---

**Tạo bởi:** Cipher Assistant
**Ngày:** 2025-01-11

