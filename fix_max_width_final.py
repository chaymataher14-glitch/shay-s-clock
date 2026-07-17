import re

with open("index.html", "r") as f:
    html = f.read()

html = html.replace('width: 100%; max-width: 100%;', 'width: 100%; max-width: min(calc(500px * var(--auto-scale, 1)), 100%);')

with open("index.html", "w") as f:
    f.write(html)
