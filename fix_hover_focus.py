import re

with open("index.html", "r") as f:
    html = f.read()

html = html.replace('document.addEventListener("click", () => { document.body.focus(); });', 'document.addEventListener("click", () => { document.body.focus(); window.focus(); });\ndocument.addEventListener("mouseenter", () => { window.focus(); document.body.focus(); });')

with open("index.html", "w") as f:
    f.write(html)
