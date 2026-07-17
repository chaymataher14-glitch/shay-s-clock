import re

with open("index.html", "r") as f:
    html = f.read()

dup_block = """  @container widget (max-width: 460px) {
  
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

  .settings-grid { grid-template-columns: 1fr; }
  }"""

correct_block = """  @container widget (max-width: 460px) {
    .settings-grid { grid-template-columns: 1fr; }
  }"""

html = html.replace(dup_block, correct_block)

with open("index.html", "w") as f:
    f.write(html)
