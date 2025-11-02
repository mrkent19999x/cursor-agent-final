# ⚡ Quick Fix - Copy Paste Ngay

## 1️⃣ Copy Meta Tags Vào `<head>`

```html
<!-- Viewport với viewport-fit=cover -->
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">

<!-- PWA & iOS Meta -->
<meta name="theme-color" content="#000000">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
```

## 2️⃣ Copy CSS Vào File CSS Của Bạn

```css
html, body {
  width: 100%;
  height: 100%;
  overflow: hidden;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
}

body {
  background-color: #000000; /* Đổi thành màu app của bạn */
  padding: env(safe-area-inset-top) 
           env(safe-area-inset-right) 
           env(safe-area-inset-bottom) 
           env(safe-area-inset-left);
  padding-top: constant(safe-area-inset-top);
  padding-right: constant(safe-area-inset-right);
  padding-bottom: constant(safe-area-inset-bottom);
  padding-left: constant(safe-area-inset-left);
}

#app {
  width: 100%;
  height: 100%;
  min-height: 100vh;
  min-height: -webkit-fill-available;
}
```

## 3️⃣ Sửa Header/Footer

```css
/* Header */
.header {
  padding-top: calc(1rem + env(safe-area-inset-top));
  padding-top: calc(1rem + constant(safe-area-inset-top));
}

/* Footer */
.footer {
  padding-bottom: calc(1rem + env(safe-area-inset-bottom));
  padding-bottom: calc(1rem + constant(safe-area-inset-bottom));
}
```

## 4️⃣ Sửa manifest.json

```json
{
  "display": "standalone",
  "background_color": "#000000",
  "theme_color": "#000000"
}
```

## ✅ Xong! Test lại thôi!