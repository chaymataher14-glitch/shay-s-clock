import re

with open("index.html", "r") as f:
    html = f.read()

html = html.replace('<body>', '<body tabindex="0">')

with open("index.html", "w") as f:
    f.write(html)
