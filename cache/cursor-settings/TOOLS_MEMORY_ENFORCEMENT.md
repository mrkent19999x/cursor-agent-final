# 🔒 TOOLS MEMORY ENFORCEMENT - KHÔNG BAO GIỜ QUÊN

## 🎯 MỤC ĐÍCH

Đảm bảo agent Cursor **KHÔNG BAO GIỜ**:
- Dùng tools không tồn tại
- Quên tools available
- Lặp lại lỗi "tool not found"

---

## 🔄 AUTO-UPDATE MECHANISM

### Khi phát hiện lỗi "tool not found":

1. **NGAY LẬP TỨC:**
   - Update `AVAILABLE_TOOLS_REFERENCE.md`
   - Ghi rõ tool nào SAI, tool nào ĐÚNG
   - Commit & push vào GitHub

2. **TRONG SESSION:**
   - Ghi nhớ tool sai → không dùng lại
   - Dùng tool đúng ngay lập tức

3. **PERSISTENT MEMORY:**
   - Lưu vào `TOOLS_MEMORY_ENFORCEMENT.md` (file này)
   - Mỗi khi start → đọc file này trước
   - Update liên tục khi có tool mới

---

## 📋 PRE-FLIGHT CHECKLIST

**TRƯỚC MỖI TASK:**

- [ ] Đã đọc `AVAILABLE_TOOLS_REFERENCE.md`?
- [ ] Đã check tools available trong system message?
- [ ] Tool định dùng có trong reference không?
- [ ] Nếu không chắc → dùng `run_terminal_cmd` với shell command

---

## 🚨 RED FLAGS - DỪNG NGAY NẾU THẤY

### Tool names phổ biến KHÔNG TỒN TẠI:
- ❌ `read_file` → Dùng `run_terminal_cmd("cat file")`
- ❌ `write_file` → Dùng `edit_file`
- ❌ `list_files` → Dùng `run_terminal_cmd("ls")`
- ❌ `read_directory` → Dùng `run_terminal_cmd("ls -la")`
- ❌ `copy_file` → Dùng `run_terminal_cmd("cp")`
- ❌ `move_file` → Dùng `run_terminal_cmd("mv")`

### Safe fallback:
**Khi không chắc → LUÔN dùng `run_terminal_cmd` với shell command**

---

## 🔄 UPDATE WORKFLOW

### Mỗi khi có tool mới từ Cursor:
1. Test tool có hoạt động không
2. Thêm vào `AVAILABLE_TOOLS_REFERENCE.md`
3. Commit & push
4. Update checklist trong Custom Mode Instructions

### Mỗi khi phát hiện tool sai:
1. Ghi vào `TOOLS_MEMORY_ENFORCEMENT.md` (file này)
2. Update `AVAILABLE_TOOLS_REFERENCE.md` với warning
3. Commit & push
4. Không bao giờ lặp lại lỗi đó

---

## 💾 PERSISTENT STORAGE

File này được lưu trong:
- Local: `~/cursor-agent-final/cache/cursor-settings/`
- GitHub: `https://github.com/mrkent19999x/cursor-agent-final/cache/cursor-settings/`
- MCP: Accessible qua `@cursor-agent-repo`

**Agent PHẢI đọc file này mỗi khi start session!**

---

## 📅 LOG LỖI TOOLS

### 2025-11-05:
- ❌ `read_file` - Agent dùng nhưng không tồn tại
- ✅ Fix: Dùng `run_terminal_cmd("cat file")` thay thế
- ✅ Action: Đã update AVAILABLE_TOOLS_REFERENCE.md

---

## 🎯 SUCCESS METRICS

- **0 lỗi "tool not found"** trong session
- **100% tools validation** trước khi dùng
- **Auto-update** khi có tool mới
- **Persistent memory** qua GitHub repo

---

**Ghi nhớ:** Khi không chắc → Dùng `run_terminal_cmd`. An toàn 100%!
