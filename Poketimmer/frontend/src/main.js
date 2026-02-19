import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router' // donde esta importado

const app = createApp(App)
app.use(router) // mi router
app.mount('#app')