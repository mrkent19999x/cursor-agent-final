#!/bin/bash
# Cursor IDE Configuration Setup Script

echo "⚙️ Cursor IDE Configuration Setup"
echo "================================="
echo ""

# Check if Cursor is installed
if ! command -v cursor &> /dev/null; then
    echo "❌ Cursor IDE not found in PATH"
    echo "Please install Cursor IDE first:"
    echo "📥 Download from: https://cursor.sh/"
    echo ""
    echo "After installation, add Cursor to your PATH or run this script again."
    exit 1
fi

echo "✅ Cursor IDE found: $(cursor --version 2>/dev/null || echo 'Installed')"
echo ""

# Create Cursor config directory
CURSOR_CONFIG_DIR="$HOME/.cursor"
echo "📁 Creating Cursor config directory: $CURSOR_CONFIG_DIR"
mkdir -p "$CURSOR_CONFIG_DIR"

# Copy configuration files
echo "📋 Copying configuration files..."
echo ""

# Copy cursor settings
if [ -f "/workspace/configs/cursor-settings.json" ]; then
    cp "/workspace/configs/cursor-settings.json" "$CURSOR_CONFIG_DIR/settings.json"
    echo "✅ Copied cursor-settings.json to $CURSOR_CONFIG_DIR/settings.json"
else
    echo "❌ cursor-settings.json not found!"
    exit 1
fi

# Copy environment variables
if [ -f "/workspace/configs/environment.env" ]; then
    cp "/workspace/configs/environment.env" "$CURSOR_CONFIG_DIR/.env"
    echo "✅ Copied environment.env to $CURSOR_CONFIG_DIR/.env"
else
    echo "❌ environment.env not found!"
    exit 1
fi

# Copy ultimate assistant config
if [ -f "/workspace/configs/ultimate-assistant.json" ]; then
    cp "/workspace/configs/ultimate-assistant.json" "$CURSOR_CONFIG_DIR/ultimate-assistant.json"
    echo "✅ Copied ultimate-assistant.json to $CURSOR_CONFIG_DIR/ultimate-assistant.json"
else
    echo "⚠️ ultimate-assistant.json not found (optional)"
fi

# Create MCP servers directory
MCP_DIR="$CURSOR_CONFIG_DIR/mcp"
echo "📁 Creating MCP servers directory: $MCP_DIR"
mkdir -p "$MCP_DIR"

# Copy MCP configuration
if [ -f "/workspace/configs/cursor-settings.json" ]; then
    # Extract MCP servers configuration
    jq '.mcp.servers' "/workspace/configs/cursor-settings.json" > "$MCP_DIR/servers.json" 2>/dev/null || {
        echo "⚠️ Could not extract MCP servers config (jq not available)"
        echo "📝 You can manually copy the mcp.servers section from cursor-settings.json"
    }
    echo "✅ Created MCP servers configuration"
fi

echo ""
echo "🔧 Setting up environment variables..."
echo "===================================="

# Load environment variables
if [ -f "$CURSOR_CONFIG_DIR/.env" ]; then
    # Source the environment file
    set -a
    source "$CURSOR_CONFIG_DIR/.env"
    set +a
    echo "✅ Environment variables loaded"
    
    # Show some key variables (without revealing values)
    echo "📋 Key environment variables:"
    echo "  - GITHUB_TOKEN: ${GITHUB_TOKEN:+[SET]}"
    echo "  - NOTION_API_KEY: ${NOTION_API_KEY:+[SET]}"
    echo "  - SUPABASE_URL: ${SUPABASE_URL:+[SET]}"
    echo "  - TAVILY_API_KEY: ${TAVILY_API_KEY:+[SET]}"
    echo "  - SENTRY_AUTH_TOKEN: ${SENTRY_AUTH_TOKEN:+[SET]}"
else
    echo "❌ Environment file not found!"
fi

echo ""
echo "📝 Creating startup script..."
echo "============================"

# Create a startup script for Cursor
STARTUP_SCRIPT="$CURSOR_CONFIG_DIR/start-cursor.sh"
cat > "$STARTUP_SCRIPT" << 'EOF'
#!/bin/bash
# Cursor IDE Startup Script with MCP Configuration

echo "🚀 Starting Cursor IDE with MCP Configuration..."

# Load environment variables
if [ -f "$HOME/.cursor/.env" ]; then
    set -a
    source "$HOME/.cursor/.env"
    set +a
    echo "✅ Environment variables loaded"
fi

# Start Cursor IDE
cursor "$@"
EOF

chmod +x "$STARTUP_SCRIPT"
echo "✅ Created startup script: $STARTUP_SCRIPT"

echo ""
echo "🧪 Testing MCP Configuration..."
echo "==============================="

# Test MCP servers
if [ -f "/workspace/test-mcp-config.js" ]; then
    echo "Running MCP configuration test..."
    node /workspace/test-mcp-config.js
else
    echo "⚠️ MCP test script not found"
fi

echo ""
echo "📋 Configuration Summary:"
echo "========================="
echo "✅ Cursor config directory: $CURSOR_CONFIG_DIR"
echo "✅ Settings file: $CURSOR_CONFIG_DIR/settings.json"
echo "✅ Environment file: $CURSOR_CONFIG_DIR/.env"
echo "✅ MCP servers config: $MCP_DIR/servers.json"
echo "✅ Startup script: $STARTUP_SCRIPT"
echo ""

echo "🎯 Next Steps:"
echo "============="
echo "1. Restart Cursor IDE completely"
echo "2. Open Cursor IDE"
echo "3. Check MCP servers in Cursor settings"
echo "4. Test MCP functionality"
echo ""

echo "🔧 Manual Steps (if needed):"
echo "============================"
echo "1. Open Cursor IDE"
echo "2. Go to Settings (Cmd/Ctrl + ,)"
echo "3. Search for 'MCP'"
echo "4. Verify MCP servers are loaded"
echo "5. Test with a simple MCP command"
echo ""

echo "🚀 Cursor IDE Configuration Complete!"
echo "===================================="
echo ""
echo "💡 Tips:"
echo "- Use the startup script: $STARTUP_SCRIPT"
echo "- Check logs in Cursor for MCP errors"
echo "- Test each MCP server individually"
echo "- Update API keys as needed"
echo ""
echo "🎉 Ready to use Cursor Agent Learning Hub!"