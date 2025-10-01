#!/bin/bash

# MCP Configuration Setup Script for Cursor IDE
# Script để cấu hình MCP cho Cursor IDE

echo "🔧 MCP Configuration Setup for Cursor IDE"
echo "=========================================="
echo ""

# Check if Cursor is installed
if ! command -v cursor &> /dev/null; then
    echo "❌ Cursor IDE not found in PATH"
    echo "Please install Cursor IDE first: https://cursor.sh/"
    exit 1
fi

echo "✅ Cursor IDE found"

# Find Cursor config directory
CURSOR_CONFIG_DIR=""

# Try different possible locations
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    CURSOR_CONFIG_DIR="$HOME/Library/Application Support/Cursor/User"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux
    CURSOR_CONFIG_DIR="$HOME/.config/Cursor/User"
elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
    # Windows
    CURSOR_CONFIG_DIR="$APPDATA/Cursor/User"
fi

if [ -z "$CURSOR_CONFIG_DIR" ]; then
    echo "❌ Could not determine Cursor config directory"
    echo "Please manually copy the configuration files"
    exit 1
fi

echo "📁 Cursor config directory: $CURSOR_CONFIG_DIR"

# Create config directory if it doesn't exist
mkdir -p "$CURSOR_CONFIG_DIR"

# Copy settings file
SETTINGS_FILE="$CURSOR_CONFIG_DIR/settings.json"
BACKUP_FILE="$CURSOR_CONFIG_DIR/settings.json.backup.$(date +%Y%m%d_%H%M%S)"

echo ""
echo "📋 Copying MCP configuration..."

# Backup existing settings if they exist
if [ -f "$SETTINGS_FILE" ]; then
    echo "💾 Backing up existing settings to: $BACKUP_FILE"
    cp "$SETTINGS_FILE" "$BACKUP_FILE"
fi

# Copy new settings
cp "/workspace/configs/cursor-settings.json" "$SETTINGS_FILE"
echo "✅ MCP settings copied to: $SETTINGS_FILE"

# Copy environment file
ENV_FILE="$CURSOR_CONFIG_DIR/.env"
cp "/workspace/configs/environment.env" "$ENV_FILE"
echo "✅ Environment variables copied to: $ENV_FILE"

echo ""
echo "🎉 MCP Configuration Complete!"
echo ""
echo "📝 Next Steps:"
echo "1. Update API keys in: $ENV_FILE"
echo "2. Restart Cursor IDE"
echo "3. Test MCP servers in Cursor"
echo ""
echo "🔧 Available MCP Servers:"
echo "- Notion (Documentation)"
echo "- Sentry (Error Monitoring)"
echo "- Supabase (Database)"
echo "- Apify (Web Scraping)"
echo "- Filesystem (File Access)"
echo "- Sequential Thinking (Logic)"
echo "- Heroku (App Management)"
echo "- HubSpot (CRM)"
echo "- Tavily (Web Search)"
echo "- Kubernetes (Container Management)"
echo "- Datadog (Monitoring)"
echo ""
echo "📖 For detailed setup guide, see: /workspace/MCP_SETUP_GUIDE.md"
echo ""
echo "🚀 Ready to use MCP with Cursor IDE!"