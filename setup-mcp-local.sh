#!/bin/bash
# MCP Local Setup Script for Cursor Agent

echo "🚀 Setting up MCP locally for Cursor Agent..."

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "📝 Creating .env file..."
    cp configs/environment.env .env
    echo "✅ .env file created"
else
    echo "✅ .env file already exists"
fi

# Create Cursor config directory if it doesn't exist
CURSOR_CONFIG_DIR="$HOME/.cursor"
if [ ! -d "$CURSOR_CONFIG_DIR" ]; then
    echo "📁 Creating Cursor config directory..."
    mkdir -p "$CURSOR_CONFIG_DIR"
    echo "✅ Cursor config directory created"
else
    echo "✅ Cursor config directory already exists"
fi

# Copy Cursor settings
echo "⚙️ Copying Cursor settings..."
cp configs/cursor-settings.json "$CURSOR_CONFIG_DIR/settings.json"
echo "✅ Cursor settings copied"

# Check if MCP servers are installed
echo "🔍 Checking MCP servers installation..."

# Check core MCP servers
MCP_SERVERS=(
    "firecrawl-mcp"
    "github-mcp-scoped-server" 
    "concurrent-browser-mcp"
    "@browserbasehq/mcp"
    "slack-mcp-server"
    "qdrant-mcp-server"
    "docker-mcp-server"
    "kubernetes-mcp-server"
    "postgresql-mcp-server"
    "@sentry/mcp-server"
)

for server in "${MCP_SERVERS[@]}"; do
    if npm list -g "$server" &> /dev/null; then
        echo "✅ $server is installed"
    else
        echo "❌ $server is not installed"
    fi
done

echo ""
echo "🎉 MCP setup completed!"
echo ""
echo "📋 Next steps:"
echo "1. Edit .env file with your API keys:"
echo "   - FIRECRAWL_API_KEY (for web scraping)"
echo "   - GITHUB_TOKEN (for GitHub integration)"
echo "   - BROWSERBASE_API_KEY (for browser automation)"
echo "   - SLACK_BOT_TOKEN (for Slack integration)"
echo "   - SENTRY_AUTH_TOKEN (for error monitoring)"
echo ""
echo "2. Restart Cursor IDE"
echo ""
echo "3. Test MCP servers by asking Cursor to:"
echo "   - Browse a website (using browser MCP)"
echo "   - Search GitHub repositories (using GitHub MCP)"
echo "   - Monitor errors (using Sentry MCP)"
echo ""
echo "🔧 Available MCP Servers:"
echo "- Firecrawl (Web scraping)"
echo "- GitHub (Repository management)"
echo "- Browser (Browser automation)"
echo "- Browserbase (Cloud browsers)"
echo "- Slack (Communication)"
echo "- Qdrant (Vector search)"
echo "- Docker (Container management)"
echo "- Kubernetes (Orchestration)"
echo "- PostgreSQL (Database)"
echo "- Sentry (Error monitoring)"
echo ""
echo "🚀 Your MCP setup is ready!"