#!/bin/bash
# Script tự động cập nhật Cursor AI Library
# Tác giả: Cursor Assistant cho anh Nghĩa
# Ngày: 25/10/2025

echo "🚀 CURSOR AI LIBRARY - CẬP NHẬT TỰ ĐỘNG"
echo "========================================"
echo ""

# Kiểm tra Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 không được cài đặt!"
    exit 1
fi

# Tạo backup
echo "💾 Tạo backup dữ liệu cũ..."
if [ -d "cursor_ai_library_organized" ]; then
    cp -r cursor_ai_library_organized cursor_ai_library_backup_$(date +%Y%m%d_%H%M%S)
    echo "✅ Đã tạo backup"
else
    echo "⚠️  Không tìm thấy thư viện cũ để backup"
fi

# Cào web mới
echo ""
echo "🕷️  Bắt đầu cào web cursor.com..."
python3 cursor_web_scraper.py

if [ $? -eq 0 ]; then
    echo "✅ Cào web thành công!"
else
    echo "❌ Lỗi khi cào web!"
    exit 1
fi

# Tổ chức thư viện
echo ""
echo "📚 Tổ chức thư viện mới..."
python3 cursor_ai_library_organizer.py

if [ $? -eq 0 ]; then
    echo "✅ Tổ chức thư viện thành công!"
else
    echo "❌ Lỗi khi tổ chức thư viện!"
    exit 1
fi

# Tạo báo cáo
echo ""
echo "📊 Tạo báo cáo cuối cùng..."
python3 create_final_report.py

if [ $? -eq 0 ]; then
    echo "✅ Tạo báo cáo thành công!"
else
    echo "❌ Lỗi khi tạo báo cáo!"
fi

# Hiển thị kết quả
echo ""
echo "🎉 HOÀN THÀNH CẬP NHẬT!"
echo "======================="
echo "📁 Thư viện mới: cursor_ai_library_organized/"
echo "📄 Báo cáo: FINAL_CURSOR_AI_LIBRARY_REPORT.md"
echo "🔍 Tìm kiếm: python3 cursor_ai_search.py"
echo ""
echo "📊 Thống kê:"
echo "- Ngày cập nhật: $(date)"
echo "- Thư mục backup: cursor_ai_library_backup_*"
echo "- Dữ liệu mới: cursor_ai_library_organized/"
echo ""
echo "✨ Anh có thể sử dụng thư viện ngay bây giờ!"