import re

with open("index.html", "r") as f:
    html = f.read()

# 1. Update playChime
old_chime = """  function playChime() {
    const volEl = document.getElementById('volume');
    const vol = volEl ? volEl.value / 100 : 0.5;
    if (vol <= 0) return;
    try {
      const ctx = getAudioContext();
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.frequency.setValueAtTime(600, ctx.currentTime);
      gain.gain.setValueAtTime(vol, ctx.currentTime);
      osc.start();
      gain.gain.exponentialRampToValueAtTime(0.00001, ctx.currentTime + 1.5);
      osc.stop(ctx.currentTime + 1.5);
    } catch (e) {
      console.error('Audio playback failed', e);
    }
  }"""

new_chime = """  function playChime() {
    const volEl = document.getElementById('volume');
    const vol = volEl ? volEl.value / 100 : 0.5;
    if (vol <= 0) return;
    try {
      const ctx = getAudioContext();
      
      const playBeep = (startTime, freq, duration) => {
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.type = 'sine';
        osc.frequency.setValueAtTime(freq, startTime);
        
        const osc2 = ctx.createOscillator();
        osc2.type = 'triangle';
        osc2.frequency.setValueAtTime(freq * 1.01, startTime); // slight detune
        osc2.connect(gain);
        
        gain.gain.setValueAtTime(0, startTime);
        gain.gain.linearRampToValueAtTime(vol, startTime + 0.05);
        gain.gain.exponentialRampToValueAtTime(0.001, startTime + duration);
        
        osc.start(startTime);
        osc.stop(startTime + duration);
        osc2.start(startTime);
        osc2.stop(startTime + duration);
      };

      const now = ctx.currentTime;
      // Play a clear, bright attention sequence lasting ~2.5 seconds
      playBeep(now, 880, 0.5);      // A5
      playBeep(now + 0.3, 880, 0.5); 
      playBeep(now + 0.6, 1108.73, 0.5); // C#6
      playBeep(now + 0.9, 1108.73, 0.5);
      playBeep(now + 1.2, 1318.51, 1.5); // E6 long
    } catch (e) {
      console.error('Audio playback failed', e);
    }
  }"""

html = html.replace(old_chime, new_chime)

# 2. Fix max-width
html = html.replace('max-width: min(calc(500px * var(--auto-scale, 1)), 100%);', 'max-width: 100%;')

# 3. Fix Sync & Embedding font sizes
old_sync_1 = 'font-size: calc(0.85rem * var(--auto-scale, 1)); color: var(--text); margin-bottom: calc(8px * var(--auto-scale, 1));">'
new_sync_1 = 'font-size: calc(1.05rem * var(--auto-scale, 1)); line-height: 1.5; color: var(--text); margin-bottom: calc(12px * var(--auto-scale, 1));">'
html = html.replace(old_sync_1, new_sync_1)

old_sync_2 = 'font-size: calc(0.75rem * var(--auto-scale, 1)); background: var(--bg); color: var(--text);" onclick="this.select()">'
new_sync_2 = 'font-size: calc(0.9rem * var(--auto-scale, 1)); background: var(--bg); color: var(--text);" onclick="this.select()">'
html = html.replace(old_sync_2, new_sync_2)

old_sync_3 = 'font-size: calc(0.75rem * var(--auto-scale, 1));">Copy</button>'
new_sync_3 = 'font-size: calc(0.9rem * var(--auto-scale, 1));">Copy</button>'
html = html.replace(old_sync_3, new_sync_3)

# make sure warning font size isn't hardcoded too small
html = html.replace('margin-bottom: 8px; display: block; text-align: center;">⚠️', 'margin-bottom: 8px; display: block; text-align: center; font-size: 1em;">⚠️')


with open("index.html", "w") as f:
    f.write(html)
