const { app, BrowserWindow } = require('electron');
const path = require('path');

function createWindow() {
    // 1. Configuración de la ventana
    const mainWindow = new BrowserWindow({
        width: 1200,
        height: 800,
        title: "Poké-Pomodoro",
        icon: path.join(__dirname, '../public/favicon.ico'), // Opcional
        webPreferences: {
            nodeIntegration: true,
            contextIsolation: false
        }
    });

    // 2. ¿Qué cargamos?
    // EN DESARROLLO: Cargamos la URL de Vite (localhost:5173)
    // EN PRODUCCIÓN: Cargaremos el archivo index.html generado
    const isDev = !app.isPackaged;

    if (isDev) {
        mainWindow.loadURL('http://localhost:5173');
        // Abrir herramientas de desarrollador (F12) automáticamente para ver errores
        mainWindow.webContents.openDevTools();
    } else {
        mainWindow.loadFile(path.join(__dirname, '../dist/index.html'));
    }
}

// 3. Ciclo de vida de la App
app.whenReady().then(() => {
    createWindow();

    app.on('activate', () => {
        if (BrowserWindow.getAllWindows().length === 0) createWindow();
    });
});

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') app.quit();
});