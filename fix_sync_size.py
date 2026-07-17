import re

with open("index.html", "r") as f:
    html = f.read()

html = html.replace('font-size: calc(1.05rem * var(--auto-scale, 1));', 'font-size: calc(1.15rem * var(--auto-scale, 1));')
html = html.replace('font-size: calc(0.9rem * var(--auto-scale, 1));', 'font-size: calc(1rem * var(--auto-scale, 1));')

with open("index.html", "w") as f:
    f.write(html)
