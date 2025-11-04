#!/bin/bash

# Script để lưu cache Cursor settings vào GitHub repo
# Usage: ./save-cursor-cache.sh [topic] [source] [content_file]

REPO_DIR="$HOME/cursor-agent-final"
CACHE_DIR="$REPO_DIR/cache"
DATE=$(date +"%Y-%m-%d %H:%M:%S")

TOPIC="$1"
SOURCE="$2"  # docs, forum, github
CONTENT_FILE="$3"
URL="$4"     # Optional: URL của nguồn

if [ -z "$TOPIC" ] || [ -z "$SOURCE" ]; then
    echo "Usage: $0 <topic> <source> [content_file] [url]"
    echo "Example: $0 'custom-modes' 'docs' content.txt 'https://docs.cursor.com/agent/modes'"
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
if [ -n "$URL" ]; then
    case "$SOURCE" in
        docs)
            echo "- Docs: [$URL]($URL)" >> "$FILEPATH"
            ;;
        forum)
            echo "- Forum: [$URL]($URL)" >> "$FILEPATH"
            ;;
        github)
            echo "- GitHub: [$URL]($URL)" >> "$FILEPATH"
            ;;
    esac
else
    echo "- Nguồn: [URL sẽ được thêm]" >> "$FILEPATH"
fi

# Commit và push
cd "$REPO_DIR" || exit 1
git add "$FILEPATH" 2>/dev/null
git commit -m "Cache: Update $TOPIC from $SOURCE - $DATE" 2>/dev/null

# Push với error handling
if git push origin main 2>/dev/null; then
    echo "✅ Đã lưu cache và push: $FILEPATH"
else
    echo "⚠️ Đã lưu cache nhưng push thất bại. Check git credentials."
    echo "📁 File đã được lưu tại: $FILEPATH"
fi
