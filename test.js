function robustToggle() {
  const player = document.getElementById('player');
  if (!player.src || player.src.includes('about:blank')) {
    loadMedia();
  } else {
    togglePlayMedia();
  }
}
