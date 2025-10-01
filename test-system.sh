#!/bin/bash
# Comprehensive System Test for Cursor Agent Learning Hub

echo "🧪 Comprehensive System Test"
echo "==========================="
echo ""

# Test results tracking
TOTAL_TESTS=0
PASSED_TESTS=0
FAILED_TESTS=0

# Function to run test
run_test() {
    local test_name="$1"
    local test_command="$2"
    local expected_result="$3"
    
    TOTAL_TESTS=$((TOTAL_TESTS + 1))
    
    echo "🔍 Testing: $test_name"
    
    if eval "$test_command" > /dev/null 2>&1; then
        echo "✅ PASS: $test_name"
        PASSED_TESTS=$((PASSED_TESTS + 1))
        return 0
    else
        echo "❌ FAIL: $test_name"
        FAILED_TESTS=$((FAILED_TESTS + 1))
        return 1
    fi
}

# Function to check file exists
check_file() {
    local file_path="$1"
    local description="$2"
    
    TOTAL_TESTS=$((TOTAL_TESTS + 1))
    
    echo "🔍 Checking: $description"
    
    if [ -f "$file_path" ]; then
        echo "✅ PASS: $description exists"
        PASSED_TESTS=$((PASSED_TESTS + 1))
        return 0
    else
        echo "❌ FAIL: $description not found"
        FAILED_TESTS=$((FAILED_TESTS + 1))
        return 1
    fi
}

# Function to check directory exists
check_directory() {
    local dir_path="$1"
    local description="$2"
    
    TOTAL_TESTS=$((TOTAL_TESTS + 1))
    
    echo "🔍 Checking: $description"
    
    if [ -d "$dir_path" ]; then
        echo "✅ PASS: $description exists"
        PASSED_TESTS=$((PASSED_TESTS + 1))
        return 0
    else
        echo "❌ FAIL: $description not found"
        FAILED_TESTS=$((FAILED_TESTS + 1))
        return 1
    fi
}

echo "📋 Testing System Components..."
echo "==============================="
echo ""

# Test 1: Dependencies
echo "🔧 Testing Dependencies:"
echo "------------------------"
run_test "Node.js Installation" "node --version"
run_test "npm Installation" "npm --version"
run_test "Python Installation" "python3 --version"
echo ""

# Test 2: Project Structure
echo "📁 Testing Project Structure:"
echo "----------------------------"
check_directory "/workspace" "Workspace directory"
check_directory "/workspace/docs" "Documentation directory"
check_directory "/workspace/configs" "Configuration directory"
check_directory "/workspace/scripts" "Scripts directory"
check_file "/workspace/README.md" "README file"
echo ""

# Test 3: Configuration Files
echo "⚙️ Testing Configuration Files:"
echo "------------------------------"
check_file "/workspace/configs/cursor-settings.json" "Cursor settings"
check_file "/workspace/configs/environment.env" "Environment variables"
check_file "/workspace/configs/ultimate-assistant.json" "Ultimate assistant config"
check_file "/workspace/configs/agents.md" "Agent rules"
echo ""

# Test 4: Cursor IDE Configuration
echo "🎯 Testing Cursor IDE Configuration:"
echo "------------------------------------"
check_directory "$HOME/.cursor" "Cursor config directory"
check_file "$HOME/.cursor/settings.json" "Cursor settings file"
check_file "$HOME/.cursor/.env" "Cursor environment file"
check_file "$HOME/.cursor/start-cursor.sh" "Cursor startup script"
echo ""

# Test 5: MCP Servers Installation
echo "🔗 Testing MCP Servers Installation:"
echo "------------------------------------"
run_test "Filesystem MCP" "npx @modelcontextprotocol/server-filesystem --help"
run_test "Notion MCP" "npx @notionhq/notion-mcp-server --help"
run_test "Supabase MCP" "npx @supabase/mcp-server-supabase --help"
run_test "Sentry MCP" "npx @sentry/mcp-server --help"
run_test "Apify MCP" "npx @apify/actors-mcp-server --help"
run_test "Tavily MCP" "npx tavily-mcp --help"
echo ""

# Test 6: Environment Variables
echo "🔑 Testing Environment Variables:"
echo "--------------------------------"
run_test "GITHUB_TOKEN" "[ -n \"\$GITHUB_TOKEN\" ]"
run_test "SUPABASE_URL" "[ -n \"\$SUPABASE_URL\" ]"
run_test "TAVILY_API_KEY" "[ -n \"\$TAVILY_API_KEY\" ]"
run_test "SENTRY_AUTH_TOKEN" "[ -n \"\$SENTRY_AUTH_TOKEN\" ]"
echo ""

# Test 7: Scripts
echo "📜 Testing Scripts:"
echo "------------------"
check_file "/workspace/install-missing-mcp.sh" "MCP installation script"
check_file "/workspace/setup-api-keys.sh" "API keys setup script"
check_file "/workspace/setup-cursor-config.sh" "Cursor config script"
check_file "/workspace/install-cursor-and-config.sh" "Cursor installation script"
check_file "/workspace/test-mcp-config.js" "MCP test script"
echo ""

# Test 8: Documentation
echo "📚 Testing Documentation:"
echo "------------------------"
check_file "/workspace/API_KEYS_GUIDE.md" "API keys guide"
check_file "/workspace/MCP_SETUP_GUIDE.md" "MCP setup guide"
check_file "/workspace/ADVANCED_MCP_SERVERS.md" "Advanced MCP servers guide"
echo ""

# Test 9: Run MCP Configuration Test
echo "🧪 Running MCP Configuration Test:"
echo "---------------------------------"
if [ -f "/workspace/test-mcp-config.js" ]; then
    echo "Running comprehensive MCP test..."
    node /workspace/test-mcp-config.js
else
    echo "❌ MCP test script not found"
    FAILED_TESTS=$((FAILED_TESTS + 1))
fi
echo ""

# Test 10: System Performance
echo "⚡ Testing System Performance:"
echo "----------------------------"
run_test "Disk Space" "[ \$(df /workspace | tail -1 | awk '{print \$4}') -gt 1000000 ]"
run_test "Memory Available" "[ \$(free -m | awk 'NR==2{print \$7}') -gt 500 ]"
run_test "CPU Load" "[ \$(uptime | awk '{print \$10}' | sed 's/,//') -lt 2.0 ]"
echo ""

# Final Results
echo "📊 Test Results Summary:"
echo "========================"
echo "Total Tests: $TOTAL_TESTS"
echo "Passed: $PASSED_TESTS"
echo "Failed: $FAILED_TESTS"
echo "Success Rate: $(( (PASSED_TESTS * 100) / TOTAL_TESTS ))%"
echo ""

if [ $FAILED_TESTS -eq 0 ]; then
    echo "🎉 All tests passed! System is ready to use."
    echo "============================================="
elif [ $FAILED_TESTS -lt $((TOTAL_TESTS / 2)) ]; then
    echo "⚠️ Some tests failed, but system is mostly functional."
    echo "====================================================="
else
    echo "❌ Many tests failed. System needs attention."
    echo "============================================="
fi

echo ""
echo "🔧 Troubleshooting:"
echo "==================="
if [ $FAILED_TESTS -gt 0 ]; then
    echo "1. Check failed components above"
    echo "2. Run individual test scripts"
    echo "3. Check logs for errors"
    echo "4. Verify API keys are set"
    echo "5. Restart Cursor IDE"
fi

echo ""
echo "📝 Next Steps:"
echo "=============="
echo "1. Start Cursor IDE: $HOME/.cursor/start-cursor.sh"
echo "2. Test MCP servers in Cursor"
echo "3. Update API keys as needed"
echo "4. Check Cursor logs for errors"
echo ""

echo "🚀 System Test Complete!"
echo "========================"