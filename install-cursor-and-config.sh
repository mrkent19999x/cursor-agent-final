#!/bin/bash
# Cursor IDE Installation and Configuration Script

echo "🚀 Cursor IDE Installation and Configuration"
echo "============================================="
echo ""

# Detect OS
OS=$(uname -s)
ARCH=$(uname -m)

echo "🖥️ Detected OS: $OS $ARCH"
echo ""

# Function to install Cursor IDE
install_cursor() {
    echo "📥 Installing Cursor IDE..."
    
    case $OS in
        "Linux")
            echo "Installing Cursor IDE for Linux..."
            
            # Download Cursor IDE
            CURSOR_VERSION="0.42.3"
            CURSOR_URL="https://downloader.cursor.sh/linux/appImage/x64"
            CURSOR_FILE="cursor.AppImage"
            
            echo "Downloading Cursor IDE..."
            wget -O "$CURSOR_FILE" "$CURSOR_URL" || {
                echo "❌ Failed to download Cursor IDE"
                echo "Please download manually from: https://cursor.sh/"
                return 1
            }
            
            # Make it executable
            chmod +x "$CURSOR_FILE"
            
            # Create symlink
            sudo mv "$CURSOR_FILE" /usr/local/bin/cursor || {
                echo "⚠️ Could not move to /usr/local/bin, trying ~/.local/bin"
                mkdir -p ~/.local/bin
                mv "$CURSOR_FILE" ~/.local/bin/cursor
                echo "✅ Cursor IDE installed to ~/.local/bin/cursor"
                echo "Add ~/.local/bin to your PATH: export PATH=\$PATH:~/.local/bin"
            }
            
            echo "✅ Cursor IDE installed successfully"
            ;;
        "Darwin")
            echo "Installing Cursor IDE for macOS..."
            
            # Download Cursor IDE for macOS
            CURSOR_URL="https://downloader.cursor.sh/mac/universal"
            CURSOR_FILE="cursor.dmg"
            
            echo "Downloading Cursor IDE..."
            curl -L -o "$CURSOR_FILE" "$CURSOR_URL" || {
                echo "❌ Failed to download Cursor IDE"
                echo "Please download manually from: https://cursor.sh/"
                return 1
            }
            
            echo "✅ Cursor IDE downloaded. Please install manually:"
            echo "1. Open $CURSOR_FILE"
            echo "2. Drag Cursor to Applications folder"
            echo "3. Run this script again"
            ;;
        *)
            echo "❌ Unsupported OS: $OS"
            echo "Please install Cursor IDE manually from: https://cursor.sh/"
            return 1
            ;;
    esac
}

# Check if Cursor is already installed
if command -v cursor &> /dev/null; then
    echo "✅ Cursor IDE already installed: $(cursor --version 2>/dev/null || echo 'Installed')"
else
    echo "❌ Cursor IDE not found. Installing..."
    install_cursor
fi

echo ""
echo "⚙️ Setting up Cursor Configuration..."
echo "====================================="

# Create Cursor config directory
CURSOR_CONFIG_DIR="$HOME/.cursor"
echo "📁 Creating Cursor config directory: $CURSOR_CONFIG_DIR"
mkdir -p "$CURSOR_CONFIG_DIR"

# Copy configuration files
echo "📋 Copying configuration files..."

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

echo ""
echo "🔧 Setting up environment variables..."

# Load environment variables
if [ -f "$CURSOR_CONFIG_DIR/.env" ]; then
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
echo "✅ Startup script: $STARTUP_SCRIPT"
echo ""

echo "🎯 Next Steps:"
echo "============="
echo "1. Start Cursor IDE:"
echo "   - Linux: cursor"
echo "   - macOS: Open Cursor from Applications"
echo "   - Or use: $STARTUP_SCRIPT"
echo ""
echo "2. Verify MCP servers in Cursor:"
echo "   - Open Settings (Cmd/Ctrl + ,)"
echo "   - Search for 'MCP'"
echo "   - Check if MCP servers are loaded"
echo ""
echo "3. Test MCP functionality:"
echo "   - Try using MCP commands"
echo "   - Check Cursor logs for errors"
echo ""

echo "🔧 Manual Configuration (if needed):"
echo "====================================="
echo "1. Open Cursor IDE"
echo "2. Go to Settings (Cmd/Ctrl + ,)"
echo "3. Search for 'MCP'"
echo "4. Verify MCP servers configuration"
echo "5. Test with a simple MCP command"
echo ""

echo "🚀 Cursor IDE Installation and Configuration Complete!"
echo "===================================================="
echo ""
echo "💡 Tips:"
echo "- Use the startup script: $STARTUP_SCRIPT"
echo "- Check logs in Cursor for MCP errors"
echo "- Test each MCP server individually"
echo "- Update API keys as needed"
echo ""
echo "🎉 Ready to use Cursor Agent Learning Hub!"