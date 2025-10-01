#!/bin/bash
# API Keys Setup Script for Cursor Agent Learning Hub

echo "🔑 API Keys Setup for Cursor Agent Learning Hub"
echo "=============================================="
echo ""

# Function to prompt for API key
prompt_api_key() {
    local key_name="$1"
    local description="$2"
    local current_value="$3"
    
    echo "📋 $description"
    echo "Current value: $current_value"
    echo ""
    read -p "Enter your $key_name (or press Enter to skip): " new_value
    
    if [ -n "$new_value" ]; then
        echo "$new_value"
    else
        echo "$current_value"
    fi
}

# Load current environment file
ENV_FILE="/workspace/configs/environment.env"
if [ -f "$ENV_FILE" ]; then
    echo "📁 Loading current environment file..."
    source "$ENV_FILE"
else
    echo "❌ Environment file not found at $ENV_FILE"
    exit 1
fi

echo "🔧 Setting up API Keys..."
echo "========================="
echo ""

# Core API Keys
echo "🎯 Core API Keys (Required for basic functionality):"
echo "---------------------------------------------------"

GITHUB_TOKEN=$(prompt_api_key "GITHUB_TOKEN" "GitHub Personal Access Token for repository access" "$GITHUB_TOKEN")
SUPABASE_URL=$(prompt_api_key "SUPABASE_URL" "Supabase project URL" "$SUPABASE_URL")
SUPABASE_ANON_KEY=$(prompt_api_key "SUPABASE_ANON_KEY" "Supabase anonymous key" "$SUPABASE_ANON_KEY")

echo ""
echo "🔍 Search & Web APIs:"
echo "--------------------"

TAVILY_API_KEY=$(prompt_api_key "TAVILY_API_KEY" "Tavily API key for web search" "$TAVILY_API_KEY")
FIRECRAWL_API_KEY=$(prompt_api_key "FIRECRAWL_API_KEY" "Firecrawl API key for web scraping" "$FIRECRAWL_API_KEY")

echo ""
echo "📊 Monitoring & Analytics:"
echo "-------------------------"

SENTRY_AUTH_TOKEN=$(prompt_api_key "SENTRY_AUTH_TOKEN" "Sentry auth token for error monitoring" "$SENTRY_AUTH_TOKEN")
SENTRY_ORG=$(prompt_api_key "SENTRY_ORG" "Sentry organization slug" "$SENTRY_ORG")
SENTRY_PROJECT=$(prompt_api_key "SENTRY_PROJECT" "Sentry project slug" "$SENTRY_PROJECT")

echo ""
echo "🚀 Deployment & Infrastructure:"
echo "------------------------------"

HEROKU_API_KEY=$(prompt_api_key "HEROKU_API_KEY" "Heroku API key for deployment" "$HEROKU_API_KEY")
KUBECONFIG=$(prompt_api_key "KUBECONFIG" "Kubernetes config path" "$KUBECONFIG")

echo ""
echo "💼 Business & CRM:"
echo "-----------------"

HUBSPOT_ACCESS_TOKEN=$(prompt_api_key "HUBSPOT_ACCESS_TOKEN" "HubSpot access token for CRM" "$HUBSPOT_ACCESS_TOKEN")
NOTION_API_KEY=$(prompt_api_key "NOTION_API_KEY" "Notion API key for documentation" "$NOTION_API_KEY")

echo ""
echo "🤖 Automation & Web Scraping:"
echo "----------------------------"

APIFY_API_TOKEN=$(prompt_api_key "APIFY_API_TOKEN" "Apify API token for web automation" "$APIFY_API_TOKEN")

echo ""
echo "🌐 Browser & Testing:"
echo "--------------------"

BROWSERBASE_API_KEY=$(prompt_api_key "BROWSERBASE_API_KEY" "Browserbase API key for browser automation" "$BROWSERBASE_API_KEY")
BROWSERBASE_PROJECT_ID=$(prompt_api_key "BROWSERBASE_PROJECT_ID" "Browserbase project ID" "$BROWSERBASE_PROJECT_ID")

echo ""
echo "💬 Communication:"
echo "----------------"

SLACK_BOT_TOKEN=$(prompt_api_key "SLACK_BOT_TOKEN" "Slack bot token for notifications" "$SLACK_BOT_TOKEN")

echo ""
echo "📊 Monitoring & Observability:"
echo "-----------------------------"

DATADOG_API_KEY=$(prompt_api_key "DATADOG_API_KEY" "Datadog API key for monitoring" "$DATADOG_API_KEY")
DATADOG_APP_KEY=$(prompt_api_key "DATADOG_APP_KEY" "Datadog application key" "$DATADOG_APP_KEY")

echo ""
echo "💾 Database & Storage:"
echo "---------------------"

QDRANT_URL=$(prompt_api_key "QDRANT_URL" "Qdrant vector database URL" "$QDRANT_URL")
POSTGRES_CONNECTION_STRING=$(prompt_api_key "POSTGRES_CONNECTION_STRING" "PostgreSQL connection string" "$POSTGRES_CONNECTION_STRING")

echo ""
echo "💾 Saving API Keys..."
echo "===================="

# Create backup
cp "$ENV_FILE" "$ENV_FILE.backup.$(date +%Y%m%d_%H%M%S)"

# Update environment file
cat > "$ENV_FILE" << EOF
# Environment Variables for Cursor Agent Learning Hub - MCP Configuration

# Core MCP Servers (Required)
FIRECRAWL_API_KEY=$FIRECRAWL_API_KEY
GITHUB_TOKEN=$GITHUB_TOKEN

# Browser & Automation MCPs
BROWSERBASE_API_KEY=$BROWSERBASE_API_KEY
BROWSERBASE_PROJECT_ID=$BROWSERBASE_PROJECT_ID

# Communication MCPs
SLACK_BOT_TOKEN=$SLACK_BOT_TOKEN

# Database & Search MCPs
QDRANT_URL=$QDRANT_URL
POSTGRES_CONNECTION_STRING=$POSTGRES_CONNECTION_STRING

# Development & Infrastructure MCPs
KUBECONFIG=$KUBECONFIG

# Monitoring MCPs
SENTRY_AUTH_TOKEN=$SENTRY_AUTH_TOKEN

# Performance & Monitoring
CURSOR_PERFORMANCE_MONITORING=true
CURSOR_COST_ALERT_THRESHOLD=80
CURSOR_COST_STOP_THRESHOLD=95
CURSOR_CONTEXT_MAX_USAGE=80

# Vietnamese Language Configuration
CURSOR_DEFAULT_LANGUAGE=vi
CURSOR_CULTURAL_CONTEXT=vietnam
CURSOR_DATE_FORMAT=dd/MM/yyyy
CURSOR_CURRENCY=VND
CURSOR_TIMEZONE=Asia/Ho_Chi_Minh

# Management Focus Configuration
CURSOR_MANAGEMENT_FOCUS=true
CURSOR_BUSINESS_TERMINOLOGY=true
CURSOR_EXECUTIVE_SUMMARY=true
CURSOR_COMPLIANCE_MODE=true

# Security Configuration
CURSOR_TOOL_APPROVAL=true
CURSOR_SECURITY_MODE=true
CURSOR_AUDIT_LOGGING=true
CURSOR_PERMISSION_CHECKS=true

# New MCP Servers API Keys
SENTRY_AUTH_TOKEN=$SENTRY_AUTH_TOKEN
SENTRY_ORG=$SENTRY_ORG
SENTRY_PROJECT=$SENTRY_PROJECT
HEROKU_API_KEY=$HEROKU_API_KEY
SUPABASE_URL=$SUPABASE_URL
SUPABASE_ANON_KEY=$SUPABASE_ANON_KEY
APIFY_API_TOKEN=$APIFY_API_TOKEN
HUBSPOT_ACCESS_TOKEN=$HUBSPOT_ACCESS_TOKEN
TAVILY_API_KEY=$TAVILY_API_KEY
DATADOG_API_KEY=$DATADOG_API_KEY
DATADOG_APP_KEY=$DATADOG_APP_KEY

# Unified Email Integration
GITHUB_EMAIL=begau1302@gmail.com
CURSOR_EMAIL=begau1302@gmail.com
MCP_EMAIL=begau1302@gmail.com
NOTIFICATION_EMAIL=begau1302@gmail.com
ALERT_EMAIL=begau1302@gmail.com
REPORT_EMAIL=begau1302@gmail.com

# Auto-sync Configuration
AUTO_SYNC_ENABLED=true
AUTO_SYNC_FREQUENCY=real_time
AUTO_SYNC_SERVICES=github,cursor,mcp_servers,notifications
EOF

# Copy to Cursor directory
cp "$ENV_FILE" ~/.cursor/.env

echo "✅ API Keys saved successfully!"
echo ""

# Test API keys
echo "🧪 Testing API Keys..."
echo "====================="

# Test GitHub token
if [ -n "$GITHUB_TOKEN" ] && [ "$GITHUB_TOKEN" != "your_github_token_here" ]; then
    echo "🔍 Testing GitHub token..."
    if curl -s -H "Authorization: token $GITHUB_TOKEN" https://api.github.com/user > /dev/null; then
        echo "✅ GitHub token - Valid"
    else
        echo "❌ GitHub token - Invalid"
    fi
fi

# Test Supabase
if [ -n "$SUPABASE_URL" ] && [ "$SUPABASE_URL" != "your_supabase_url_here" ]; then
    echo "🔍 Testing Supabase connection..."
    if curl -s "$SUPABASE_URL/rest/v1/" > /dev/null; then
        echo "✅ Supabase URL - Valid"
    else
        echo "❌ Supabase URL - Invalid"
    fi
fi

echo ""
echo "🎉 API Keys Setup Complete!"
echo "=========================="
echo ""
echo "📝 Next Steps:"
echo "1. Restart Cursor IDE: ~/.cursor/start-cursor.sh"
echo "2. Test MCP servers: node /workspace/test-mcp-config.js"
echo "3. Run system test: ./test-system.sh"
echo ""
echo "🔧 Troubleshooting:"
echo "- Check logs: tail -f ~/.cursor/logs/cursor.log"
echo "- Verify API keys: source ~/.cursor/.env && echo \$GITHUB_TOKEN"
echo "- Test individual MCP: npx @modelcontextprotocol/server-filesystem --help"