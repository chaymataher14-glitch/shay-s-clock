import re

with open("index.html", "r") as f:
    html = f.read()

old_swipe = """  document.addEventListener('wheel', (e) => {
    if (!document.getElementById('swipe-nav-toggle').checked) return;
    const now = Date.now();
    if (now - lastSwipeTime > 300) {
      swipeAccumulator = 0;
    }
    lastSwipeTime = now;
    
    // Only care if vertical scroll is dominant
    if (Math.abs(e.deltaY) > Math.abs(e.deltaX)) {
      swipeAccumulator += e.deltaY;
      // Use a smaller threshold to make it feel responsive
      if (Math.abs(swipeAccumulator) > 50) {
        cycleTabs(swipeAccumulator > 0 ? 1 : -1);
        swipeAccumulator = 0;
        lastSwipeTime = now + 400; // Cooldown to prevent multiple tab switches in one swipe
      }
    }
  }, { passive: true });

  let touchStartY = 0;
  let touchStartX = 0;
  let lastTouchTime = 0;
  
  // Also support 1-finger or 2-finger swipe on touch devices if no scroll is happening
  document.addEventListener('touchstart', (e) => {
    if (!document.getElementById('swipe-nav-toggle').checked) return;
    // We can allow both 1 or 2 fingers, user asked for "finger swiping up and down"
    touchStartY = e.touches[0].clientY;
    touchStartX = e.touches[0].clientX;
  }, { passive: true });

  document.addEventListener('touchmove', (e) => {
    if (!document.getElementById('swipe-nav-toggle').checked) return;
    const currentY = e.touches[0].clientY;
    const currentX = e.touches[0].clientX;
    const deltaY = touchStartY - currentY;
    const deltaX = touchStartX - currentX;
    
    const now = Date.now();
    if (now - lastTouchTime < 500) return; // Cooldown
    
    // Ensure it's a vertical swipe
    if (Math.abs(deltaY) > Math.abs(deltaX) && Math.abs(deltaY) > 50) {
       cycleTabs(deltaY > 0 ? 1 : -1);
       lastTouchTime = now;
       touchStartY = currentY; // Reset
    }
  }, { passive: true });"""

new_swipe = """  function isScrollable(el) {
    while (el && el !== document.body && el !== document.documentElement) {
      if (el.scrollHeight > el.clientHeight) {
         const overflowY = window.getComputedStyle(el).overflowY;
         if (overflowY === 'auto' || overflowY === 'scroll') {
             return true;
         }
      }
      el = el.parentElement;
    }
    return false;
  }

  document.addEventListener('wheel', (e) => {
    if (!document.getElementById('swipe-nav-toggle').checked) return;
    if (isScrollable(e.target)) return;

    const now = Date.now();
    if (now - lastSwipeTime > 300) {
      swipeAccumulator = 0;
    }
    lastSwipeTime = now;
    
    // Only care if vertical scroll is dominant
    if (Math.abs(e.deltaY) > Math.abs(e.deltaX)) {
      swipeAccumulator += e.deltaY;
      if (Math.abs(swipeAccumulator) > 60) {
        cycleTabs(swipeAccumulator > 0 ? 1 : -1);
        swipeAccumulator = 0;
        lastSwipeTime = now + 400; 
      }
    }
  }, { passive: true });

  let touchStartY = 0;
  let touchStartX = 0;
  let lastTouchTime = 0;
  
  document.addEventListener('touchstart', (e) => {
    if (!document.getElementById('swipe-nav-toggle').checked) return;
    touchStartY = e.touches[0].clientY;
    touchStartX = e.touches[0].clientX;
  }, { passive: true });

  document.addEventListener('touchmove', (e) => {
    if (!document.getElementById('swipe-nav-toggle').checked) return;
    if (isScrollable(e.target)) return;
    
    const currentY = e.touches[0].clientY;
    const currentX = e.touches[0].clientX;
    const deltaY = touchStartY - currentY;
    const deltaX = touchStartX - currentX;
    
    const now = Date.now();
    if (now - lastTouchTime < 500) return;
    
    if (Math.abs(deltaY) > Math.abs(deltaX) && Math.abs(deltaY) > 50) {
       cycleTabs(deltaY > 0 ? 1 : -1);
       lastTouchTime = now;
       touchStartY = currentY; 
    }
  }, { passive: true });"""

html = html.replace(old_swipe, new_swipe)

with open("index.html", "w") as f:
    f.write(html)
