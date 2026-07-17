import re

with open("index.html", "r") as f:
    html = f.read()

html = html.replace('max-width: min(500px, 100%);', 'max-width: min(900px, 100%);')

# Let's also see if we can do something about the PiP window header
old_pip = "const pipWindow = await documentPictureInPicture.requestWindow({"
new_pip = "const pipWindow = await documentPictureInPicture.requestWindow({ disallowReturnToOpener: true,"

html = html.replace(old_pip, new_pip)

with open("index.html", "w") as f:
    f.write(html)
