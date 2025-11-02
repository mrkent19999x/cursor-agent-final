# 🎯 Hướng Dẫn Fix Viewport PWA Full Screen

## ❌ Vấn Đề Anh Gặp

- PWA bị **cắt ở trên hoặc dưới** khi mở full screen
- Có **màu xanh lòi ra** (thường là safe area hoặc status bar area)
- Viewport không chiếm hết màn hình

## ✅ Giải Pháp

### 🔴 NGUY HIỂM: Không có rủi ro cao, chỉ thay đổi CSS và meta tags

---

## 📋 Checklist Fix Viewport PWA

### 1. **Meta Viewport Tags** (Quan Trọng Nhất!)

```html
<!-- Trong <head> của index.html -->
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
```

**Giải thích:**
- `viewport-fit=cover` → Cho phép app chiếm hết màn hình (quan trọng cho iPhone có notch)
- `maximum-scale=1.0, user-scalable=no` → Tránh zoom không mong muốn

---

### 2. **iOS Safe Area Insets** (Fix Màu Xanh Lòi Ra)

**Vấn đề:** iOS Safari có notch, home indicator → cần padding cho các vùng này

**Giải pháp trong CSS:**

```css
body {
  /* Dùng safe area insets - tự động tính toán padding */
  padding: env(safe-area-inset-top) 
           env(safe-area-inset-right) 
           env(safe-area-inset-bottom) 
           env(safe-area-inset-left);
  
  /* Fallback cho iOS 11 (dùng constant thay vì env) */
  padding-top: constant(safe-area-inset-top);
  padding-right: constant(safe-area-inset-right);
  padding-bottom: constant(safe-area-inset-bottom);
  padding-left: constant(safe-area-inset-left);
}
```

**Lưu ý quan trọng:**
- `env()` cho iOS 11.2+
- `constant()` cho iOS 11.0-11.1 (cần cả 2 để tương thích)

---

### 3. **Meta Tags Cho iOS**

```html
<!-- Cho phép fullscreen trên iOS -->
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">

<!-- Theme color (màu của status bar) -->
<meta name="theme-color" content="#000000">
```

**Giải thích:**
- `black-translucent` → Status bar trong suốt, content hiển thị phía sau
- `theme-color` → Màu của status bar trên Android

---

### 4. **manifest.json Config**

```json
{
  "display": "standalone",  // ← Quan trọng! standalone = full screen
  "background_color": "#000000",
  "theme_color": "#000000"
}
```

**Các display modes:**
- `standalone` → ✅ Full screen (giống app)
- `fullscreen` → Full screen nhưng có thể gây lỗi
- `minimal-ui` → Có URL bar nhỏ
- `browser` → Mở như web bình thường

---

### 5. **CSS Fix Cho Body/HTML**

```css
html, body {
  width: 100%;
  height: 100%;
  overflow: hidden;
  /* Fix cho iOS Safari */
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
}

body {
  background-color: #000000; /* Màu này sẽ hiện ở safe area */
  /* Safe area padding */
  padding: env(safe-area-inset-top) 
           env(safe-area-inset-right) 
           env(safe-area-inset-bottom) 
           env(safe-area-inset-left);
}
```

**Giải thích:**
- `position: fixed` → Tránh scroll không mong muốn
- `overflow: hidden` → Không cho scroll body, chỉ scroll content bên trong
- Background color → Màu này sẽ hiện ở vùng safe area (thường là màu xanh lòi ra)

---

### 6. **Container Chính**

```css
#app {
  width: 100%;
  height: 100%;
  min-height: 100vh;
  min-height: -webkit-fill-available; /* iOS Safari fix */
}
```

**Giải thích:**
- `-webkit-fill-available` → Fix cho iOS Safari (chiều cao viewport)

---

## 🎨 Cấu Trúc Layout Đúng

```
┌─────────────────────────────┐
│ Safe Area Top (notch)       │ ← Padding từ env(safe-area-inset-top)
├─────────────────────────────┤
│ Header                      │
├─────────────────────────────┤
│                             │
│      Content Area           │ ← Có thể scroll
│                             │
├─────────────────────────────┤
│ Footer                      │
├─────────────────────────────┤
│ Safe Area Bottom (home bar) │ ← Padding từ env(safe-area-inset-bottom)
└─────────────────────────────┘
```

---

## 🔧 Các Fix Thường Gặp

### Fix 1: Màu Xanh Ở Trên/Dưới

**Nguyên nhân:** Background color của body khác với app

**Giải pháp:**
```css
body {
  background-color: #000000; /* Đổi thành màu giống app của bạn */
}
```

### Fix 2: Bị Cắt Ở Trên

**Nguyên nhân:** Thiếu safe area inset top

**Giải pháp:**
```css
.header {
  padding-top: calc(1rem + env(safe-area-inset-top));
}
```

### Fix 3: Bị Cắt Ở Dưới (Home Indicator)

**Nguyên nhân:** Thiếu safe area inset bottom

**Giải pháp:**
```css
.footer {
  padding-bottom: calc(1rem + env(safe-area-inset-bottom));
}
```

### Fix 4: Viewport Không Full Screen

**Nguyên nhân:** Thiếu `viewport-fit=cover` trong meta tag

**Giải pháp:**
```html
<meta name="viewport" content="viewport-fit=cover">
```

---

## 📱 Test Trên Thiết Bị Thật

### iOS Safari (iPhone)

1. Mở Safari → vào website
2. Share → Add to Home Screen
3. Mở từ Home Screen → Kiểm tra viewport

### Android Chrome

1. Mở Chrome → vào website
2. Menu → Install App
3. Mở từ app drawer → Kiểm tra viewport

---

## 🐛 Debug Safe Area

Thêm vào URL: `?debug=1` để xem safe area values:

```javascript
// Trong console hoặc script
console.log({
  top: getComputedStyle(document.documentElement)
    .getPropertyValue('env(safe-area-inset-top)'),
  bottom: getComputedStyle(document.documentElement)
    .getPropertyValue('env(safe-area-inset-bottom)')
});
```

---

## ✅ Checklist Cuối Cùng

- [ ] Meta viewport có `viewport-fit=cover`
- [ ] Meta tags iOS đầy đủ
- [ ] manifest.json có `display: "standalone"`
- [ ] Body có safe area padding (env + constant)
- [ ] Background color đúng (không bị màu xanh lòi ra)
- [ ] Header/Footer có safe area padding riêng
- [ ] Test trên iOS thật
- [ ] Test trên Android thật

---

## 📚 Tham Khảo

- [MDN: Safe Area](https://developer.mozilla.org/en-US/docs/Web/CSS/env)
- [Web.dev: PWA Viewport](https://web.dev/add-manifest/)
- [Apple: Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/macos)

---

**Chúc anh fix được viewport! 🎉**