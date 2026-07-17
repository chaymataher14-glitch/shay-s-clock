import re
with open("index.html", "r") as f:
    html = f.read()

# change parseYouTubeEmbed to use youtube-nocookie.com
html = html.replace('https://www.youtube.com/embed/', 'https://www.youtube-nocookie.com/embed/')

with open("index.html", "w") as f:
    f.write(html)
