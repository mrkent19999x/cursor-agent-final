#!/bin/bash
# Complete Advanced MCP Setup Script

echo "🚀 Setting up Advanced MCP Configuration..."

# Make scripts executable
chmod +x install-advanced-mcp.sh
chmod +x setup-mcp-local.sh

# Run advanced MCP installation
echo "📦 Installing advanced MCP servers..."
./install-advanced-mcp.sh

# Setup configuration
echo "⚙️ Setting up advanced configuration..."

# Copy advanced settings
cp configs/cursor-settings-advanced.json ~/.cursor/settings.json
echo "✅ Advanced Cursor settings copied"

# Copy advanced environment
cp configs/environment-advanced.env .env
echo "✅ Advanced environment configuration copied"

echo ""
echo "🎉 Advanced MCP setup completed!"
echo ""
echo "📋 Next steps:"
echo "1. Get API keys from these services:"
echo "   🔍 Tavily Search: https://tavily.com/"
echo "   🦁 Brave Search: https://brave.com/search/api/"
echo "   🦆 DuckDuckGo: Free (no API key needed)"
echo "   🌤️ Weather: https://openweathermap.org/api"
echo "   📺 YouTube: https://console.developers.google.com/"
echo "   🎵 Spotify: https://developer.spotify.com/"
echo "   🎨 Figma: https://www.figma.com/developers/api"
echo ""
echo "2. Update .env file with your actual API keys"
echo ""
echo "3. Restart Cursor IDE"
echo ""
echo "4. Test new MCP servers:"
echo "   - 'Tìm kiếm thông tin về AI trên Tavily'"
echo "   - 'Tìm kiếm Brave về công nghệ mới nhất'"
echo "   - 'Xem thời tiết hôm nay'"
echo "   - 'Tìm video YouTube về lập trình'"
echo "   - 'Phát nhạc Spotify'"
echo "   - 'Mở file Figma design'"
echo ""
echo "🔧 Available Advanced MCP Servers:"
echo "✅ Filesystem access"
echo "✅ SQLite database"
echo "✅ Memory management"
echo "✅ HTTP fetch"
echo "✅ Tavily search (AI-powered)"
echo "✅ Brave search"
echo "✅ DuckDuckGo search"
echo "✅ Weather information"
echo "✅ Time zone management"
echo "✅ YouTube integration"
echo "✅ Spotify music"
echo "✅ Figma integration"
echo "✅ Firecrawl web scraping"
echo "✅ GitHub integration"
echo "✅ Browser automation"
echo "✅ Browserbase cloud browsers"
echo "✅ Slack communication"
echo "✅ Qdrant vector search"
echo "✅ Docker container management"
echo "✅ Kubernetes orchestration"
echo "✅ Sentry error monitoring"
echo ""
echo "🚀 Your advanced MCP setup is ready!"
echo "💡 Pro tip: Tavily search sẽ thay thế web search truyền thống với AI-powered results!"