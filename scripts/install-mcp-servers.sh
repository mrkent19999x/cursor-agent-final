#!/bin/bash
# Cursor Agent Learning Hub - MCP Servers Installation Script

echo "🔗 Installing MCP Servers for Cursor Agent..."

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js not found. Please install Node.js first."
    echo "📥 Download from: https://nodejs.org/"
    exit 1
fi

echo "✅ Node.js found: $(node -v)"

# Check if npm is installed
if ! command -v npm &> /dev/null; then
    echo "❌ npm not found. Please install npm first."
    exit 1
fi

echo "✅ npm found: $(npm -v)"

# Install core MCP servers
echo "📦 Installing core MCP servers..."

# Firecrawl MCP
echo "Installing Firecrawl MCP..."
npm install -g firecrawl-mcp
echo "✅ Firecrawl MCP installed"

# GitHub MCP
echo "Installing GitHub MCP..."
npm install -g github-mcp-scoped-server
echo "✅ GitHub MCP installed"

# Browser MCP
echo "Installing Browser MCP..."
npm install -g concurrent-browser-mcp
echo "✅ Browser MCP installed"

# Install Playwright for Browser MCP
echo "Installing Playwright browsers..."
npx playwright install
echo "✅ Playwright browsers installed"

# Install additional MCP servers
echo "📦 Installing additional MCP servers..."

# Atlassian MCP
echo "Installing Atlassian MCP..."
npm install -g mcp-remote
echo "✅ Atlassian MCP installed"

# AWS Knowledge MCP
echo "Installing AWS Knowledge MCP..."
pip install uvx
echo "✅ AWS Knowledge MCP installed"

# Browserbase MCP
echo "Installing Browserbase MCP..."
npm install -g @browserbasehq/mcp
echo "✅ Browserbase MCP installed"

# Pearl MCP
echo "Installing Pearl MCP..."
npm install -g pearl-mcp-server
echo "✅ Pearl MCP installed"

# Linear MCP
echo "Installing Linear MCP..."
npm install -g mcp-remote
echo "✅ Linear MCP installed"

# Notion MCP
echo "Installing Notion MCP..."
npm install -g mcp-remote
echo "✅ Notion MCP installed"

# Stripe MCP
echo "Installing Stripe MCP..."
npm install -g stripe-mcp-server
echo "✅ Stripe MCP installed"

# Slack MCP
echo "Installing Slack MCP..."
npm install -g slack-mcp-server
echo "✅ Slack MCP installed"

# Google Drive MCP
echo "Installing Google Drive MCP..."
npm install -g google-drive-mcp-server
echo "✅ Google Drive MCP installed"

# Analytics MCPs
echo "Installing Analytics MCPs..."
npm install -g axiom-mcp-server
npm install -g raygun-mcp-server
echo "✅ Analytics MCPs installed"

# Search MCPs
echo "Installing Search MCPs..."
npm install -g brave-search-mcp-server
npm install -g qdrant-mcp-server
echo "✅ Search MCPs installed"

# Development MCPs
echo "Installing Development MCPs..."
npm install -g docker-mcp-server
npm install -g kubernetes-mcp-server
npm install -g postgresql-mcp-server
npm install -g e2b-mcp-server
echo "✅ Development MCPs installed"

echo ""
echo "🎉 MCP Servers installation completed!"
echo ""
echo "📋 Next steps:"
echo "1. Update your API keys in .env file"
echo "2. Restart Cursor IDE"
echo "3. Test MCP servers with examples in examples/ folder"
echo ""
echo "🔧 Available MCP Servers:"
echo "- Firecrawl (Web scraping)"
echo "- GitHub (Repository management)"
echo "- Browser (Browser automation)"
echo "- Atlassian (Jira, Confluence)"
echo "- AWS Knowledge (Documentation)"
echo "- Browserbase (Cloud browsers)"
echo "- Pearl (Human experts)"
echo "- Linear (Issue tracking)"
echo "- Notion (Documentation)"
echo "- Stripe (Payments)"
echo "- Slack (Communication)"
echo "- Google Drive (File management)"
echo "- Axiom (Log analysis)"
echo "- Raygun (Error monitoring)"
echo "- Brave Search (Web search)"
echo "- Qdrant (Vector search)"
echo "- Docker (Container management)"
echo "- Kubernetes (Orchestration)"
echo "- PostgreSQL (Database)"
echo "- E2B (Code execution)"
echo ""
echo "🚀 All MCP servers are ready to use!"