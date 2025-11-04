# `/report` - Tạo Báo Cáo Quản Lý

## Mô tả
Tạo báo cáo quản lý theo format chuẩn cho Product Owner.

## Usage
```
/report <type> [project]
```

## Parameters
- `type` (required): Loại báo cáo:
  - `progress` - Báo cáo tiến độ
  - `performance` - Báo cáo hiệu suất
  - `risks` - Phân tích risks
  - `summary` - Executive summary
- `project` (optional): Tên project. Default: current project

## Workflow
1. **Thu thập dữ liệu:**
   - Scan codebase
   - Đọc README, docs
   - Check git commits, issues
   - Xem monitoring reports

2. **Phân tích:**
   - Phân tích theo type
   - Tính toán metrics
   - Identify risks/opportunities

3. **Tạo báo cáo:**
   - Dùng template từ `examples/management-templates/`
   - Format theo chuẩn
   - Export PDF/Markdown

## Output Format

### Progress Report:
```
📊 BÁO CÁO TIẾN ĐỘ: [Project Name]

✅ Hoàn thành: X%
⏳ Đang làm: Y%
📋 Còn lại: Z%

📈 METRICS:
- Tiến độ: X%
- Budget: X% đã dùng
- Quality: X/10

⚠️ RISKS:
- [Risk 1]: [Mitigation]
- [Risk 2]: [Mitigation]

💡 RECOMMENDATIONS:
- [Recommendation 1]
- [Recommendation 2]
```

### Risks Report:
```
⚠️ PHÂN TÍCH RISKS: [Project Name]

🔴 CAO:
- [Risk 1]: [Impact] - [Mitigation]

🟡 TRUNG BÌNH:
- [Risk 2]: [Impact] - [Mitigation]

🟢 THẤP:
- [Risk 3]: [Impact] - [Mitigation]

💡 KHUYẾN NGHỊ:
- [Action 1]
- [Action 2]
```

## Examples
```
/report progress my-web-app
/report performance api-service
/report risks automation-tool
/report summary
```

## Notes
- **Dùng templates:** Từ `examples/management-templates/`
- **KHÔNG dùng thuật ngữ kỹ thuật:** Giải thích đơn giản
- **Focus vào business impact:** Không focus vào code details
- **Tiếng Việt:** Tất cả output bằng tiếng Việt
- **Export options:** Markdown hoặc PDF

## Templates Used
- `examples/management-templates/executive-summary-template.md`
- `examples/management-templates/project-report-template.md`

