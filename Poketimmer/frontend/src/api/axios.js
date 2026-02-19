import axios from 'axios';

// Creamos una instancia de Axios con la URL de Django
const api = axios.create({
    baseURL: 'http://127.0.0.1:8000/api/',
    timeout: 5000, // Si tarda más de 5 segundos, se cancela la petición
    headers: {
        'Content-Type': 'application/json',
    }
});

// INTERCEPTOR:
// Antes de cada petición, revisa si tenemos un token guardado y lo pega. Si no, fuera, no es valida
api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem('access_token');
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    },
    (error) => Promise.reject(error)
);

export default api;