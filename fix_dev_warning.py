import re

with open("index.html", "r") as f:
    html = f.read()

old_logic = """    // Show warning if on dev URL
    if (url.hostname.includes('ais-dev-')) {
      document.getElementById('dev-warning').style.display = 'block';
      // Automatically convert dev url to pre url for convenience
      url.hostname = url.hostname.replace('ais-dev-', 'ais-pre-');
    }"""

new_logic = """    // Check if running as PWA or standalone
    const isStandalone = window.matchMedia('(display-mode: standalone)').matches || window.navigator.standalone || window.matchMedia('(display-mode: window-controls-overlay)').matches || window.matchMedia('(display-mode: fullscreen)').matches || window.matchMedia('(display-mode: minimal-ui)').matches || !window.location.href.startsWith('http');
    
    // Show warning if on dev URL and not standalone
    if (url.hostname.includes('ais-dev-') && !isStandalone) {
      document.getElementById('dev-warning').style.display = 'block';
      // Automatically convert dev url to pre url for convenience
      url.hostname = url.hostname.replace('ais-dev-', 'ais-pre-');
    } else {
      document.getElementById('dev-warning').style.display = 'none';
    }
    
    if (isStandalone) {
       const syncSection = document.getElementById('unique-url-box').closest('.section-group');
       if (syncSection) syncSection.style.display = 'none';
    }"""

html = html.replace(old_logic, new_logic)

with open("index.html", "w") as f:
    f.write(html)
