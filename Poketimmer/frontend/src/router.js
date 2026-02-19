import { createRouter, createWebHistory } from 'vue-router';
import LoginView from './views/LoginView.vue';
import DashboardView from './views/DashboardView.vue';
import PokedexView from './views/PokedexView.vue';
import PCView from './views/PCView.vue';
import RegistroView from './views/RegistroView.vue';

const routes = [
    { path: '/', component: LoginView },
    { path: '/registro', component: RegistroView },
    { path: '/dashboard', component: DashboardView, meta: { requiresAuth: true } },//Protegido 
    { path: '/pokedex', component: PokedexView, meta: { requiresAuth: true } },
    { path: '/pc', component: PCView, meta: { requiresAuth: true } },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

// GUARDIA DE NAVEGACIÓN
// Si intentas ir a /dashboard sin tener token, te patea al Login
router.beforeEach((to, from, next) => {
    const token = localStorage.getItem('access_token');
    if (to.meta.requiresAuth && !token) {
        next('/');
    } else {
        next();
    }
});

export default router;