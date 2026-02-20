<script setup>
import { ref } from "vue";
import api from "../api/axios";
import { useRouter } from "vue-router";

const username = ref("");
const password = ref("");
const error = ref("");
const router = useRouter();

const login = async () => {
  try {
    // Limpiamos el error al intentar loguearse de nuevo
    error.value = "";

    const response = await api.post("auth/login/", {
      username: username.value,
      password: password.value,
    });

    localStorage.setItem("access_token", response.data.access);
    localStorage.setItem("refresh_token", response.data.refresh);

    router.push("/dashboard");
  } catch (e) {
    console.error(e);
    error.value = "Usuario o contraseña incorrectos";
  }
};
</script>

<template>
  <div class="login-wrapper">
    <div class="login-container">
      <div class="pokeball-container">
        <svg
          class="pokeball"
          viewBox="0 0 100 100"
          xmlns="http://www.w3.org/2000/svg">
          <circle
            cx="50"
            cy="50"
            r="45"
            fill="#f2eef5"
            stroke="#181818"
            stroke-width="6" />
          <path
            d="M 5 50 A 45 45 0 0 1 95 50 Z"
            fill="#4fc4cf"
            stroke="#181818"
            stroke-width="6" />
          <line
            x1="5"
            y1="50"
            x2="95"
            y2="50"
            stroke="#181818"
            stroke-width="6" />
          <circle
            cx="50"
            cy="50"
            r="14"
            fill="#fffffe"
            stroke="#181818"
            stroke-width="6" />
          <circle cx="50" cy="50" r="6" fill="#181818" />
        </svg>
      </div>

      <h2>IDENTIFICACIÓN</h2>
      <p class="tagline">
        Bienvenido — accede para gestionar tu equipo, tareas y temporizador.
      </p>

      <form @submit.prevent="login">
        <input
          v-model="username"
          type="text"
          placeholder="ID Entrenador"
          :class="{ 'input-error': error }"
          required />

        <input
          v-model="password"
          type="password"
          placeholder="Contraseña secreta"
          :class="{ 'input-error': error }"
          required />

        <p v-if="error" class="error-message">{{ error }}</p>

        <button type="submit">Acceder al Sistema</button>
      </form>

      <router-link to="/registro" class="link-register">
        ¿Eres nuevo? Regístrate aquí
      </router-link>
    </div>
  </div>
</template>

<style scoped>
/* Fondo general de la página con imagen */
.login-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  padding: 20px;
  box-sizing: border-box;
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;

  /* Centrado fijo solo para login (llena el viewport) */
  position: fixed;
  inset: 0;
  background-color: var(--highlight);
  background-image: url("/pokemon/alola.jpg");
  background-size: cover;
  background-position: center center;
  background-repeat: no-repeat;
  background-attachment: fixed;
  z-index: 1;
}

.login-wrapper::before {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, rgba(0, 0, 0, 0.04), rgba(0, 0, 0, 0.1));
  pointer-events: none;
}

/* Tarjeta principal estilo ilustración/cómic */
.login-container {
  max-width: 420px;
  width: 100%;
  padding: 36px 56px;
  background: rgba(
    242,
    238,
    245,
    0.96
  ); /* semi-transparente para dejar ver el fondo */
  backdrop-filter: blur(6px);
  border-radius: 16px;
  border: 3px solid var(--stroke);
  text-align: center;
  box-shadow: 12px 12px 0px rgba(153, 79, 243, 0.16);
  box-sizing: border-box;
  position: relative;
  z-index: 2;
}

/* Contenedor y animación de la Pokébola */
.pokeball-container {
  margin-top: -70px;
  margin-bottom: 18px;
  display: flex;
  justify-content: center;
}
.pokeball {
  width: 100px;
  height: 100px;
  transition: transform 0.3s ease;
}
.pokeball:hover {
  transform: rotate(15deg) scale(1.1);
}

/* Título */
h2 {
  color: var(--headline);
  margin-bottom: 25px;
  font-size: 1.8rem;
  font-weight: 800;
  letter-spacing: 1px;
}

.tagline {
  margin-top: -6px;
  margin-bottom: 18px;
  color: var(--paragraph);
  font-weight: 600;
  font-size: 0.95rem;
  opacity: 0.98;
}

/* Campos de entrada */
input {
  display: block;
  width: 100%;
  box-sizing: border-box;
  margin: 15px 0;
  padding: 14px;
  background: var(--elements-bg);
  border: 3px solid var(--stroke);
  border-radius: 8px;
  font-family: inherit;
  font-size: 1.1rem;
  color: var(--paragraph);
  transition: all 0.2s ease;
}

input::placeholder {
  color: #a0a0a0;
}

input:focus {
  outline: none;
  border-color: var(--highlight);
  box-shadow: 0 0 0 4px rgba(79, 196, 207, 0.18);
}

/* ESTADO DE ERROR */
input.input-error {
  border-color: #e74c3c !important;
  background-color: #fff6f6;
  color: #c0392b;
}

.error-message {
  color: #e74c3c;
  font-weight: 600;
  margin: -5px 0 15px 0;
  font-size: 0.95rem;
  text-align: left;
}

/* Botón de acceso */
button {
  width: 100%;
  background: var(--button);
  color: var(--button-text);
  border: 3px solid var(--stroke);
  padding: 14px;
  cursor: pointer;
  font-size: 1.2rem;
  font-weight: bold;
  border-radius: 8px;
  margin-top: 10px;
  box-shadow: 4px 4px 0px rgba(24, 24, 24, 0.9);
  transition: all 0.1s ease-in-out;
}

button:hover {
  background: var(--tertiary);
  transform: translate(-2px, -2px);
  box-shadow: 6px 6px 0px rgba(24, 24, 24, 0.9);
}

button:active {
  transform: translate(4px, 4px);
  box-shadow: 0px 0px 0px #181818;
}

/* Enlace de registro */
.link-register {
  display: block;
  margin-top: 25px;
  color: #994ff3;
  font-weight: 600;
  text-decoration: none;
  font-size: 1rem;
  transition: color 0.2s;
}

.link-register:hover {
  color: #181818;
  text-decoration: underline;
}

/* --- RESPONSIVE DESIGN (MÓVILES) --- */
@media (max-width: 480px) {
  .login-container {
    padding: 30px 20px;
    box-shadow: 5px 5px 0px #994ff3;
  }

  .pokeball-container {
    margin-top: -65px;
  }

  .pokeball {
    width: 75px;
    height: 75px;
  }

  h2 {
    font-size: 1.5rem;
    margin-bottom: 20px;
  }

  input {
    font-size: 1rem;
    padding: 12px;
  }

  button {
    font-size: 1.1rem;
    padding: 12px;
    box-shadow: 3px 3px 0px #181818;
  }

  button:hover {
    box-shadow: 5px 5px 0px #181818;
  }
}
</style>
