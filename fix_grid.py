import re

with open("index.html", "r") as f:
    html = f.read()

html = html.replace('grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);', 'grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));')

with open("index.html", "w") as f:
    f.write(html)
