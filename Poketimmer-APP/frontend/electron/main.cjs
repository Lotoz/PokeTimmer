const { app, BrowserWindow } = require('electron');
const path = require('path');
const { spawn } = require('child_process');

let backendProcess = null;

function startBackend() {
    if (app.isPackaged) {
        const executableName = process.platform === 'win32' ? 'pokeapi.exe' : 'pokeapi';
        // Usamos path.resolve para asegurar que la ruta sea absoluta y limpia
        const backendPath = path.resolve(process.resourcesPath, 'backend', executableName);

        console.log("Ruta detectada para backend:", backendPath);

        backendProcess = spawn(backendPath, [], {
            // VITAL: Ejecutar el proceso con el directorio de trabajo correcto
            cwd: path.dirname(backendPath),
            env: {
                ...process.env,
                PYTHONUNBUFFERED: "1" // Para que los logs salgan en tiempo real
            }
        });

        backendProcess.stdout.on('data', (data) => {
            console.log(`[Django STDOUT]: ${data}`);
        });

        backendProcess.stderr.on('data', (data) => {
            console.error(`[Django STDERR]: ${data}`);
        });

        backendProcess.on('error', (err) => {
            console.error("No se pudo lanzar el proceso del backend:", err);
        });

        backendProcess.on('close', (code) => {
            console.log(`El proceso del backend se cerró con código: ${code}`);
        });
    }
}

function createWindow() {
    const mainWindow = new BrowserWindow({
        width: 1200,
        height: 800,
        title: "Poké-Pomodoro",
        icon: path.join(__dirname, '../public/favicon/ico.png'),
        webPreferences: {
            nodeIntegration: true,
            contextIsolation: false
        }
    });

    const isDev = !app.isPackaged;

    if (isDev) {
        mainWindow.loadURL('http://localhost:5173');
        mainWindow.webContents.openDevTools();
    } else {
        mainWindow.loadFile(path.join(__dirname, '../dist/index.html'));
        mainWindow.webContents.openDevTools();
    }
}


app.whenReady().then(() => {
    startBackend();
    setTimeout(() => {
        createWindow();
    }, 1000);
    app.on('activate', () => {
        if (BrowserWindow.getAllWindows().length === 0) createWindow();
    });
});


app.on('window-all-closed', () => {
    if (backendProcess) {
        backendProcess.kill();
    }
    if (process.platform !== 'darwin') app.quit();
});