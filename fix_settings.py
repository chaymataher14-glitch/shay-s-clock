import re

with open("index.html", "r") as f:
    html = f.read()

# Fix fit() function
old_fit = """      let s = 1;
      if (scaleFit && measureH > availH) s = Math.min(s, availH / measureH);
      if (measureW > availW) s = Math.min(s, availW / measureW);
      s = Math.max(0.1, Math.min(1, s));"""

new_fit = """      let s = 1;
      if (view.id !== 'view-style') {
          if (scaleFit && measureH > availH) s = Math.min(s, availH / measureH);
      }
      if (measureW > availW) s = Math.min(s, availW / measureW);
      s = Math.max(0.1, Math.min(1, s));"""

html = html.replace(old_fit, new_fit)

# Fix max-widths for settings so they are constrained nicely
html = html.replace('width: 100%; max-width: 100%;', 'width: 100%; max-width: min(calc(600px * var(--auto-scale, 1)), 100%);')

with open("index.html", "w") as f:
    f.write(html)
