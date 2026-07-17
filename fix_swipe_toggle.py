import re

with open("index.html", "r") as f:
    html = f.read()

# Add the UI toggle
ui_toggle = """
        <div class="style-row">
          <label for="swipe-nav-toggle">Swipe / Scroll to Navigate Tabs</label>
          <label class="switch">
            <input type="checkbox" id="swipe-nav-toggle" checked onchange="saveSettings()">
            <span class="slider"></span>
          </label>
        </div>"""

html = html.replace('        <div class="style-row">\n          <label for="autostart-toggle">Auto-start next phase</label>', ui_toggle + '\n        <div class="style-row">\n          <label for="autostart-toggle">Auto-start next phase</label>')

# Add to saveSettings
html = html.replace("autoStart: document.getElementById('autostart-toggle').checked,", "autoStart: document.getElementById('autostart-toggle').checked,\n        swipeNav: document.getElementById('swipe-nav-toggle').checked,")

# Add to loadSettings
load_toggle = "if (settings.swipeNav !== undefined) document.getElementById('swipe-nav-toggle').checked = settings.swipeNav;\n      if (settings.autoStart"
html = html.replace("if (settings.autoStart", load_toggle)

with open("index.html", "w") as f:
    f.write(html)
