#!/bin/bash

# Script validation tools để đảm bảo agent không dùng tools sai
# Usage: ./validate-tools.sh [tool_name]

TOOLS_REFERENCE="$HOME/cursor-agent-final/cache/cursor-settings/AVAILABLE_TOOLS_REFERENCE.md"

if [ ! -f "$TOOLS_REFERENCE" ]; then
    echo "⚠️ AVAILABLE_TOOLS_REFERENCE.md chưa tồn tại"
    exit 1
fi

TOOL_NAME="$1"

if [ -z "$TOOL_NAME" ]; then
    echo "📋 Danh sách tools available:"
    grep -E "^#### ✅|^#### ❌" "$TOOLS_REFERENCE" | sed 's/#### //' | sed 's/`//g'
    exit 0
fi

# Check tool
if grep -q "#### ✅.*\`$TOOL_NAME\`" "$TOOLS_REFERENCE"; then
    echo "✅ Tool '$TOOL_NAME' CÓ TỒN TẠI"
    grep -A 5 "#### ✅.*\`$TOOL_NAME\`" "$TOOLS_REFERENCE"
    exit 0
elif grep -q "#### ❌.*\`$TOOL_NAME\`" "$TOOLS_REFERENCE"; then
    echo "❌ Tool '$TOOL_NAME' KHÔNG TỒN TẠI"
    echo ""
    echo "Cách thay thế:"
    grep -A 10 "#### ❌.*\`$TOOL_NAME\`" "$TOOLS_REFERENCE"
    exit 1
else
    echo "⚠️ Tool '$TOOL_NAME' chưa có trong reference"
    echo "Cần check tools available trong system message hoặc update reference"
    exit 2
fi
