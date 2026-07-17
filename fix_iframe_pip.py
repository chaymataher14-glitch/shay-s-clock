import re

with open("index.html", "r") as f:
    html = f.read()

# Instead of just changing src, replace the iframe entirely
pip_move_old = """      const player = document.getElementById('player');
      const playerSrc = player ? player.src : '';
      if (player) player.src = 'about:blank'; // prevent double-play or errors while moving
      
      pipWindow.document.body.appendChild(widget);
      
      if (player) {
         // Re-assign src after a short delay to ensure it loads in the new window context
         setTimeout(() => {
             player.src = playerSrc;
         }, 50);
      }"""

pip_move_new = """      const player = document.getElementById('player');
      const playerContainer = player ? player.parentElement : null;
      const playerSrc = player ? player.src : '';
      if (player) player.remove();
      
      pipWindow.document.body.appendChild(widget);
      
      if (playerSrc && playerContainer) {
         setTimeout(() => {
             const newPlayer = pipWindow.document.createElement('iframe');
             newPlayer.id = 'player';
             newPlayer.title = 'YouTube player';
             newPlayer.allow = 'autoplay; encrypted-media; picture-in-picture';
             newPlayer.allowFullscreen = true;
             newPlayer.style.position = 'absolute';
             newPlayer.style.width = '100%';
             newPlayer.style.height = '100%';
             newPlayer.style.border = 'none';
             newPlayer.src = playerSrc;
             playerContainer.appendChild(newPlayer);
         }, 50);
      }"""
      
html = html.replace(pip_move_old, pip_move_new)

pip_close_old = """      pipWindow.addEventListener("pagehide", (event) => {
        // bring it back
        const p = pipWindow.document.getElementById('player');
        const pSrc = p ? p.src : '';
        if (p) p.src = 'about:blank';

        window.__pipWindow = null;
        document.body.appendChild(widget);

        if (p) {
           setTimeout(() => { p.src = pSrc; }, 50);
        }
      });"""

pip_close_new = """      pipWindow.addEventListener("pagehide", (event) => {
        // bring it back
        const p = pipWindow.document.getElementById('player');
        const pContainer = p ? p.parentElement : null;
        const pSrc = p ? p.src : '';
        if (p) p.remove();

        window.__pipWindow = null;
        document.body.appendChild(widget);

        if (pSrc && pContainer) {
           setTimeout(() => {
             const newPlayer = document.createElement('iframe');
             newPlayer.id = 'player';
             newPlayer.title = 'YouTube player';
             newPlayer.allow = 'autoplay; encrypted-media; picture-in-picture';
             newPlayer.allowFullscreen = true;
             newPlayer.style.position = 'absolute';
             newPlayer.style.width = '100%';
             newPlayer.style.height = '100%';
             newPlayer.style.border = 'none';
             newPlayer.src = pSrc;
             pContainer.appendChild(newPlayer);
           }, 50);
        }
      });"""

html = html.replace(pip_close_old, pip_close_new)

with open("index.html", "w") as f:
    f.write(html)
