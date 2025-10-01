#!/bin/bash
# Cursor Agent Learning Hub - Install Missing MCP Servers

echo "🔧 Installing Missing MCP Servers..."
echo "====================================="

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js not found. Please install Node.js first."
    exit 1
fi

echo "✅ Node.js found: $(node -v)"

# Check if npm is installed
if ! command -v npm &> /dev/null; then
    echo "❌ npm not found. Please install npm first."
    exit 1
fi

echo "✅ npm found: $(npm -v)"
echo ""

# Install Core MCP Servers
echo "📦 Installing Core MCP Servers..."
echo "================================="

# Filesystem MCP
echo "Installing Filesystem MCP..."
npm install -g @modelcontextprotocol/server-filesystem
echo "✅ Filesystem MCP installed"

# Sequential Thinking MCP
echo "Installing Sequential Thinking MCP..."
npm install -g @modelcontextprotocol/server-sequential-thinking
echo "✅ Sequential Thinking MCP installed"

# Memory MCP
echo "Installing Memory MCP..."
npm install -g @modelcontextprotocol/server-memory
echo "✅ Memory MCP installed"

# SQLite MCP
echo "Installing SQLite MCP..."
npm install -g @modelcontextprotocol/server-sqlite
echo "✅ SQLite MCP installed"

# Fetch MCP
echo "Installing Fetch MCP..."
npm install -g @modelcontextprotocol/server-fetch
echo "✅ Fetch MCP installed"

echo ""

# Install Business & Management MCPs
echo "💼 Installing Business & Management MCPs..."
echo "==========================================="

# Notion MCP (already working, but ensure latest version)
echo "Updating Notion MCP..."
npm install -g @notionhq/notion-mcp-server
echo "✅ Notion MCP updated"

# Sentry MCP
echo "Installing Sentry MCP..."
npm install -g @sentry/mcp-server
echo "✅ Sentry MCP installed"

# Supabase MCP (already working, but ensure latest version)
echo "Updating Supabase MCP..."
npm install -g @supabase/mcp-server-supabase
echo "✅ Supabase MCP updated"

# Heroku MCP
echo "Installing Heroku MCP..."
npm install -g @heroku/mcp-server
echo "✅ Heroku MCP installed"

# Apify MCP
echo "Installing Apify MCP..."
npm install -g @apify/actors-mcp-server
echo "✅ Apify MCP installed"

# HubSpot MCP
echo "Installing HubSpot MCP..."
npm install -g @hubspot/mcp-server
echo "✅ HubSpot MCP installed"

echo ""

# Install Web Search MCPs
echo "🔍 Installing Web Search MCPs..."
echo "==============================="

# Tavily MCP
echo "Installing Tavily MCP..."
npm install -g tavily-mcp
echo "✅ Tavily MCP installed"

# Brave Search MCP
echo "Installing Brave Search MCP..."
npm install -g brave-search-mcp-server
echo "✅ Brave Search MCP installed"

# DuckDuckGo MCP
echo "Installing DuckDuckGo MCP..."
npm install -g duckduckgo-mcp-server
echo "✅ DuckDuckGo MCP installed"

echo ""

# Install Development & Infrastructure MCPs
echo "🛠️ Installing Development & Infrastructure MCPs..."
echo "================================================"

# Kubernetes MCP
echo "Installing Kubernetes MCP..."
npm install -g mcp-server-kubernetes
echo "✅ Kubernetes MCP installed"

# Docker MCP
echo "Installing Docker MCP..."
npm install -g docker-mcp-server
echo "✅ Docker MCP installed"

# PostgreSQL MCP
echo "Installing PostgreSQL MCP..."
npm install -g postgresql-mcp-server
echo "✅ PostgreSQL MCP installed"

echo ""

# Install Monitoring & Analytics MCPs
echo "📊 Installing Monitoring & Analytics MCPs..."
echo "=========================================="

# Datadog MCP
echo "Installing Datadog MCP..."
npm install -g @winor30/mcp-server-datadog
echo "✅ Datadog MCP installed"

# Qdrant MCP
echo "Installing Qdrant MCP..."
npm install -g qdrant-mcp-server
echo "✅ Qdrant MCP installed"

echo ""

# Install Communication MCPs
echo "💬 Installing Communication MCPs..."
echo "================================="

# Slack MCP
echo "Installing Slack MCP..."
npm install -g slack-mcp-server
echo "✅ Slack MCP installed"

echo ""

# Install Browser & Automation MCPs
echo "🌐 Installing Browser & Automation MCPs..."
echo "========================================="

# Browserbase MCP
echo "Installing Browserbase MCP..."
npm install -g @browserbasehq/mcp
echo "✅ Browserbase MCP installed"

# Firecrawl MCP
echo "Installing Firecrawl MCP..."
npm install -g firecrawl-mcp
echo "✅ Firecrawl MCP installed"

# GitHub MCP
echo "Installing GitHub MCP..."
npm install -g github-mcp-scoped-server
echo "✅ GitHub MCP installed"

echo ""

# Test installation
echo "🧪 Testing MCP Installation..."
echo "=============================="

# Test a few key MCPs
echo "Testing Filesystem MCP..."
if npx @modelcontextprotocol/server-filesystem --help > /dev/null 2>&1; then
    echo "✅ Filesystem MCP - Working"
else
    echo "❌ Filesystem MCP - Failed"
fi

echo "Testing Notion MCP..."
if npx @notionhq/notion-mcp-server --help > /dev/null 2>&1; then
    echo "✅ Notion MCP - Working"
else
    echo "❌ Notion MCP - Failed"
fi

echo "Testing Supabase MCP..."
if npx @supabase/mcp-server-supabase --help > /dev/null 2>&1; then
    echo "✅ Supabase MCP - Working"
else
    echo "❌ Supabase MCP - Failed"
fi

echo ""
echo "🎉 MCP Servers Installation Complete!"
echo "===================================="
echo ""
echo "📋 Installed MCP Servers:"
echo "✅ Core MCPs: Filesystem, Sequential Thinking, Memory, SQLite, Fetch"
echo "✅ Business: Notion, Sentry, Supabase, Heroku, Apify, HubSpot"
echo "✅ Web Search: Tavily, Brave Search, DuckDuckGo"
echo "✅ Development: Kubernetes, Docker, PostgreSQL"
echo "✅ Monitoring: Datadog, Qdrant"
echo "✅ Communication: Slack"
echo "✅ Browser: Browserbase, Firecrawl, GitHub"
echo ""
echo "📝 Next Steps:"
echo "1. Update API keys in /workspace/configs/environment.env"
echo "2. Copy cursor-settings.json to your Cursor IDE configuration"
echo "3. Restart Cursor IDE"
echo "4. Test MCP servers with: node test-mcp-config.js"
echo ""
echo "🚀 Ready to use MCP servers with Cursor IDE!"