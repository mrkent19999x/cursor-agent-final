#!/bin/bash
# API Keys Setup Script for Cursor Agent Learning Hub

echo "🔑 API Keys Setup Script"
echo "========================"
echo ""

# Check if environment.env exists
if [ ! -f "/workspace/configs/environment.env" ]; then
    echo "❌ environment.env file not found!"
    exit 1
fi

echo "✅ Found environment.env file"
echo ""

# Function to update API key
update_api_key() {
    local key_name=$1
    local description=$2
    local current_value=$(grep "^${key_name}=" /workspace/configs/environment.env | cut -d'=' -f2)
    
    echo "🔧 ${description}"
    echo "Current value: ${current_value}"
    echo ""
    echo "Options:"
    echo "1. Enter new API key"
    echo "2. Skip this key"
    echo "3. Use placeholder (for testing)"
    echo ""
    read -p "Choose option (1-3): " choice
    
    case $choice in
        1)
            read -p "Enter new API key: " new_key
            if [ ! -z "$new_key" ]; then
                sed -i "s|^${key_name}=.*|${key_name}=${new_key}|" /workspace/configs/environment.env
                echo "✅ Updated ${key_name}"
            else
                echo "❌ Empty key, skipping..."
            fi
            ;;
        2)
            echo "⏭️ Skipped ${key_name}"
            ;;
        3)
            echo "📝 Using placeholder for ${key_name}"
            ;;
        *)
            echo "❌ Invalid option, skipping..."
            ;;
    esac
    echo ""
}

# Interactive API key setup
echo "🎯 Let's set up your API keys!"
echo "You can skip any key you don't have or don't want to use."
echo ""

# Core MCP Servers
echo "📦 Core MCP Servers:"
echo "==================="
update_api_key "GITHUB_TOKEN" "GitHub Personal Access Token (for repository management)"
update_api_key "FIRECRAWL_API_KEY" "Firecrawl API Key (for web scraping)"

# Business & Management MCPs
echo "💼 Business & Management MCPs:"
echo "============================="
update_api_key "NOTION_API_KEY" "Notion API Key (for document management)"
update_api_key "SENTRY_AUTH_TOKEN" "Sentry Auth Token (for error monitoring)"
update_api_key "SENTRY_ORG" "Sentry Organization (for error monitoring)"
update_api_key "SENTRY_PROJECT" "Sentry Project (for error monitoring)"
update_api_key "HEROKU_API_KEY" "Heroku API Key (for app deployment)"
update_api_key "SUPABASE_URL" "Supabase URL (for database management)"
update_api_key "SUPABASE_ANON_KEY" "Supabase Anonymous Key (for database management)"
update_api_key "APIFY_API_TOKEN" "Apify API Token (for web automation)"
update_api_key "HUBSPOT_ACCESS_TOKEN" "HubSpot Access Token (for CRM)"
update_api_key "TAVILY_API_KEY" "Tavily API Key (for web search)"

# Monitoring & Analytics MCPs
echo "📊 Monitoring & Analytics MCPs:"
echo "==============================="
update_api_key "DATADOG_API_KEY" "Datadog API Key (for monitoring)"
update_api_key "DATADOG_APP_KEY" "Datadog App Key (for monitoring)"

# Browser & Automation MCPs
echo "🌐 Browser & Automation MCPs:"
echo "============================="
update_api_key "BROWSERBASE_API_KEY" "Browserbase API Key (for cloud browsers)"
update_api_key "BROWSERBASE_PROJECT_ID" "Browserbase Project ID (for cloud browsers)"

# Communication MCPs
echo "💬 Communication MCPs:"
echo "===================="
update_api_key "SLACK_BOT_TOKEN" "Slack Bot Token (for team communication)"

# Database MCPs
echo "🗄️ Database MCPs:"
echo "================="
update_api_key "POSTGRES_CONNECTION_STRING" "PostgreSQL Connection String (for database)"

echo "🎉 API Keys setup complete!"
echo "========================="
echo ""
echo "📋 Summary of changes:"
echo "======================"

# Show updated keys
echo "Updated API keys:"
grep -E "^[A-Z_]+_API_KEY=|^[A-Z_]+_TOKEN=|^[A-Z_]+_URL=|^[A-Z_]+_ORG=|^[A-Z_]+_PROJECT=|^[A-Z_]+_ID=" /workspace/configs/environment.env | grep -v "your_.*_here" | while read line; do
    key_name=$(echo $line | cut -d'=' -f1)
    echo "✅ $key_name"
done

echo ""
echo "📝 Next steps:"
echo "=============="
echo "1. Test your API keys with: node test-mcp-config.js"
echo "2. Copy cursor-settings.json to your Cursor IDE configuration"
echo "3. Restart Cursor IDE"
echo "4. Test MCP servers in Cursor"
echo ""
echo "🔗 Need help getting API keys? Check: /workspace/API_KEYS_GUIDE.md"
echo ""
echo "🚀 Ready to use MCP servers with Cursor IDE!"