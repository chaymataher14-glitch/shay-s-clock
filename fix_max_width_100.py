import re

with open("index.html", "r") as f:
    html = f.read()

html = html.replace('max-width: min(900px, 100%);', 'max-width: 100%;')

with open("index.html", "w") as f:
    f.write(html)
