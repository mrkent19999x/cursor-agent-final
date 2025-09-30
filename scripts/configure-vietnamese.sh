#!/bin/bash
# Cursor Agent Learning Hub - Vietnamese Configuration Script

echo "🇻🇳 Configuring Vietnamese language support for Cursor Agent..."

# Create Vietnamese language pack
echo "📝 Creating Vietnamese language pack..."

# Create Vietnamese prompts directory
mkdir -p examples/vietnamese-prompts
echo "✅ Vietnamese prompts directory created"

# Create Vietnamese business prompts
cat > examples/vietnamese-prompts/business-prompts.md << 'EOF'
# Vietnamese Business Prompts

## Management Prompts

### Project Management
- "Phân tích tiến độ dự án {projectName} và tạo báo cáo quản lý với các điểm cần chú ý"
- "Đánh giá rủi ro dự án {projectName} từ góc độ kỹ thuật và quản lý"
- "Tạo kế hoạch triển khai cho dự án {projectName} với timeline và milestones"

### Business Analysis
- "Phân tích hiệu suất kinh doanh của {company} trong quý {quarter}"
- "Đánh giá cạnh tranh thị trường cho sản phẩm {product}"
- "Tạo báo cáo tài chính cho {period} với insights và recommendations"

### Team Management
- "Đánh giá hiệu suất team dựa trên dữ liệu {dataSource}"
- "Tạo kế hoạch đào tạo cho team {teamName}"
- "Phân tích workload và đề xuất phân bổ công việc"

## Technical Prompts

### Architecture Analysis
- "Phân tích kiến trúc hệ thống {systemName} và đề xuất cải thiện"
- "Đánh giá scalability của ứng dụng {appName}"
- "Tạo sơ đồ kiến trúc cho dự án {projectName}"

### Code Review
- "Review code của module {moduleName} và đánh giá chất lượng"
- "Kiểm tra security vulnerabilities trong codebase {projectName}"
- "Đánh giá performance của API {apiName}"

### Documentation
- "Tạo tài liệu kỹ thuật cho API {apiName}"
- "Viết user guide cho ứng dụng {appName}"
- "Tạo technical specification cho feature {featureName}"

## Compliance & Governance

### Compliance Check
- "Kiểm tra tuân thủ tiêu chuẩn {standard} cho dự án {projectName}"
- "Đánh giá compliance với GDPR cho hệ thống {systemName}"
- "Tạo báo cáo audit cho {auditType}"

### Risk Assessment
- "Đánh giá rủi ro bảo mật cho hệ thống {systemName}"
- "Phân tích rủi ro tài chính cho dự án {projectName}"
- "Tạo risk mitigation plan cho {riskType}"

## Cost Management

### Cost Analysis
- "Phân tích chi phí phát triển cho dự án {projectName}"
- "Đánh giá ROI của investment {investmentType}"
- "Tạo budget proposal cho {period}"

### Resource Optimization
- "Tối ưu hóa resource usage cho hệ thống {systemName}"
- "Phân tích cost-benefit của solution {solutionName}"
- "Đề xuất cost reduction strategies"
EOF

echo "✅ Vietnamese business prompts created"

# Create Vietnamese technical prompts
cat > examples/vietnamese-prompts/technical-prompts.md << 'EOF'
# Vietnamese Technical Prompts

## Development Prompts

### Web Development
- "Tạo trang web {pageType} với tiêu đề '{title}', màu sắc {color}, layout {layout}"
- "Implement responsive design cho component {componentName}"
- "Tối ưu hóa performance cho trang {pageName}"

### API Development
- "Tạo REST API cho {resourceName} với CRUD operations"
- "Implement authentication cho API {apiName}"
- "Tạo API documentation cho endpoint {endpointName}"

### Database Design
- "Thiết kế database schema cho ứng dụng {appName}"
- "Tạo migration scripts cho table {tableName}"
- "Optimize database performance cho query {queryType}"

## DevOps Prompts

### Deployment
- "Tạo deployment pipeline cho ứng dụng {appName}"
- "Setup CI/CD cho project {projectName}"
- "Configure monitoring cho service {serviceName}"

### Infrastructure
- "Thiết kế infrastructure cho hệ thống {systemName}"
- "Setup load balancing cho {serviceName}"
- "Configure backup strategy cho {dataType}"

## Testing Prompts

### Unit Testing
- "Tạo unit tests cho function {functionName}"
- "Implement test coverage cho module {moduleName}"
- "Tạo mock objects cho service {serviceName}"

### Integration Testing
- "Tạo integration tests cho API {apiName}"
- "Test database integration cho {featureName}"
- "Tạo end-to-end tests cho workflow {workflowName}"

## Security Prompts

### Security Analysis
- "Phân tích security vulnerabilities trong code {codeType}"
- "Implement security best practices cho {componentName}"
- "Tạo security audit report cho {systemName}"

### Authentication & Authorization
- "Implement JWT authentication cho {appName}"
- "Setup role-based access control cho {systemName}"
- "Configure OAuth2 cho service {serviceName}"
EOF

echo "✅ Vietnamese technical prompts created"

# Create Vietnamese management templates
mkdir -p examples/management-templates
cat > examples/management-templates/executive-summary-template.md << 'EOF'
# Executive Summary Template

## Tóm tắt Điều hành

### Mục tiêu
- **Mục tiêu chính**: {mainObjective}
- **KPI quan trọng**: {keyKPIs}
- **Timeline**: {timeline}

### Kết quả chính
- **Thành tựu**: {achievements}
- **Thách thức**: {challenges}
- **Cơ hội**: {opportunities}

### Khuyến nghị
- **Action Items**: {actionItems}
- **Next Steps**: {nextSteps}
- **Resource Requirements**: {resourceRequirements}

### Metrics
- **Performance**: {performanceMetrics}
- **Cost**: {costMetrics}
- **Quality**: {qualityMetrics}
EOF

echo "✅ Executive summary template created"

# Create Vietnamese report templates
cat > examples/management-templates/project-report-template.md << 'EOF'
# Project Report Template

## Báo cáo Dự án: {projectName}

### Thông tin Dự án
- **Tên dự án**: {projectName}
- **Ngày bắt đầu**: {startDate}
- **Ngày kết thúc dự kiến**: {endDate}
- **Ngân sách**: {budget}
- **Team size**: {teamSize}

### Tiến độ Dự án
- **Completion Rate**: {completionRate}%
- **Milestones đã hoàn thành**: {completedMilestones}
- **Milestones sắp tới**: {upcomingMilestones}
- **Risks**: {risks}

### Performance Metrics
- **Quality Score**: {qualityScore}/10
- **Budget Utilization**: {budgetUtilization}%
- **Timeline Adherence**: {timelineAdherence}%
- **Team Satisfaction**: {teamSatisfaction}/10

### Issues & Risks
- **Critical Issues**: {criticalIssues}
- **Medium Issues**: {mediumIssues}
- **Low Issues**: {lowIssues}
- **Risk Mitigation**: {riskMitigation}

### Recommendations
- **Immediate Actions**: {immediateActions}
- **Long-term Strategies**: {longTermStrategies}
- **Resource Adjustments**: {resourceAdjustments}
EOF

echo "✅ Project report template created"

# Create Vietnamese configuration
cat > configs/vietnamese-config.json << 'EOF'
{
  "vietnamese": {
    "language": {
      "formal": "Kính chào anh/chị",
      "informal": "Chào bạn",
      "business": "Kinh doanh",
      "technical": "Kỹ thuật",
      "management": "Quản lý"
    },
    "context": {
      "business": {
        "revenue": "Doanh thu",
        "profit": "Lợi nhuận",
        "customer": "Khách hàng",
        "marketing": "Marketing",
        "strategy": "Chiến lược",
        "management": "Quản lý",
        "compliance": "Tuân thủ",
        "governance": "Quản trị",
        "performance": "Hiệu suất",
        "optimization": "Tối ưu hóa"
      },
      "technology": {
        "architecture": "Kiến trúc",
        "deployment": "Triển khai",
        "monitoring": "Giám sát",
        "automation": "Tự động hóa",
        "integration": "Tích hợp",
        "optimization": "Tối ưu hóa",
        "scalability": "Khả năng mở rộng",
        "security": "Bảo mật",
        "performance": "Hiệu suất",
        "reliability": "Độ tin cậy"
      }
    },
    "formatting": {
      "date": "dd/MM/yyyy",
      "time": "HH:mm",
      "currency": "VND",
      "number": "1.000.000",
      "percentage": "95%"
    },
    "prompts": {
      "management": {
        "architectureAnalysis": "Phân tích kiến trúc dự án {projectName}, đánh giá tính phức tạp, rủi ro và đề xuất cải thiện cho quản lý.",
        "complianceCheck": "Kiểm tra tuân thủ tiêu chuẩn {standard} cho dự án {projectName}, tạo báo cáo quản lý với các điểm cần chú ý.",
        "costAnalysis": "Phân tích chi phí và usage của Agent cho dự án {projectName}, đề xuất tối ưu hóa ngân sách.",
        "teamPerformance": "Đánh giá hiệu suất team dựa trên dữ liệu {dataSource}, tạo báo cáo quản lý với insights và recommendations.",
        "riskAssessment": "Đánh giá rủi ro dự án {projectName} từ góc độ kỹ thuật và quản lý, đề xuất mitigation strategies."
      },
      "technical": {
        "webDevelopment": "Tạo trang web {pageType} với tiêu đề '{title}', màu sắc {color}, layout {layout}. Sử dụng {framework} và đảm bảo responsive.",
        "apiDevelopment": "Tạo REST API cho {resourceName} với method {method}, parameters {params}, response format {format}.",
        "databaseDesign": "Thiết kế database cho ứng dụng {appName}, bao gồm các bảng {tables}, quan hệ {relationships}.",
        "testing": "Tạo test cases cho {component} với các scenarios {scenarios}, coverage {coverage}%."
      }
    }
  }
}
EOF

echo "✅ Vietnamese configuration created"

echo ""
echo "🇻🇳 Vietnamese configuration completed!"
echo ""
echo "📋 Created files:"
echo "- examples/vietnamese-prompts/business-prompts.md"
echo "- examples/vietnamese-prompts/technical-prompts.md"
echo "- examples/management-templates/executive-summary-template.md"
echo "- examples/management-templates/project-report-template.md"
echo "- configs/vietnamese-config.json"
echo ""
echo "🎯 Vietnamese language support is ready!"
echo "📚 Use prompts from examples/vietnamese-prompts/ folder"
echo "📊 Use templates from examples/management-templates/ folder"
echo ""
echo "🚀 Cursor Agent is now optimized for Vietnamese management!"