import re

with open("index.html", "r") as f:
    html = f.read()

html = re.sub(r'max-width: min\(calc\(420px \* var\(--auto-scale, 1\)\), 100%\);', r'max-width: min(500px, 100%);', html)

with open("index.html", "w") as f:
    f.write(html)
