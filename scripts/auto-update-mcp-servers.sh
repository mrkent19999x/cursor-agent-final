#!/bin/bash
# Auto Update MCP Servers Script
# Chạy hàng ngày để update MCP servers lên version mới nhất

echo "🔄 Checking MCP Servers updates..."
echo "📅 Date: $(date)"

# List các MCP servers cần check
MCP_SERVERS=(
    "@modelcontextprotocol/server-filesystem"
    "@modelcontextprotocol/server-github"
    "@modelcontextprotocol/server-brave-search"
    "@modelcontextprotocol/server-puppeteer"
    "@modelcontextprotocol/server-sequential-thinking"
)

# Check và update từng server
for server in "${MCP_SERVERS[@]}"; do
    echo ""
    echo "📦 Checking $server..."
    
    # Check version hiện tại
    CURRENT_VERSION=$(npm list -g $server 2>/dev/null | grep "$server" | awk '{print $2}' | tr -d '└─┬')
    
    if [ -z "$CURRENT_VERSION" ]; then
        echo "⚠️  $server not installed, skipping..."
        continue
    fi
    
    # Get latest version
    LATEST_VERSION=$(npm view $server version 2>/dev/null)
    
    if [ -z "$LATEST_VERSION" ]; then
        echo "⚠️  Cannot get latest version for $server"
        continue
    fi
    
    # Compare versions
    if [ "$CURRENT_VERSION" != "$LATEST_VERSION" ]; then
        echo "🔄 Update available: $CURRENT_VERSION → $LATEST_VERSION"
        echo "⏳ Updating..."
        
        # Update
        npm install -g $server@latest
        
        if [ $? -eq 0 ]; then
            echo "✅ Updated $server to $LATEST_VERSION"
        else
            echo "❌ Failed to update $server"
        fi
    else
        echo "✅ $server is up to date ($CURRENT_VERSION)"
    fi
done

echo ""
echo "✅ MCP Servers update check completed"
echo "📅 Finished at: $(date)"

