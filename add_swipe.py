import re

with open("index.html", "r") as f:
    html = f.read()

swipe_js = """
  // Swipe to Navigate Tabs (2-finger swipe / Wheel)
  let swipeAccumulator = 0;
  let lastSwipeTime = 0;
  
  function cycleTabs(direction) {
    const tabs = Array.from(document.querySelectorAll('.side-tab'));
    if (!tabs.length) return;
    let activeIdx = tabs.findIndex(tab => tab.classList.contains('active'));
    if (activeIdx === -1) activeIdx = 0;
    let nextIdx = activeIdx + direction;
    if (nextIdx < 0) nextIdx = tabs.length - 1;
    if (nextIdx >= tabs.length) nextIdx = 0;
    tabs[nextIdx].click();
  }

  document.addEventListener('wheel', (e) => {
    let el = e.target;
    let canScroll = false;
    while (el && el !== document.body && el !== document.documentElement) {
      if (el.scrollHeight > el.clientHeight) {
         const overflowY = window.getComputedStyle(el).overflowY;
         if (overflowY === 'auto' || overflowY === 'scroll') {
             // Only consider it scrollable if there is actual content to scroll
             // and we are not at the very top trying to scroll up, etc.
             canScroll = true;
             break;
         }
      }
      el = el.parentElement;
    }

    if (canScroll) return; // Prevent tab switch if scrolling in a scrollable area

    const now = Date.now();
    if (now - lastSwipeTime > 300) {
      swipeAccumulator = 0;
    }
    lastSwipeTime = now;
    
    // Only care if vertical scroll is dominant
    if (Math.abs(e.deltaY) > Math.abs(e.deltaX)) {
      swipeAccumulator += e.deltaY;
      if (Math.abs(swipeAccumulator) > 150) {
        cycleTabs(swipeAccumulator > 0 ? 1 : -1);
        swipeAccumulator = 0;
        lastSwipeTime = now + 400; // Cooldown
      }
    }
  }, { passive: true });

  let touchStartY = 0;
  let touchStartX = 0;
  let lastTouchTime = 0;
  
  document.addEventListener('touchstart', (e) => {
    if (e.touches.length === 2) {
      touchStartY = e.touches[0].clientY;
      touchStartX = e.touches[0].clientX;
    }
  }, { passive: true });

  document.addEventListener('touchmove', (e) => {
    if (e.touches.length === 2) {
      const currentY = e.touches[0].clientY;
      const currentX = e.touches[0].clientX;
      const deltaY = touchStartY - currentY;
      const deltaX = touchStartX - currentX;
      
      const now = Date.now();
      if (now - lastTouchTime < 500) return; // Cooldown
      
      if (Math.abs(deltaY) > Math.abs(deltaX) && Math.abs(deltaY) > 40) {
         cycleTabs(deltaY > 0 ? 1 : -1);
         lastTouchTime = now;
         touchStartY = currentY; // Reset
      }
    }
  }, { passive: true });
"""

html = html.replace('// --- INITIALIZATION ORDER ---', swipe_js + '\n  // --- INITIALIZATION ORDER ---')

with open("index.html", "w") as f:
    f.write(html)
