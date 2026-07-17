import re

with open("index.html", "r") as f:
    html = f.read()

head_additions = """<link rel="manifest" href="./manifest.json">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Focus App">
<link rel="apple-touch-icon" href="./icon.svg">"""

if '<link rel="manifest"' not in html:
    html = html.replace('</head>', head_additions + '\n</head>')

sw_registration = """<script>
  if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
      navigator.serviceWorker.register('./sw.js').then(registration => {
        console.log('SW registered: ', registration);
      }).catch(registrationError => {
        console.log('SW registration failed: ', registrationError);
      });
    });
  }
</script>"""

if 'serviceWorker' not in html:
    html = html.replace('</body>', sw_registration + '\n</body>')

with open("index.html", "w") as f:
    f.write(html)
