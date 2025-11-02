#!/usr/bin/env python3
"""
Local Test Server để verify FFC Feature hoạt động
Sử dụng để test mà không cần deploy thật
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import urllib.parse

# Mock Firebase data
mock_feature_flags = [
    {
        'id': '1',
        'name': 'enable_new_ui',
        'description': 'Bật giao diện mới',
        'enabled': True,
        'tags': ['ui', 'experimental'],
        'createdAt': '2025-11-02T10:00:00Z',
        'updatedAt': '2025-11-02T19:00:00Z',
        'createdBy': 'admin'
    },
    {
        'id': '2',
        'name': 'enable_payment',
        'description': 'Bật tính năng thanh toán',
        'enabled': False,
        'tags': ['payment', 'production'],
        'createdAt': '2025-11-02T11:00:00Z',
        'updatedAt': '2025-11-02T12:00:00Z',
        'createdBy': 'admin'
    }
]

class FFCRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Handle GET requests"""
        if self.path == '/admin/ffc' or self.path == '/admin/ffc/':
            self.send_ffc_page()
        elif self.path == '/api/ffc':
            self.send_ffc_api()
        elif self.path == '/admin/login':
            self.send_login_page()
        elif self.path == '/admin':
            self.send_admin_dashboard()
        else:
            self.send_error(404)
    
    def do_POST(self):
        """Handle POST requests"""
        if self.path == '/api/ffc':
            self.handle_ffc_post()
        elif self.path == '/api/login':
            self.handle_login()
        else:
            self.send_error(404)
    
    def send_ffc_page(self):
        """Send FFC dashboard HTML"""
        html = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Feature Flags Management</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100">
    <div class="container mx-auto px-4 py-8">
        <div class="flex justify-between items-center mb-6">
            <h1 class="text-3xl font-bold">Feature Flags Management</h1>
            <button id="addBtn" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
                + Thêm Feature Flag
            </button>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
            <div class="bg-white p-4 rounded shadow">
                <div class="text-gray-600">Tổng số Flags</div>
                <div id="totalFlags" class="text-2xl font-bold">0</div>
            </div>
            <div class="bg-green-50 p-4 rounded shadow">
                <div class="text-green-700">Đang bật</div>
                <div id="enabledFlags" class="text-2xl font-bold text-green-600">0</div>
            </div>
            <div class="bg-red-50 p-4 rounded shadow">
                <div class="text-red-700">Đang tắt</div>
                <div id="disabledFlags" class="text-2xl font-bold text-red-600">0</div>
            </div>
        </div>
        
        <div class="bg-white rounded shadow overflow-hidden">
            <table class="min-w-full">
                <thead class="bg-gray-50">
                    <tr>
                        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Tên</th>
                        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Mô tả</th>
                        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Tags</th>
                        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Trạng thái</th>
                        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Thao tác</th>
                    </tr>
                </thead>
                <tbody id="flagsTable" class="divide-y divide-gray-200">
                    <!-- Filled by JavaScript -->
                </tbody>
            </table>
        </div>
    </div>
    
    <script>
        async function loadFlags() {
            const response = await fetch('/api/ffc');
            const data = await response.json();
            const flags = data.data || [];
            
            // Update stats
            document.getElementById('totalFlags').textContent = flags.length;
            document.getElementById('enabledFlags').textContent = flags.filter(f => f.enabled).length;
            document.getElementById('disabledFlags').textContent = flags.filter(f => !f.enabled).length;
            
            // Update table
            const tbody = document.getElementById('flagsTable');
            tbody.innerHTML = flags.map(flag => `
                <tr class="hover:bg-gray-50">
                    <td class="px-6 py-4 whitespace-nowrap font-medium">${flag.name}</td>
                    <td class="px-6 py-4">${flag.description || ''}</td>
                    <td class="px-6 py-4">
                        <div class="flex gap-2">
                            ${flag.tags.map(tag => `<span class="bg-gray-100 px-2 py-1 rounded text-xs">${tag}</span>`).join('')}
                        </div>
                    </td>
                    <td class="px-6 py-4">
                        <button class="px-3 py-1 rounded text-sm font-medium ${flag.enabled ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'}">
                            ${flag.enabled ? 'Đang bật' : 'Đang tắt'}
                        </button>
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap">
                        <button class="text-blue-600 hover:text-blue-800 mr-4">Sửa</button>
                        <button class="text-red-600 hover:text-red-800">Xóa</button>
                    </td>
                </tr>
            `).join('');
        }
        
        window.onload = () => loadFlags();
    </script>
</body>
</html>"""
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(html.encode('utf-8'))
    
    def send_ffc_api(self):
        """Send FFC API response"""
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        response = {
            'success': True,
            'data': mock_feature_flags
        }
        self.wfile.write(json.dumps(response).encode('utf-8'))
    
    def handle_ffc_post(self):
        """Handle FFC POST request"""
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode('utf-8'))
        
        # Add new flag
        new_flag = {
            'id': str(len(mock_feature_flags) + 1),
            **data,
            'createdAt': '2025-11-02T19:00:00Z',
            'updatedAt': '2025-11-02T19:00:00Z',
            'createdBy': 'admin'
        }
        mock_feature_flags.append(new_flag)
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps({'success': True, 'data': new_flag}).encode('utf-8'))
    
    def send_login_page(self):
        """Send login page"""
        html = """<!DOCTYPE html>
<html>
<head>
    <title>Admin Login</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 flex items-center justify-center min-h-screen">
    <div class="bg-white p-8 rounded shadow">
        <h1 class="text-2xl font-bold mb-4">Admin Login</h1>
        <form method="POST" action="/api/login">
            <input type="email" name="email" placeholder="Email" class="w-full border rounded px-3 py-2 mb-4" required>
            <input type="password" name="password" placeholder="Password" class="w-full border rounded px-3 py-2 mb-4" required>
            <button type="submit" class="w-full bg-blue-500 text-white py-2 rounded hover:bg-blue-600">Login</button>
        </form>
    </div>
</body>
</html>"""
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(html.encode('utf-8'))
    
    def send_admin_dashboard(self):
        """Send admin dashboard"""
        html = """<!DOCTYPE html>
<html>
<head>
    <title>Admin Dashboard</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100">
    <nav class="bg-white shadow mb-4">
        <div class="container mx-auto px-4 py-2">
            <a href="/admin/ffc" class="text-blue-600 hover:text-blue-800">Feature Flags</a>
        </div>
    </nav>
    <div class="container mx-auto px-4 py-8">
        <h1 class="text-3xl font-bold">Admin Dashboard</h1>
    </div>
</body>
</html>"""
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(html.encode('utf-8'))
    
    def handle_login(self):
        """Handle login"""
        self.send_response(302)
        self.send_header('Location', '/admin')
        self.end_headers()
    
    def log_message(self, format, *args):
        """Override to suppress default logging"""
        pass

def run_server(port=8000):
    """Run test server"""
    server = HTTPServer(('localhost', port), FFCRequestHandler)
    print(f"🚀 Test server running on http://localhost:{port}")
    print(f"📄 FFC Page: http://localhost:{port}/admin/ffc")
    print(f"🔌 API: http://localhost:{port}/api/ffc")
    print("\nPress Ctrl+C to stop")
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n\n✅ Server stopped")
        server.server_close()

if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    run_server(port)
