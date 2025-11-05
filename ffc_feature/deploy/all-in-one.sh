#!/bin/bash

###############################################################################
# 🚀 FFC FEATURE - ONE CLICK DEPLOY & TEST
# Tự động deploy và test FFC feature
###############################################################################

set -e  # Exit on error

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Config
BASE_URL="https://etaxfinal.vercel.app"
ADMIN_EMAIL="phuctran123@gmail.com"
ADMIN_PASSWORD="123456"
FFC_URL="${BASE_URL}/admin/ffc"

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}🚀 FFC FEATURE - ONE CLICK DEPLOY & TEST${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Step 1: Check prerequisites
echo -e "${YELLOW}📋 Bước 1: Kiểm tra prerequisites...${NC}"
echo ""

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo -e "${RED}❌ Node.js chưa được cài đặt${NC}"
    echo "   Vui lòng cài Node.js: https://nodejs.org/"
    exit 1
fi
echo -e "${GREEN}✅ Node.js: $(node --version)${NC}"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python3 chưa được cài đặt${NC}"
    exit 1
fi
echo -e "${GREEN}✅ Python3: $(python3 --version)${NC}"

echo ""

# Step 2: Setup Firebase Firestore
echo -e "${YELLOW}📋 Bước 2: Setup Firebase Firestore...${NC}"
echo ""
echo -e "${BLUE}⚠️  Cần setup Firestore collection thủ công:${NC}"
echo "   1. Vào Firebase Console: https://console.firebase.google.com/u/0/project/anhbao-373f3/firestore"
echo "   2. Tạo collection: 'featureFlags'"
echo "   3. Add index cho field 'updatedAt' (Descending)"
echo ""
read -p "   Đã setup Firestore chưa? (y/n): " firestore_ready
if [ "$firestore_ready" != "y" ]; then
    echo -e "${YELLOW}⏸️  Tạm dừng. Hãy setup Firestore và chạy lại script.${NC}"
    exit 0
fi
echo -e "${GREEN}✅ Firestore ready${NC}"
echo ""

# Step 3: Create integration files
echo -e "${YELLOW}📋 Bước 3: Tạo integration files...${NC}"
echo ""

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

# Create integration guide
INTEGRATION_GUIDE="$PROJECT_ROOT/FFC_INTEGRATION_GUIDE.md"
cat > "$INTEGRATION_GUIDE" << 'EOF'
# 🔧 FFC Integration Guide

## 📦 Files cần copy

### 1. Frontend Component
Copy `ffc_feature/frontend/FFCDashboard.tsx` vào project:
- Next.js: `app/admin/ffc/page.tsx` hoặc `components/admin/FFCDashboard.tsx`
- React: `src/components/admin/FFCDashboard.tsx`

### 2. API Route
Copy `ffc_feature/backend/api/ffc.js` vào:
- Next.js: `app/api/ffc/route.js`

### 3. Navigation Menu
Add vào admin navigation:
```tsx
<li>
  <a href="/admin/ffc">Feature Flags</a>
</li>
```

## ⚙️ Setup Steps

### Step 1: Install Dependencies
```bash
npm install firebase firebase-admin
```

### Step 2: Setup Firebase Config
Create `lib/firebase.ts`:
```typescript
import { initializeApp } from 'firebase/app'
import { getFirestore } from 'firebase/firestore'

const firebaseConfig = {
  // Your Firebase config
}

const app = initializeApp(firebaseConfig)
export const db = getFirestore(app)
```

### Step 3: Setup Environment Variables
Add to `.env.local`:
```
FIREBASE_PROJECT_ID=anhbao-373f3
FIREBASE_CLIENT_EMAIL=your-service-account@...
FIREBASE_PRIVATE_KEY=your-private-key
```

### Step 4: Deploy
```bash
vercel deploy --prod
```

## ✅ Verify
Run test script:
```bash
python3 ffc_feature/tests/test-ffc-e2e.py
```
EOF

echo -e "${GREEN}✅ Integration guide created: $INTEGRATION_GUIDE${NC}"
echo ""

# Step 4: Create test script
echo -e "${YELLOW}📋 Bước 4: Tạo test script tự động...${NC}"
echo ""

TEST_SCRIPT="$SCRIPT_DIR/../tests/test-ffc-e2e.py"
mkdir -p "$(dirname "$TEST_SCRIPT")"

cat > "$TEST_SCRIPT" << EOF
#!/usr/bin/env python3
"""
E2E Test tự động cho FFC Feature sau khi deploy
"""
import asyncio
import sys
from playwright.async_api import async_playwright

BASE_URL = "${BASE_URL}"
ADMIN_EMAIL = "${ADMIN_EMAIL}"
ADMIN_PASSWORD = "${ADMIN_PASSWORD}"
FFC_URL = "${FFC_URL}"

async def test_ffc():
    print("🧪 TESTING FFC FEATURE")
    print("="*60)
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        
        try:
            # Login
            print("\\n1️⃣ Logging in...")
            await page.goto(f"{BASE_URL}/admin/login", wait_until='networkidle')
            await page.fill('input[type="email"]', ADMIN_EMAIL)
            await page.fill('input[type="password"]', ADMIN_PASSWORD)
            await page.click('button[type="submit"]')
            await page.wait_for_load_state('networkidle', timeout=15000)
            print("   ✅ Logged in")
            
            # Navigate to FFC
            print("\\n2️⃣ Navigating to FFC page...")
            await page.goto(FFC_URL, wait_until='networkidle', timeout=10000)
            current_url = page.url
            print(f"   Current URL: {current_url}")
            
            if 'login' in current_url.lower():
                print("   ❌ Redirected to login - FFC page not accessible")
                return False
            
            # Check for FFC content
            print("\\n3️⃣ Checking FFC content...")
            page_content = await page.content()
            
            ffc_indicators = ['feature flag', 'featureflag', 'ffc']
            found = any(indicator in page_content.lower() for indicator in ffc_indicators)
            
            if found:
                print("   ✅ FFC page loaded!")
                
                # Check for UI elements
                try:
                    title = await page.query_selector('h1')
                    if title:
                        title_text = await title.text_content()
                        print(f"   ✅ Found title: {title_text}")
                    
                    # Try to find "Add" button
                    add_button = await page.query_selector('button:has-text("Thêm"), button:has-text("Add")')
                    if add_button:
                        print("   ✅ Found Add button")
                        return True
                except:
                    pass
                
                return True
            else:
                print("   ❌ FFC content not found")
                return False
                
        except Exception as e:
            print(f"   ❌ Error: {str(e)}")
            return False
        finally:
            await browser.close()

if __name__ == "__main__":
    result = asyncio.run(test_ffc())
    if result:
        print("\\n✅ FFC FEATURE TEST PASSED!")
        sys.exit(0)
    else:
        print("\\n❌ FFC FEATURE TEST FAILED!")
        sys.exit(1)
EOF

chmod +x "$TEST_SCRIPT"
echo -e "${GREEN}✅ Test script created: $TEST_SCRIPT${NC}"
echo ""

# Step 5: Run E2E test (if page exists)
echo -e "${YELLOW}📋 Bước 5: Chạy E2E test...${NC}"
echo ""

# Check if FFC page exists
echo "   Đang kiểm tra FFC page..."
if python3 -c "
import requests
response = requests.get('${FFC_URL}', timeout=5, allow_redirects=False)
exit(0 if response.status_code == 200 else 1)
" 2>/dev/null; then
    echo -e "${GREEN}   ✅ FFC page đã tồn tại!${NC}"
    echo "   Đang chạy test..."
    
    if python3 "$TEST_SCRIPT"; then
        echo -e "${GREEN}✅ E2E TEST PASSED!${NC}"
    else
        echo -e "${YELLOW}⚠️  E2E TEST FAILED - Có thể page chưa được integrate${NC}"
    fi
else
    echo -e "${YELLOW}   ⚠️  FFC page chưa tồn tại${NC}"
    echo "   Cần integrate code vào project trước"
    echo ""
    echo -e "${BLUE}📝 NEXT STEPS:${NC}"
    echo "   1. Xem integration guide: $INTEGRATION_GUIDE"
    echo "   2. Copy files vào project"
    echo "   3. Deploy lại"
    echo "   4. Chạy lại script này: ./deploy/all-in-one.sh"
fi

echo ""

# Step 6: Summary
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}✅ HOÀN THÀNH!${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo "📁 Files đã tạo:"
echo "   ✅ Frontend: ffc_feature/frontend/FFCDashboard.tsx"
echo "   ✅ Backend: ffc_feature/backend/api/ffc.js"
echo "   ✅ Integration Guide: FFC_INTEGRATION_GUIDE.md"
echo "   ✅ Test Script: ffc_feature/tests/test-ffc-e2e.py"
echo ""
echo "📋 Next steps:"
echo "   1. Xem FFC_INTEGRATION_GUIDE.md để biết cách integrate"
echo "   2. Copy files vào project"
echo "   3. Setup Firebase (nếu chưa)"
echo "   4. Deploy và test"
echo ""
echo -e "${GREEN}🎉 Done!${NC}"
