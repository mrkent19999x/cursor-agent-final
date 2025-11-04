# `/analyze` - Phân tích Codebase và Tạo Báo Cáo

## Mô tả
Phân tích codebase và tạo báo cáo Executive Summary cho Product Owner (không biết code).

## Usage
```
/analyze [path]
```

## Parameters
- `path` (optional): Path đến codebase cần phân tích. Default: current directory

## Workflow
1. **Scan codebase:**
   - Đọc structure
   - Đọc README, docs
   - Check git commits, issues
   - Xem monitoring reports (nếu có)

2. **Phân tích:**
   - Tiến độ (completion rate)
   - Risks (technical, business)
   - Opportunities (optimization, features)

3. **Tạo báo cáo:**
   - Executive Summary
   - Risk assessment
   - Recommendations
   - Metrics

## Output Format
```
📊 BÁO CÁO PHÂN TÍCH: [Project Name]

## 📊 Tóm tắt Điều hành
- **Mục tiêu**: [Mục tiêu chính]
- **KPI**: [Key metrics]
- **Timeline**: [Thời gian]

## ✅ Thành tựu
- [Achievement 1]
- [Achievement 2]

## ⚠️ Thách thức
- [Challenge 1]
- [Challenge 2]

## 💡 Cơ hội
- [Opportunity 1]
- [Opportunity 2]

## 📋 Khuyến nghị
- [Recommendation 1]
- [Recommendation 2]

## 📈 Metrics
- **Tiến độ**: X%
- **Budget**: X%
- **Quality**: X/10
```

## Examples
```
/analyze
/analyze ./src
/analyze ../my-project
```

## Notes
- **KHÔNG dùng thuật ngữ kỹ thuật** - Giải thích đơn giản
- **Focus vào business impact** - Không focus vào code details
- **Dùng templates** - Từ `examples/management-templates/`
- **Tiếng Việt** - Tất cả output bằng tiếng Việt

