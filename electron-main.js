const { app, BrowserWindow } = require('electron');
const path = require('path');

// Try to use electron-store if available (installed via npm)
let Store;
try {
  Store = require('electron-store');
} catch(e) {
  Store = null;
}

const store = Store ? new Store() : null;

function createWindow() {
  const windowBounds = store ? store.get('windowBounds') : null;
  
  const mainWindow = new BrowserWindow({
    width: windowBounds ? windowBounds.width : 800,
    height: windowBounds ? windowBounds.height : 600,
    x: windowBounds ? windowBounds.x : undefined,
    y: windowBounds ? windowBounds.y : undefined,
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true,
      sandbox: true,
    },
    icon: path.join(__dirname, 'public/icon.png'),
    autoHideMenuBar: true,
  });

  // Remember window state
  mainWindow.on('resize', () => {
    if(store) store.set('windowBounds', mainWindow.getBounds());
  });
  
  mainWindow.on('move', () => {
    if(store) store.set('windowBounds', mainWindow.getBounds());
  });

  // Check if we are in development mode (running via vite) or production (loading dist/index.html)
  // Usually, we would load the built dist/index.html
  mainWindow.loadFile(path.join(__dirname, 'dist/index.html')).catch(() => {
    // fallback if dist is missing, maybe running dev
    console.log("dist/index.html not found, make sure to build first");
  });
}

app.whenReady().then(() => {
  createWindow();

  app.on('activate', function () {
    if (BrowserWindow.getAllWindows().length === 0) createWindow();
  });
});

app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') app.quit();
});
