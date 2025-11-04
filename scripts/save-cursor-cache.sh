#!/bin/bash

# Script để lưu cache Cursor settings vào GitHub repo
# Usage: ./save-cursor-cache.sh [topic] [source] [content_file]

REPO_DIR="$HOME/cursor-agent-final"
CACHE_DIR="$REPO_DIR/cache"
DATE=$(date +"%Y-%m-%d %H:%M:%S")

TOPIC="$1"
SOURCE="$2"  # docs, forum, github
CONTENT_FILE="$3"

if [ -z "$TOPIC" ] || [ -z "$SOURCE" ]; then
    echo "Usage: $0 <topic> <source> [content_file]"
    echo "Example: $0 'custom-modes' 'docs' content.txt"
    exit 1
fi

# Tạo filename từ topic
FILENAME=$(echo "$TOPIC" | tr ' ' '-' | tr '[:upper:]' '[:lower:]').md
FILEPATH="$CACHE_DIR/cursor-settings/$FILENAME"

# Tạo nội dung cache
echo "# $TOPIC" > "$FILEPATH"
echo "" >> "$FILEPATH"
echo "## 📊 Thông tin" >> "$FILEPATH"
echo "- **Nguồn**: $SOURCE" >> "$FILEPATH"
echo "- **Ngày kiểm chứng**: $DATE" >> "$FILEPATH"
echo "- **Từ nguồn**: $SOURCE" >> "$FILEPATH"
echo "" >> "$FILEPATH"

if [ -n "$CONTENT_FILE" ] && [ -f "$CONTENT_FILE" ]; then
    echo "## 📋 Nội dung" >> "$FILEPATH"
    cat "$CONTENT_FILE" >> "$FILEPATH"
else
    echo "## 📋 Nội dung" >> "$FILEPATH"
    echo "[Content sẽ được cập nhật]" >> "$FILEPATH"
fi

echo "" >> "$FILEPATH"
echo "## 🔗 Links" >> "$FILEPATH"
echo "- Nguồn: [URL sẽ được thêm]" >> "$FILEPATH"

# Commit và push
cd "$REPO_DIR"
git add "$FILEPATH"
git commit -m "Cache: Update $TOPIC from $SOURCE - $DATE" 2>/dev/null
git push origin main 2>/dev/null

echo "✅ Đã lưu cache: $FILEPATH"
