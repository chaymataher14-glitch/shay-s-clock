import re

with open("index.html", "r") as f:
    html = f.read()

old = """      <div class="section-group">
        <div class="section-label">Sync & Embedding</div>
        <div style="font-size: calc(0.85rem * var(--auto-scale, 1)); color: var(--text); margin-bottom: calc(8px * var(--auto-scale, 1));">
          <span id="dev-warning" style="display: none; background: #ff4444; color: white; padding: 6px; border-radius: 6px; font-weight: bold; margin-bottom: 8px; display: block; text-align: center;">⚠️ Embed blocked! You are using the private development link. You MUST click "Share" at the top right of AI Studio, open the public link, and copy the URL from there to embed in Notion.</span>
          <span style="opacity: 0.8;">Multiple widgets in Notion? You <b>must</b> embed a Unique URL for each to keep settings independent.</span>
        </div>
        <div style="display:flex; gap: calc(8px * var(--auto-scale, 1));">"""

new = """      <div class="section-group">
        <div class="section-label">Sync & Embedding</div>
        <div style="width: 100%; font-size: calc(0.85rem * var(--auto-scale, 1)); color: var(--text); margin-bottom: calc(8px * var(--auto-scale, 1));">
          <span id="dev-warning" style="display: none; background: #ff4444; color: white; padding: 6px; border-radius: 6px; font-weight: bold; margin-bottom: 8px; display: block; text-align: center;">⚠️ Embed blocked! You are using the private development link. You MUST click "Share" at the top right of AI Studio, open the public link, and copy the URL from there to embed in Notion.</span>
          <span style="opacity: 0.8;">Multiple widgets in Notion? You <b>must</b> embed a Unique URL for each to keep settings independent.</span>
        </div>
        <div style="width: 100%; display:flex; gap: calc(8px * var(--auto-scale, 1));">"""

html = html.replace(old, new)

with open("index.html", "w") as f:
    f.write(html)
