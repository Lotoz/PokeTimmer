<script setup>
import { ref } from "vue";
import api from "../api/axios";
import { useRouter } from "vue-router";

const username = ref("");
const password = ref("");
const email = ref("");
const error = ref("");
const router = useRouter();

const registrar = async () => {
  try {
    await api.post("auth/registro/", {
      username: username.value,
      password: password.value,
      email: email.value,
    });

    alert("¡Registro exitoso! Bienvenido al mundo Pokémon.");
    router.push("/");
  } catch (e) {
    console.error(e);
    // Intentamos capturar el error específico de Django si el usuario ya existe
    error.value =
      e.response?.data?.username?.[0] || "Error al registrar entrenador";
  }
};
</script>

<template>
  <div class="login-wrapper">
    <div class="login-container">
      <h2>NUEVO ENTRENADOR</h2>
      <form @submit.prevent="registrar">
        <input
          v-model="username"
          type="text"
          placeholder="ID Entrenador (Usuario)"
          required />
        <input
          v-model="email"
          type="email"
          placeholder="Correo electrónico"
          required />
        <input
          v-model="password"
          type="password"
          placeholder="Contraseña"
          required />
        <button type="submit">Crear Cuenta</button>
      </form>

      <p v-if="error" class="error">❌ {{ error }}</p>

      <router-link to="/" class="link-back">
        ¿Ya tienes cuenta? Identifícate
      </router-link>
    </div>
  </div>
</template>

<style scoped>
.login-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: #1a252f;
}

.login-container {
  max-width: 350px;
  width: 100%;
  padding: 30px;
  background: #c0392b; /* Rojo base */
  border-radius: 15px;
  border: 6px solid #e74c3c; /* Rojo brillante */
  text-align: center;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.5);
  color: white;
}

h2 {
  color: #f1c40f;
  margin-bottom: 20px;
  font-size: 2rem;
  border-bottom: 2px solid rgba(255, 255, 255, 0.2);
  padding-bottom: 10px;
}

input {
  display: block;
  width: 100%;
  margin: 15px 0;
  padding: 12px;
  background: #ecf0f1;
  border: 4px solid #7f8c8d;
  border-radius: 5px;
  font-family: inherit;
  font-size: 1.2rem;
  color: #2c3e50; /* Texto oscuro para lectura */
}

button {
  width: 100%;
  background: #2ecc71;
  color: #fff;
  border: 4px solid #27ae60;
  padding: 12px;
  cursor: pointer;
  font-size: 1.3rem;
  border-radius: 5px;
  margin-top: 10px;
}

.error {
  background: rgba(0, 0, 0, 0.5);
  padding: 10px;
  margin-top: 15px;
  border-radius: 5px;
  color: #ff6b6b;
}

.link-back {
  display: block;
  margin-top: 20px;
  color: #f1c40f;
  text-decoration: none;
  font-size: 1.1rem;
}

.link-back:hover {
  text-decoration: underline;
}
</style>
