export default function showAlert(message, type = 'default', timeout = 3000) {
    // create or reuse alert element
    let el = document.querySelector('.custom-alert');
    if (!el) {
        el = document.createElement('div');
        el.className = 'custom-alert';
        document.body.appendChild(el);
    }

    el.className = 'custom-alert';
    if (type === 'error') el.classList.add('error');
    else if (type === 'success') el.classList.add('success');

    el.textContent = message;

    // show
    requestAnimationFrame(() => el.classList.add('show'));

    // hide after timeout
    clearTimeout(el._hideTimeout);
    el._hideTimeout = setTimeout(() => {
        el.classList.remove('show');
    }, timeout);
}

// also override native alert to use styled alert
if (typeof window !== 'undefined') {
    window.alert = (msg) => showAlert(String(msg), 'default', 3000);
}
