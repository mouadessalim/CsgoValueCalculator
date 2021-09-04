// app.js

// Modules to control application life and create native browser window
const { app, BrowserWindow} = require('electron')
const { autoUpdater } = require('electron-updater');
const path = require('path')

function createWindow () {
  // Create the browser window.
  const mainWindow = new BrowserWindow({
    width: 740,
    height: 265,
    resizable: false,
    title: "CsgoValueCalculator",
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      nodeIntegration: true,
      contextIsolation: false
    }
  })
  

  // and load the index.html of the app.
  mainWindow.loadFile('index.html')
  mainWindow.setMenuBarVisibility(false)
  mainWindow.webContents.on('new-window', function(e, url) {
    e.preventDefault();
    require('electron').shell.openExternal(url);
  });

  const sendStatusToWindow = (text) => {
    if (mainWindow) {
      mainWindow.webContents.send('message', text);
    }
  };

  autoUpdater.checkForUpdates();

  autoUpdater.on('checking-for-update', () => {
    sendStatusToWindow('Checking for update...');
  });
  autoUpdater.on('update-available', info => {
    sendStatusToWindow('A new Update available! Downloading...');
  });
  autoUpdater.on('error', err => {
    sendStatusToWindow(`Error in auto-updater: ${err.toString()}`);
  });
  autoUpdater.on('download-progress', progressObj => {
    sendStatusToWindow(
      ` Downloaded: ${progressObj.percent}%`
    );
  });
  autoUpdater.on('update-downloaded', info => {
    sendStatusToWindow('Update downloaded! When launching the app the next time, it will update.');
  });

  // Open the DevTools.
  //mainWindow.webContents.openDevTools();
}

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.whenReady().then(() => {
  createWindow()

  app.on('activate', function () {
    // On macOS it's common to re-create a window in the app when the
    // dock icon is clicked and there are no other windows open.
    if (BrowserWindow.getAllWindows().length === 0) createWindow()
  })
})

// Quit when all windows are closed, except on macOS. There, it's common
// for applications and their menu bar to stay active until the user quits
// explicitly with Cmd + Q.
app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') app.quit()
})

// In this file you can include the rest of your app's specific main process
// code. You can also put them in separate files and require them here.
