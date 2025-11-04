# 🗄️ Cursor Settings Cache - Repository

## 📋 Mục đích
Lưu trữ lâu dài tất cả thông tin về Cursor settings, configs từ 3 nguồn chính thức:
1. **docs.cursor.com** - Tài liệu chính thức
2. **forum.cursor.com** - Kinh nghiệm từ cộng đồng
3. **github.com/getcursor/cursor** - Code & Issues

## 📁 Cấu trúc

```
cache/
├── cursor-settings/          # Cache về settings/config
│   ├── custom-modes.md       # Custom Modes documentation
│   ├── mcp-servers.md        # MCP Servers config
│   ├── commands.md           # Commands documentation
│   └── ...                   # Các settings khác
└── research-3-sources/       # Research từ 3 nguồn
    ├── docs/                 # Từ docs.cursor.com
    ├── forum/                # Từ forum.cursor.com
    └── github/               # Từ github.com/getcursor
```

## 🔄 Auto-Sync
Cache tự động được lưu khi:
- Anh hỏi về Cursor settings
- Tìm thấy thông tin mới từ 3 nguồn
- Verify lại thông tin cũ (> 7 ngày)

## 📝 Format

Mỗi file cache có format:
```markdown
# [Topic Title]

## 📊 Thông tin
- **Nguồn**: [URL]
- **Ngày kiểm chứng**: [YYYY-MM-DD]
- **Từ nguồn**: [docs/forum/github]

## 📋 Nội dung
[Content từ nguồn]

## 🔗 Links
- Docs: [Link]
- Forum: [Link]
- GitHub: [Link]
```

## 🚀 Sử dụng
Cache này được tự động sử dụng trong Custom Mode khi anh hỏi về Cursor settings.
