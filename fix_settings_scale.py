import re

with open("index.html", "r") as f:
    html = f.read()

old_fit_logic = """      let s = 1;
      if (measureH > availH) s = Math.min(s, availH / measureH);
      if (measureW > availW) s = Math.min(s, availW / measureW);
      s = Math.max(0.1, Math.min(1, s));"""

new_fit_logic = """      let s = 1;
      if (view.id !== 'view-style') {
          if (scaleFit && measureH > availH) s = Math.min(s, availH / measureH);
      }
      if (measureW > availW) s = Math.min(s, availW / measureW);
      s = Math.max(0.1, Math.min(1, s));"""

html = html.replace(old_fit_logic, new_fit_logic)

with open("index.html", "w") as f:
    f.write(html)
