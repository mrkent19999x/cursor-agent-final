/**
 * PWA Viewport Fix JavaScript Helper
 * Các hàm utility để fix viewport và safe area
 */

// ============================================
// 1. PREVENT PULL-TO-REFRESH
// ============================================
(function preventPullToRefresh() {
  let lastTouchY = 0;
  
  document.addEventListener('touchstart', (e) => {
    if (e.touches.length !== 1) return;
    lastTouchY = e.touches[0].clientY;
  }, { passive: true });
  
  document.addEventListener('touchmove', (e) => {
    if (e.touches.length !== 1) return;
    
    const touchY = e.touches[0].clientY;
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    const scrollHeight = document.documentElement.scrollHeight;
    const clientHeight = document.documentElement.clientHeight;
    
    // Nếu đang ở top và kéo xuống -> prevent
    if (scrollTop === 0 && touchY > lastTouchY) {
      e.preventDefault();
      return false;
    }
    
    // Nếu đang ở bottom và kéo lên -> prevent
    if (scrollTop + clientHeight >= scrollHeight - 1 && touchY < lastTouchY) {
      e.preventDefault();
      return false;
    }
    
    lastTouchY = touchY;
  }, { passive: false });
})();

// ============================================
// 2. SET VIEWPORT HEIGHT (Fix iOS Safari)
// ============================================
(function setViewportHeight() {
  const setHeight = () => {
    const vh = window.innerHeight * 0.01;
    document.documentElement.style.setProperty('--vh', `${vh}px`);
  };
  
  setHeight();
  window.addEventListener('resize', setHeight);
  window.addEventListener('orientationchange', () => {
    setTimeout(setHeight, 100);
  });
})();

// Sử dụng trong CSS: height: calc(var(--vh, 1vh) * 100);

// ============================================
// 3. GET SAFE AREA VALUES (Debug)
// ============================================
function getSafeAreaValues() {
  const style = getComputedStyle(document.documentElement);
  return {
    top: style.getPropertyValue('env(safe-area-inset-top)') || 
         style.getPropertyValue('constant(safe-area-inset-top)') || '0px',
    bottom: style.getPropertyValue('env(safe-area-inset-bottom)') || 
            style.getPropertyValue('constant(safe-area-inset-bottom)') || '0px',
    left: style.getPropertyValue('env(safe-area-inset-left)') || 
          style.getPropertyValue('constant(safe-area-inset-left)') || '0px',
    right: style.getPropertyValue('env(safe-area-inset-right)') || 
           style.getPropertyValue('constant(safe-area-inset-right)') || '0px',
    viewportWidth: window.innerWidth,
    viewportHeight: window.innerHeight,
    screenWidth: window.screen.width,
    screenHeight: window.screen.height,
    devicePixelRatio: window.devicePixelRatio
  };
}

// ============================================
// 4. DEBUG MODE
// ============================================
if (window.location.search.includes('debug=1')) {
  const debugInfo = document.createElement('div');
  debugInfo.id = 'viewport-debug-info';
  debugInfo.style.cssText = `
    position: fixed;
    top: 10px;
    left: 10px;
    background: rgba(0, 0, 0, 0.8);
    color: #fff;
    padding: 10px;
    font-size: 12px;
    font-family: monospace;
    z-index: 99999;
    max-width: 300px;
    border-radius: 4px;
  `;
  document.body.appendChild(debugInfo);
  
  const updateDebug = () => {
    const info = getSafeAreaValues();
    debugInfo.innerHTML = `
      <div><strong>Safe Areas:</strong></div>
      <div>Top: ${info.top}</div>
      <div>Bottom: ${info.bottom}</div>
      <div>Left: ${info.left}</div>
      <div>Right: ${info.right}</div>
      <div style="margin-top: 10px;"><strong>Viewport:</strong></div>
      <div>${info.viewportWidth} x ${info.viewportHeight}</div>
      <div>Screen: ${info.screenWidth} x ${info.screenHeight}</div>
      <div>DPR: ${info.devicePixelRatio}</div>
    `;
  };
  
  updateDebug();
  window.addEventListener('resize', updateDebug);
  window.addEventListener('orientationchange', () => {
    setTimeout(updateDebug, 100);
  });
}

// ============================================
// 5. REGISTER SERVICE WORKER
// ============================================
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('/sw.js')
      .then(reg => {
        console.log('✅ Service Worker registered:', reg);
      })
      .catch(err => {
        console.log('❌ Service Worker registration failed:', err);
      });
  });
}

// ============================================
// 6. EXPORT (Nếu dùng module)
// ============================================
if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
    getSafeAreaValues,
    preventPullToRefresh: true // Đã chạy tự động
  };
}