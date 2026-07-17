import re

with open("index.html", "r") as f:
    html = f.read()

html = html.replace('body, html { \n    margin: 0; padding: 0; width: 100%; height: 100%;\n    background: transparent;', 'body, html { \n    margin: 0; padding: 0; width: 100%; height: 100%;\n    overflow: hidden;\n    background: transparent;')

with open("index.html", "w") as f:
    f.write(html)
