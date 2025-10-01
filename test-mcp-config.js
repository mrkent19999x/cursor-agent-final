#!/usr/bin/env node

/**
 * MCP Configuration Test Script
 * Tests if MCP servers are properly installed and configured
 */

const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');

console.log('🔧 Testing MCP Configuration...\n');

// Test MCP servers
const mcpServers = [
  {
    name: 'Filesystem MCP',
    command: 'npx',
    args: ['-y', '@modelcontextprotocol/server-filesystem', '--help'],
    timeout: 10000
  },
  {
    name: 'Sequential Thinking MCP',
    command: 'npx',
    args: ['-y', '@modelcontextprotocol/server-sequential-thinking', '--help'],
    timeout: 10000
  },
  {
    name: 'Notion MCP',
    command: 'npx',
    args: ['-y', '@notionhq/notion-mcp-server', '--help'],
    timeout: 10000
  },
  {
    name: 'Sentry MCP',
    command: 'npx',
    args: ['-y', '@sentry/mcp-server', '--help'],
    timeout: 10000
  },
  {
    name: 'Heroku MCP',
    command: 'npx',
    args: ['-y', '@heroku/mcp-server', '--help'],
    timeout: 10000
  },
  {
    name: 'Supabase MCP',
    command: 'npx',
    args: ['-y', '@supabase/mcp-server-supabase', '--help'],
    timeout: 10000
  },
  {
    name: 'Apify MCP',
    command: 'npx',
    args: ['-y', '@apify/actors-mcp-server', '--help'],
    timeout: 10000
  },
  {
    name: 'HubSpot MCP',
    command: 'npx',
    args: ['-y', '@hubspot/mcp-server', '--help'],
    timeout: 10000
  },
  {
    name: 'Tavily MCP',
    command: 'npx',
    args: ['-y', 'tavily-mcp', '--help'],
    timeout: 10000
  },
  {
    name: 'Kubernetes MCP',
    command: 'npx',
    args: ['-y', 'mcp-server-kubernetes', '--help'],
    timeout: 10000
  },
  {
    name: 'Datadog MCP',
    command: 'npx',
    args: ['-y', '@winor30/mcp-server-datadog', '--help'],
    timeout: 10000
  }
];

async function testMCPServer(server) {
  return new Promise((resolve) => {
    console.log(`Testing ${server.name}...`);
    
    const process = spawn(server.command, server.args, {
      stdio: 'pipe',
      timeout: server.timeout
    });

    let output = '';
    let error = '';

    process.stdout.on('data', (data) => {
      output += data.toString();
    });

    process.stderr.on('data', (data) => {
      error += data.toString();
    });

    process.on('close', (code) => {
      if (code === 0 || output.includes('help') || output.includes('usage')) {
        console.log(`✅ ${server.name} - OK`);
        resolve({ name: server.name, status: 'success', output });
      } else {
        console.log(`❌ ${server.name} - Failed (code: ${code})`);
        resolve({ name: server.name, status: 'failed', error });
      }
    });

    process.on('error', (err) => {
      console.log(`❌ ${server.name} - Error: ${err.message}`);
      resolve({ name: server.name, status: 'error', error: err.message });
    });

    // Timeout
    setTimeout(() => {
      process.kill();
      console.log(`⏰ ${server.name} - Timeout`);
      resolve({ name: server.name, status: 'timeout' });
    }, server.timeout);
  });
}

async function testConfiguration() {
  console.log('📋 Testing MCP Server Installation...\n');
  
  const results = [];
  
  for (const server of mcpServers) {
    const result = await testMCPServer(server);
    results.push(result);
  }

  console.log('\n📊 Test Results Summary:');
  console.log('========================');
  
  const successful = results.filter(r => r.status === 'success').length;
  const failed = results.filter(r => r.status === 'failed' || r.status === 'error').length;
  const timeout = results.filter(r => r.status === 'timeout').length;
  
  console.log(`✅ Successful: ${successful}`);
  console.log(`❌ Failed: ${failed}`);
  console.log(`⏰ Timeout: ${timeout}`);
  
  if (failed > 0) {
    console.log('\n❌ Failed Servers:');
    results.filter(r => r.status === 'failed' || r.status === 'error').forEach(r => {
      console.log(`  - ${r.name}`);
    });
  }
  
  console.log('\n🔧 Configuration Files:');
  console.log('=======================');
  
  // Check configuration files
  const configFiles = [
    '/workspace/configs/cursor-settings.json',
    '/workspace/configs/environment.env'
  ];
  
  configFiles.forEach(file => {
    if (fs.existsSync(file)) {
      console.log(`✅ ${file} - Exists`);
    } else {
      console.log(`❌ ${file} - Missing`);
    }
  });
  
  console.log('\n📝 Next Steps:');
  console.log('===============');
  console.log('1. Update API keys in /workspace/configs/environment.env');
  console.log('2. Copy cursor-settings.json to your Cursor IDE configuration');
  console.log('3. Restart Cursor IDE');
  console.log('4. Test MCP servers in Cursor');
  
  console.log('\n🎉 MCP Configuration Test Complete!');
}

// Run the test
testConfiguration().catch(console.error);