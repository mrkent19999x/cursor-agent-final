# 🛠️ AVAILABLE TOOLS REFERENCE - CURSOR AGENT

## ⚠️ QUAN TRỌNG: Agent PHẢI ĐỌC FILE NÀY TRƯỚC KHI DÙNG BẤT KỲ TOOL NÀO

**Cập nhật:** 2025-11-05  
**Mục đích:** Đảm bảo agent KHÔNG BAO GIỜ dùng tool không tồn tại

---

## ✅ TOOLS CÓ SẴN (PHẢI DÙNG ĐÚNG)

### 📁 File Operations

#### ✅ `edit_file` - Chỉnh sửa file
- **Syntax:** `edit_file(target_file, instructions, code_edit)`
- **Dùng khi:** Cần edit file, tạo file mới
- **Ví dụ:** `edit_file("/path/to/file.md", "Add section", "# New Section")`

#### ✅ `search_replace` - Thay thế text trong file
- **Syntax:** `search_replace(file_path, old_string, new_string)`
- **Dùng khi:** Cần thay đổi một đoạn text cụ thể
- **Lưu ý:** old_string phải match chính xác (kể cả whitespace)

#### ✅ `file_search` - Tìm file
- **Syntax:** `file_search(query)`
- **Dùng khi:** Cần tìm file trong workspace
- **Ví dụ:** `file_search("mcp.json")`

#### ✅ `delete_file` - Xóa file
- **Syntax:** `delete_file(target_file)`
- **Dùng khi:** Cần xóa file

---

### 🖥️ Terminal Operations

#### ✅ `run_terminal_cmd` - Chạy lệnh terminal
- **Syntax:** `run_terminal_cmd(command, is_background, require_user_approval)`
- **Dùng khi:** Cần chạy bất kỳ lệnh shell nào
- **ĐỌC FILE:** Dùng `run_terminal_cmd("cat /path/to/file")` thay vì `read_file`
- **Ví dụ đọc file:**
  ```bash
  run_terminal_cmd("cat ~/.cursor/mcp.json", false, false)
  ```

---

### 🌐 Browser Operations (MCP Browser Extension)

#### ✅ `mcp_cursor-browser-extension_browser_navigate` - Điều hướng
- **Syntax:** `mcp_cursor-browser-extension_browser_navigate(url)`
- **Dùng khi:** Cần mở trang web

#### ✅ `mcp_cursor-browser-extension_browser_snapshot` - Chụp snapshot
- **Syntax:** `mcp_cursor-browser-extension_browser_snapshot()`
- **Dùng khi:** Cần xem nội dung trang

#### ✅ `mcp_cursor-browser-extension_browser_click` - Click element
- **Syntax:** `mcp_cursor-browser-extension_browser_click(element, ref)`
- **Dùng khi:** Cần click vào element

#### ✅ Và nhiều browser tools khác...
- `browser_type` - Gõ text
- `browser_wait_for` - Đợi element
- `browser_take_screenshot` - Chụp ảnh
- etc.

---

### 🐙 GitHub Operations (MCP GitHub)

#### ✅ `mcp_github_get_file_contents` - Đọc file từ GitHub
- **Syntax:** `mcp_github_get_file_contents(owner, repo, path, branch)`
- **Dùng khi:** Cần đọc file từ GitHub repo
- **Ví dụ:** `mcp_github_get_file_contents("mrkent19999x", "cursor-agent-final", "README.md", "main")`

#### ✅ `mcp_github_create_or_update_file` - Tạo/cập nhật file
- **Syntax:** `mcp_github_create_or_update_file(owner, repo, path, content, message, branch, sha)`
- **Dùng khi:** Cần push file lên GitHub

#### ✅ Và nhiều GitHub tools khác...
- `mcp_github_search_repositories`
- `mcp_github_create_issue`
- `mcp_github_create_pull_request`
- etc.

---

## ❌ TOOLS KHÔNG TỒN TẠI - TUYỆT ĐỐI KHÔNG DÙNG

### ❌ `read_file` - KHÔNG TỒN TẠI
- **SAI:** `read_file("/path/to/file")`
- **ĐÚNG:** `run_terminal_cmd("cat /path/to/file", false, false)`
- **HOẶC:** Dùng `mcp_github_get_file_contents` nếu file trên GitHub

### ❌ `write_file` - KHÔNG TỒN TẠI
- **SAI:** `write_file("/path/to/file", content)`
- **ĐÚNG:** `edit_file("/path/to/file", "Create file", content)`

### ❌ `list_files` - KHÔNG TỒN TẠI
- **SAI:** `list_files("/path/to/dir")`
- **ĐÚNG:** `run_terminal_cmd("ls -la /path/to/dir", false, false)`

---

## 🔄 WORKFLOW ĐỌC FILE ĐÚNG

### Bước 1: Kiểm tra tools available
- Luôn check tools available trước khi dùng
- Nếu không chắc → dùng `run_terminal_cmd` với `cat`

### Bước 2: Đọc file local
```bash
run_terminal_cmd("cat /path/to/file", false, false)
```

### Bước 3: Đọc file GitHub
```
mcp_github_get_file_contents(owner, repo, path, branch)
```

### Bước 4: Tìm file
```
file_search("filename")
```

---

## 📋 CHECKLIST TRƯỚC KHI DÙNG TOOL

- [ ] Tool có trong danh sách AVAILABLE không?
- [ ] Đã đọc syntax đúng chưa?
- [ ] Có cách nào đơn giản hơn không?
- [ ] Nếu không chắc → dùng `run_terminal_cmd` với shell command

---

## 🔄 AUTO-UPDATE MECHANISM

File này được tự động cập nhật khi:
1. Cursor release tools mới
2. Agent phát hiện tool không tồn tại
3. Mỗi khi search về Cursor tools → update file này

**Agent PHẢI:** Đọc file này trước khi dùng bất kỳ tool nào mới.

---

## 📚 Nguồn tham khảo

- Cursor Tools Documentation: https://docs.cursor.com
- MCP Tools: Check trong MCP registry
- Nếu có tool mới → Update file này ngay lập tức

---

**Ghi nhớ:** Khi không chắc tool nào tồn tại → Dùng `run_terminal_cmd` với shell command. An toàn 100%!
