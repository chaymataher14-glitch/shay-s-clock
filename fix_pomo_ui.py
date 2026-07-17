import re

with open("index.html", "r") as f:
    html = f.read()

old_pomo_box = """        <div class="settings-grid">
          <div class="field"><label for="w-len">Work (min)</label><input type="number" id="w-len" value="25" min="1" onchange="saveSettings(); resetPomo();"></div>
          <div class="field"><label for="b-len">Break (min)</label><input type="number" id="b-len" value="5" min="1" onchange="saveSettings(); resetPomo();"></div>
          <div class="field"><label for="p-count">Total sessions</label><input type="number" id="p-count" value="4" min="1" onchange="saveSettings(); resetPomo();"></div>
          <div class="field"><label for="long-break-every">Sessions until long break</label><input type="number" id="long-break-every" value="4" min="1" onchange="saveSettings(); resetPomo();"></div>
          <div class="field" style="grid-column: 1 / -1;"><label for="long-break-len">Long break duration (min)</label><input type="number" id="long-break-len" value="15" min="1" onchange="saveSettings(); resetPomo();"></div>
        </div>"""

new_pomo_box = """        <div class="pomo-settings-box">
          <div class="pomo-settings-group">
            <div class="pomo-settings-title">Phase Durations</div>
            <div class="pomo-settings-row">
              <div class="field"><label for="w-len">Work (min)</label><input type="number" id="w-len" value="25" min="1" onchange="saveSettings(); resetPomo();"></div>
              <div class="field"><label for="b-len">Short Break</label><input type="number" id="b-len" value="5" min="1" onchange="saveSettings(); resetPomo();"></div>
              <div class="field"><label for="long-break-len">Long Break</label><input type="number" id="long-break-len" value="15" min="1" onchange="saveSettings(); resetPomo();"></div>
            </div>
          </div>
          <div class="pomo-settings-group" style="border-top: 1px solid rgba(0,0,0,0.05); padding-top: 1rem;">
            <div class="pomo-settings-title">Schedule</div>
            <div class="pomo-settings-row">
              <div class="field"><label for="p-count">Total Sessions</label><input type="number" id="p-count" value="4" min="1" onchange="saveSettings(); resetPomo();"></div>
              <div class="field"><label for="long-break-every">Long Break Every</label><input type="number" id="long-break-every" value="4" min="1" onchange="saveSettings(); resetPomo();"></div>
            </div>
          </div>
        </div>"""

html = html.replace(old_pomo_box, new_pomo_box)

# Add CSS
pomo_css = """
  .pomo-settings-box {
    background: var(--card); padding: calc(1.5rem * var(--auto-scale, 1)); border-radius: calc(1.5rem * var(--auto-scale, 1)); 
    width: 100%; max-width: min(calc(600px * var(--auto-scale, 1)), 100%); margin-top: calc(1.5rem * var(--auto-scale, 1));
    display: flex; flex-direction: column; gap: 1rem;
  }
  .pomo-settings-group { display: flex; flex-direction: column; gap: 0.8rem; }
  .pomo-settings-title { font-size: 0.8rem; font-weight: 700; color: var(--accent-text); text-transform: uppercase; letter-spacing: 0.5px; opacity: 0.8; }
  .pomo-settings-row { display: grid; grid-template-columns: repeat(auto-fit, minmax(100px, 1fr)); gap: calc(1rem * var(--auto-scale, 1)); }
  @container widget (max-width: 400px) {
    .pomo-settings-row { grid-template-columns: 1fr; }
  }
"""

html = html.replace('  .settings-grid {', pomo_css + '\n  .settings-grid {')

with open("index.html", "w") as f:
    f.write(html)
