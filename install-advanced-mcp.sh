#!/bin/bash
# Advanced MCP Servers Installation Script

echo "🚀 Installing Advanced MCP Servers..."

# Check prerequisites
if ! command -v node &> /dev/null; then
    echo "❌ Node.js not found. Please install Node.js first."
    exit 1
fi

if ! command -v npm &> /dev/null; then
    echo "❌ npm not found. Please install npm first."
    exit 1
fi

echo "✅ Prerequisites check passed"

# Core MCP Servers
echo "📦 Installing Core MCP Servers..."
npm install -g @modelcontextprotocol/server-filesystem
npm install -g @modelcontextprotocol/server-sqlite
npm install -g @modelcontextprotocol/server-memory
npm install -g @modelcontextprotocol/server-fetch
echo "✅ Core MCP servers installed"

# Web Search MCPs
echo "🔍 Installing Web Search MCPs..."
npm install -g tavily-mcp
npm install -g brave-search-mcp-server
npm install -g duckduckgo-mcp-server
echo "✅ Web Search MCPs installed"

# Productivity MCPs
echo "📅 Installing Productivity MCPs..."
npm install -g calendar-mcp-server
npm install -g email-mcp-server
npm install -g weather-mcp-server
npm install -g time-mcp-server
echo "✅ Productivity MCPs installed"

# Media MCPs
echo "🎵 Installing Media MCPs..."
npm install -g youtube-mcp-server
npm install -g spotify-mcp-server
npm install -g podcast-mcp-server
echo "✅ Media MCPs installed"

# Development MCPs
echo "🛠️ Installing Development MCPs..."
npm install -g figma-mcp
npm install -g ref-tools-mcp
npm install -g puppeteer-mcp-server
npm install -g git-mcp-server
echo "✅ Development MCPs installed"

# Business MCPs
echo "💼 Installing Business MCPs..."
npm install -g stock-mcp-server
npm install -g crypto-mcp-server
npm install -g banking-mcp-server
echo "✅ Business MCPs installed"

# Analytics MCPs
echo "📊 Installing Analytics MCPs..."
npm install -g @oneuptime/mcp-server
npm install -g google-analytics-mcp-server
npm install -g performance-mcp-server
echo "✅ Analytics MCPs installed"

echo ""
echo "🎉 Advanced MCP Servers installation completed!"
echo ""
echo "📋 Next steps:"
echo "1. Update your API keys in .env file"
echo "2. Update cursor-settings.json with new servers"
echo "3. Restart Cursor IDE"
echo ""
echo "🔧 New MCP Servers available:"
echo "- Filesystem access"
echo "- SQLite database"
echo "- Memory management"
echo "- HTTP fetch"
echo "- Tavily search (AI-powered)"
echo "- Brave search"
echo "- DuckDuckGo search"
echo "- Calendar integration"
echo "- Email management"
echo "- Weather information"
echo "- Time zone management"
echo "- YouTube integration"
echo "- Spotify music"
echo "- Podcast management"
echo "- Figma integration"
echo "- Ref tools"
echo "- Puppeteer automation"
echo "- Git operations"
echo "- Stock market data"
echo "- Cryptocurrency"
echo "- Banking integration"
echo "- OneUptime monitoring"
echo "- Google Analytics"
echo "- Performance monitoring"
echo ""
echo "🚀 Your advanced MCP setup is ready!"