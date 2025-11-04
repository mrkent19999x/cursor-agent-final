# `/research` - Research và Cache Thông Tin

## Mô tả
Research topic từ nhiều nguồn và cache vào repo để dùng lại sau.

## Usage
```
/research <topic>
```

## Parameters
- `topic` (required): Chủ đề cần research (ví dụ: "custom modes", "slash commands", "MCP servers")

## Workflow
1. **Search từ 3-5 sources:**
   - docs.cursor.com (official docs)
   - forum.cursor.com (community)
   - github.com/getcursor/cursor (code & issues)
   - Other trusted sources

2. **Verify:**
   - Check official docs
   - Cross-reference thông tin
   - Verify dates (ưu tiên 2025)

3. **Cache:**
   - Tạo file: `cache/cursor-settings/[topic].md`
   - Format theo template
   - Include sources và links

4. **Push:**
   - Commit và push lên GitHub
   - Báo kết quả

## Output Format
```
🔍 NGHIÊN CỨU: [Topic]

📊 NGUỒN:
1. docs.cursor.com - [Link]
2. forum.cursor.com - [Link]
3. github.com/getcursor/cursor - [Link]

✅ FINDINGS:
- [Finding 1]
- [Finding 2]
- [Finding 3]

💾 CACHE:
- File: cache/cursor-settings/[topic].md
- Status: ✅ Đã push lên GitHub

💡 KẾT LUẬN:
[Tóm tắt findings và recommendations]
```

## Examples
```
/research custom modes
/research slash commands
/research MCP servers integration
/research cursor settings configuration
```

## Notes
- **Multiple sources** - Luôn search 3-5 sources
- **Verify official** - Verify từ official docs
- **Cache everything** - Cache tất cả research
- **Push to GitHub** - Luôn push lên repo
- **Latest info** - Ưu tiên thông tin 2025

## Script Used
- `scripts/save-cursor-cache.sh <topic> <source> [content_file] [url]`

