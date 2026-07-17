import re

with open("index.html", "r") as f:
    html = f.read()

html = re.sub(r'\.section-group \{ width: 100%; max-width: min\(calc\(420px \* var\(--auto-scale, 1\)\), 100%\);', r'.section-group { width: 100%; max-width: min(500px, 100%);', html)
html = re.sub(r'\.style-row \{ width: 100%; max-width: min\(calc\(420px \* var\(--auto-scale, 1\)\), 100%\);', r'.style-row { width: 100%; max-width: min(500px, 100%);', html)

with open("index.html", "w") as f:
    f.write(html)
