/**
 * Sistema de diálogos personalizados con estética consistente
 * Reemplaza alert() y confirm() nativos del navegador
 */

class PrettyDialog {
    constructor() {
        this.currentResolve = null;
        this.initStyles();
    }

    /**
     * Inyecta estilos CSS en el documento
     */
    initStyles() {
        if (document.querySelector('#pretty-dialog-styles')) return;

        const style = document.createElement('style');
        style.id = 'pretty-dialog-styles';
        style.textContent = `
      /* Overlay del diálogo */
      .pretty-dialog-overlay {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(0, 0, 0, 0.6);
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 9999;
        opacity: 0;
        transition: opacity 0.3s ease;
        pointer-events: none;
      }

      .pretty-dialog-overlay.show {
        opacity: 1;
        pointer-events: auto;
      }

      /* Contenedor del diálogo */
      .pretty-dialog {
        background: rgba(242, 238, 245, 0.98);
        border: 4px solid #181818;
        border-radius: 12px;
        padding: 24px;
        box-shadow: 12px 12px 0px rgba(153, 79, 243, 0.2), 0 0 30px rgba(0, 0, 0, 0.3);
        max-width: 400px;
        min-width: 300px;
        transform: scale(0.8);
        transition: transform 0.3s ease;
      }

      .pretty-dialog-overlay.show .pretty-dialog {
        transform: scale(1);
      }

      /* Título */
      .pretty-dialog-title {
        font-size: 1.5rem;
        font-weight: 800;
        color: #2d1b4e;
        margin-bottom: 12px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
      }

      /* Mensaje */
      .pretty-dialog-message {
        font-size: 1rem;
        color: #5a5a5a;
        line-height: 1.6;
        margin-bottom: 24px;
        word-wrap: break-word;
      }

      /* Contenedor de botones */
      .pretty-dialog-buttons {
        display: flex;
        gap: 12px;
        justify-content: flex-end;
      }

      /* Botones */
      .pretty-dialog-btn {
        padding: 10px 20px;
        border: 3px solid #181818;
        border-radius: 8px;
        font-weight: 800;
        font-size: 0.95rem;
        cursor: pointer;
        transition: all 0.2s ease;
        text-transform: uppercase;
        box-shadow: 4px 4px 0px rgba(24, 24, 24, 0.9);
        background: #7c4dff;
        color: white;
      }

      .pretty-dialog-btn:hover {
        transform: translate(-2px, -2px);
        box-shadow: 6px 6px 0px rgba(24, 24, 24, 0.9);
      }

      .pretty-dialog-btn:active {
        transform: translate(2px, 2px);
        box-shadow: 2px 2px 0px rgba(24, 24, 24, 0.9);
      }

      /* Botón secundario (Cancelar/No) */
      .pretty-dialog-btn.secondary {
        background: #f0f0f0;
        color: #181818;
      }

      /* Botón peligro (No/Cancelar) */
      .pretty-dialog-btn.danger {
        background: #e74c3c;
        color: white;
      }

      /* Botón éxito (Sí/Aceptar) */
      .pretty-dialog-btn.success {
        background: #2ecc71;
        color: white;
      }

      /* Ícono del diálogo */
      .pretty-dialog-icon {
        font-size: 2.5rem;
        margin-bottom: 12px;
        display: block;
      }

      /* Input para prompt */
      .pretty-dialog-input {
        width: 100%;
        padding: 10px;
        border: 3px solid #181818;
        border-radius: 6px;
        font-size: 1rem;
        font-family: inherit;
        box-sizing: border-box;
        margin-bottom: 16px;
        background: white;
        color: #181818;
      }

      .pretty-dialog-input:focus {
        outline: none;
        border-color: #7c4dff;
        box-shadow: 0 0 0 3px rgba(124, 77, 255, 0.1);
      }
    `;
        document.head.appendChild(style);
    }

    /**
     * Crea y muestra un diálogo
     */
    showDialog(title, message, type = 'alert', icon = 'bi bi-exclamation-triangle') {
        return new Promise((resolve) => {
            this.currentResolve = resolve;

            // Crear overlay
            const overlay = document.createElement('div');
            overlay.className = 'pretty-dialog-overlay';

            // Crear diálogo
            const dialog = document.createElement('div');
            dialog.className = 'pretty-dialog';

            // Ícono (usar bootstrap icons cuando sea posible)
            const iconEl = document.createElement('span');
            iconEl.className = 'pretty-dialog-icon';
            // Mapea emojis/strings a clases de bootstrap-icons o a texto alternativo
            const mapIcon = (ic) => {
                if (!ic) return '<i class="bi bi-exclamation-triangle"></i>';
                const lookup = {
                    'info': 'bi bi-info-circle',
                    'question': 'bi bi-question-circle',
                    'pencil': 'bi bi-pencil',
                    'x': 'bi bi-x-circle',
                    'check': 'bi bi-check-circle',
                    'warning': 'bi bi-exclamation-triangle',
                };
                if (lookup[ic]) return `<i class="${lookup[ic]}"></i>`;
                // If ic already looks like a class name, try to use it
                if (typeof ic === 'string' && ic.startsWith('bi')) return `<i class="${ic}"></i>`;
                // Fallback: render text
                return `<span>${ic}</span>`;
            };
            iconEl.innerHTML = mapIcon(icon);

            // Título
            const titleEl = document.createElement('h2');
            titleEl.className = 'pretty-dialog-title';
            titleEl.textContent = title;

            // Mensaje
            const messageEl = document.createElement('p');
            messageEl.className = 'pretty-dialog-message';
            messageEl.textContent = message;

            // Botones
            const buttonsDiv = document.createElement('div');
            buttonsDiv.className = 'pretty-dialog-buttons';

            let inputEl = null;

            if (type === 'alert') {
                // Solo botón Aceptar
                const btnAccept = this.createButton('Aceptar', 'success', () => {
                    this.closeDialog(overlay, true);
                });
                buttonsDiv.appendChild(btnAccept);
            } else if (type === 'confirm') {
                // Botones Cancelar y Confirmar
                const btnCancel = this.createButton('Cancelar', 'secondary', () => {
                    this.closeDialog(overlay, false);
                });
                const btnConfirm = this.createButton('Confirmar', 'success', () => {
                    this.closeDialog(overlay, true);
                });
                buttonsDiv.appendChild(btnCancel);
                buttonsDiv.appendChild(btnConfirm);
            } else if (type === 'prompt') {
                // Input para prompt
                inputEl = document.createElement('input');
                inputEl.className = 'pretty-dialog-input';
                inputEl.type = 'text';
                inputEl.placeholder = message;
                inputEl.value = message || '';

                const btnCancel = this.createButton('Cancelar', 'secondary', () => {
                    this.closeDialog(overlay, null);
                });
                const btnConfirm = this.createButton('Aceptar', 'success', () => {
                    this.closeDialog(overlay, inputEl.value);
                });

                // Enter key para confirmar
                inputEl.addEventListener('keypress', (e) => {
                    if (e.key === 'Enter') {
                        this.closeDialog(overlay, inputEl.value);
                    }
                });

                buttonsDiv.appendChild(btnCancel);
                buttonsDiv.appendChild(btnConfirm);
            }

            // Armar diálogo
            dialog.appendChild(iconEl);
            dialog.appendChild(titleEl);
            dialog.appendChild(messageEl);
            if (inputEl) {
                dialog.appendChild(inputEl);
            }
            dialog.appendChild(buttonsDiv);
            overlay.appendChild(dialog);
            document.body.appendChild(overlay);

            // Mostrar con transición
            requestAnimationFrame(() => {
                overlay.classList.add('show');
                if (inputEl) {
                    inputEl.focus();
                    inputEl.select();
                }
            });

            // Permitir cerrar con Escape
            const handleEscape = (e) => {
                if (e.key === 'Escape') {
                    document.removeEventListener('keydown', handleEscape);
                    const result = type === 'confirm' ? false : true;
                    this.closeDialog(overlay, result);
                }
            };
            document.addEventListener('keydown', handleEscape);
        });
    }

    /**
     * Crea un botón con manejadores
     */
    createButton(text, theme, onClick) {
        const btn = document.createElement('button');
        btn.className = `pretty-dialog-btn ${theme}`;
        btn.textContent = text;
        btn.addEventListener('click', onClick);
        return btn;
    }

    /**
     * Cierra el diálogo
     */
    closeDialog(overlay, result) {
        overlay.classList.remove('show');
        setTimeout(() => {
            overlay.remove();
            if (this.currentResolve) {
                this.currentResolve(result);
                this.currentResolve = null;
            }
        }, 300);
    }

    /**
     * Muestra un alert personalizado
     */
    async alert(message, title = 'Información') {
        return this.showDialog(title, message, 'alert', 'bi bi-info-circle');
    }

    /**
     * Muestra un confirm personalizado
     */
    async confirm(message, title = '¿Confirmar?') {
        return this.showDialog(title, message, 'confirm', 'bi bi-question-circle');
    }

    /**
     * Muestra un prompt personalizado
     */
    async prompt(message, title = 'Ingresa texto:', defaultValue = '') {
        return this.showDialog(title, defaultValue, 'prompt', 'bi bi-pencil');
    }

    /**
     * Muestra un alert de error
     */
    async error(message, title = 'Error') {
        return this.showDialog(title, message, 'alert', 'bi bi-x-circle');
    }

    /**
     * Muestra un alert de éxito
     */
    async success(message, title = 'Éxito') {
        return this.showDialog(title, message, 'alert', 'bi bi-check-circle');
    }
}

// Crear instancia global
const dialogManager = new PrettyDialog();

// Reemplazar funciones nativas
if (typeof window !== 'undefined') {
    window.alert = (message) => {
        return dialogManager.alert(message);
    };

    window.confirm = (message) => {
        return dialogManager.confirm(message);
    };

    // Exportar para uso en componentes
    window.prettyDialog = dialogManager;
}

export default dialogManager;
