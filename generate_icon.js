const fs = require('fs');

// A simple 1x1 transparent png for now, or just an svg
const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
  <rect width="512" height="512" fill="#FDF9F3"/>
  <circle cx="256" cy="256" r="150" fill="#7A6F68"/>
</svg>`;

// We will use SVGs or generate PNGs?
// Manifest supports SVG for icons in modern browsers, but we declared PNG. Let's change the manifest to SVG for simplicity.
