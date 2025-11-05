# 🔧 FFC FEATURE - INTEGRATION GUIDE

**Hoàn chỉnh, tự động, sẵn sàng deploy!**

---

## 📦 FILES CẦN COPY

### 1. Frontend Component
**File:** `ffc_feature/frontend/FFCDashboard.tsx`

**Copy vào:**
- Next.js App Router: `app/admin/ffc/page.tsx`
- Next.js Pages Router: `pages/admin/ffc.tsx`
- React App: `src/components/admin/FFCDashboard.tsx`

### 2. Backend API
**File:** `ffc_feature/backend/api/ffc.js`

**Copy vào:**
- Next.js App Router: `app/api/ffc/route.js` (export GET, POST, PUT, DELETE)
- Next.js Pages Router: `pages/api/ffc.js` hoặc `pages/api/ffc/index.js`

### 3. Navigation Menu
Add vào admin navigation component (thường ở `components/admin/Navigation.tsx` hoặc tương tự):

```tsx
<li>
  <a href="/admin/ffc">Feature Flags</a>
</li>
```

---

## ⚙️ SETUP STEPS (Tự động)

### Option 1: Auto Setup Script (Recommended)

```bash
cd ffc_feature
chmod +x deploy/all-in-one.sh
./deploy/all-in-one.sh
```

**Script sẽ tự động:**
1. ✅ Check prerequisites
2. ✅ Guide setup Firebase
3. ✅ Create integration files
4. ✅ Run tests

### Option 2: Manual Setup

#### Step 1: Install Dependencies

```bash
npm install firebase firebase-admin
# hoặc
yarn add firebase firebase-admin
```

#### Step 2: Setup Firebase Client (Frontend)

Create hoặc update `lib/firebase.ts` hoặc `config/firebase.ts`:

```typescript
import { initializeApp } from 'firebase/app'
import { getFirestore } from 'firebase/firestore'
import { getAuth } from 'firebase/auth'

const firebaseConfig = {
  apiKey: process.env.NEXT_PUBLIC_FIREBASE_API_KEY,
  authDomain: process.env.NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN,
  projectId: process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID,
  storageBucket: process.env.NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET,
  messagingSenderId: process.env.NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID,
  appId: process.env.NEXT_PUBLIC_FIREBASE_APP_ID
}

const app = initializeApp(firebaseConfig)
export const db = getFirestore(app)
export const auth = getAuth(app)
```

#### Step 3: Setup Firebase Admin (Backend)

Create hoặc update `lib/firebase-admin.ts`:

```typescript
import { initializeApp, getApps, cert } from 'firebase-admin/app'
import { getFirestore } from 'firebase-admin/firestore'

if (!getApps().length) {
  initializeApp({
    credential: cert({
      projectId: process.env.FIREBASE_PROJECT_ID,
      clientEmail: process.env.FIREBASE_CLIENT_EMAIL,
      privateKey: process.env.FIREBASE_PRIVATE_KEY?.replace(/\\n/g, '\n')
    })
  })
}

export const adminDb = getFirestore()
```

#### Step 4: Environment Variables

Add to `.env.local` hoặc Vercel Environment Variables:

```env
# Firebase Client (Public)
NEXT_PUBLIC_FIREBASE_API_KEY=your-api-key
NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN=anhbao-373f3.firebaseapp.com
NEXT_PUBLIC_FIREBASE_PROJECT_ID=anhbao-373f3
NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET=anhbao-373f3.appspot.com
NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID=your-sender-id
NEXT_PUBLIC_FIREBASE_APP_ID=your-app-id

# Firebase Admin (Private)
FIREBASE_PROJECT_ID=anhbao-373f3
FIREBASE_CLIENT_EMAIL=your-service-account@...
FIREBASE_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n"
```

**Lấy Firebase config:**
1. Vào Firebase Console: https://console.firebase.google.com/u/0/project/anhbao-373f3/settings/general
2. Scroll xuống "Your apps" > Web app > Config
3. Copy các giá trị

**Lấy Service Account (cho Admin):**
1. Vào Firebase Console > Project Settings > Service Accounts
2. Click "Generate new private key"
3. Download JSON file
4. Copy các giá trị vào `.env.local`

#### Step 5: Setup Firestore Collection

1. Vào Firebase Console > Firestore Database
2. Click "Start collection"
3. Collection ID: `featureFlags`
4. Document ID: Auto-generated
5. Add first document (optional):
   - Field: `name` (string) - "example_flag"
   - Field: `description` (string) - "Example feature flag"
   - Field: `enabled` (boolean) - true
   - Field: `tags` (array) - ["example"]
   - Field: `createdAt` (string) - ISO timestamp
   - Field: `updatedAt` (string) - ISO timestamp
   - Field: `createdBy` (string) - "admin"

6. Setup Indexes (optional but recommended):
   - Collection: `featureFlags`
   - Field: `updatedAt` (Descending)

#### Step 6: Create Admin Page

**Next.js App Router:**
Create `app/admin/ffc/page.tsx`:

```typescript
import FFCDashboard from '@/components/admin/FFCDashboard'
// hoặc import từ file đã copy

export default function FFCPage() {
  return <FFCDashboard />
}
```

**Next.js Pages Router:**
Create `pages/admin/ffc.tsx`:

```typescript
import FFCDashboard from '@/components/admin/FFCDashboard'

export default function FFCPage() {
  return <FFCDashboard />
}
```

#### Step 7: Add to Navigation

Find navigation component (thường ở `components/admin/Navigation.tsx` hoặc `components/layout/AdminNav.tsx`):

Add link:
```tsx
<li>
  <a href="/admin/ffc" className="nav-link">
    Feature Flags
  </a>
</li>
```

#### Step 8: Deploy

```bash
# Local test
npm run dev

# Deploy to Vercel
vercel deploy --prod

# hoặc push to GitHub (nếu đã setup Vercel auto-deploy)
git push origin main
```

---

## 🧪 TESTING

### Auto Test:
```bash
cd ffc_feature/tests
python3 test-ffc-e2e.py
```

### Manual Test:
1. Login vào admin: https://etaxfinal.vercel.app/admin/login
2. Navigate to: https://etaxfinal.vercel.app/admin/ffc
3. Check:
   - ✅ Page loads without errors
   - ✅ "Add Feature Flag" button visible
   - ✅ Can create new flag
   - ✅ Can toggle enable/disable
   - ✅ Can edit flag
   - ✅ Can delete flag

---

## 🐛 TROUBLESHOOTING

### Issue: "Firebase not initialized"
**Fix:** Check Firebase config in `lib/firebase.ts`

### Issue: "Permission denied" trong Firestore
**Fix:** Check Firestore Security Rules - allow admin read/write

### Issue: Page 404
**Fix:** 
1. Check route exists: `app/admin/ffc/page.tsx`
2. Check navigation link points to `/admin/ffc`
3. Rebuild and redeploy

### Issue: "Module not found: firebase"
**Fix:** 
```bash
npm install firebase firebase-admin
```

### Issue: Environment variables not working
**Fix:**
1. Check `.env.local` exists (local)
2. Check Vercel Environment Variables (production)
3. Restart dev server after changing `.env.local`
4. Redeploy after changing Vercel env vars

---

## ✅ CHECKLIST

- [ ] Firebase config added to `.env.local`
- [ ] Firebase Admin config added
- [ ] Firestore collection `featureFlags` created
- [ ] Frontend component copied
- [ ] API route copied
- [ ] Navigation link added
- [ ] Page route created (`/admin/ffc`)
- [ ] Dependencies installed
- [ ] Local test passed
- [ ] Deployed to production
- [ ] E2E test passed

---

## 📞 SUPPORT

Nếu có vấn đề:
1. Check troubleshooting section
2. Run E2E test: `python3 ffc_feature/tests/test-ffc-e2e.py`
3. Check browser console for errors
4. Check Vercel logs
5. Check Firebase logs

---

**Created by:** Cipher AI Assistant  
**Status:** ✅ Production Ready  
**Last Updated:** 2025-11-02
