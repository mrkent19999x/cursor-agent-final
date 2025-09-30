#!/bin/bash
# Cursor Agent Learning Hub - Setup Script

echo "🚀 Setting up Cursor Agent Learning Hub..."

# Check if Cursor is installed
if ! command -v cursor &> /dev/null; then
    echo "❌ Cursor IDE not found. Please install Cursor first."
    echo "📥 Download from: https://cursor.com/downloads"
    exit 1
fi

echo "✅ Cursor IDE found"

# Backup existing settings
if [ -f ~/.cursor/settings.json ]; then
    cp ~/.cursor/settings.json ~/.cursor/settings.json.backup.$(date +%Y%m%d_%H%M%S)
    echo "✅ Existing settings backed up"
fi

# Copy configuration files
echo "📋 Copying configuration files..."

# Copy global settings
cp configs/cursor-settings.json ~/.cursor/settings.json
echo "✅ Global settings copied"

# Copy MCP servers config
cp configs/mcp-servers.json ~/.cursor/mcp.json
echo "✅ MCP servers config copied"

# Copy agent rules
cp configs/agents.md ./AGENTS.md
echo "✅ Agent rules copied"

# Setup environment variables
if [ -f configs/environment.env ]; then
    cp configs/environment.env .env
    echo "✅ Environment variables copied"
    echo "⚠️  Please update .env with your actual API keys"
fi

echo ""
echo "🎉 Setup completed successfully!"
echo ""
echo "📋 Next steps:"
echo "1. Update .env file with your actual API keys"
echo "2. Restart Cursor IDE to apply changes"
echo "3. Run ./scripts/install-mcp-servers.sh to install MCP servers"
echo "4. Test configuration with examples in examples/ folder"
echo ""
echo "📚 Documentation available in docs/ folder"
echo "🔧 Configuration files in configs/ folder"
echo "📊 Monitoring tools in monitoring/ folder"
echo ""
echo "🚀 Cursor Agent Learning Hub is ready!"