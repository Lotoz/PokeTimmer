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
      <h2>IDENTIFICACIÓN</h2>
      <form @submit.prevent="login">
        <input
          v-model="username"
          type="text"
          placeholder="ID Entrenador"
          required />
        <input
          v-model="password"
          type="password"
          placeholder="Contraseña secreta"
          required />
        <button type="submit">Acceder al Sistema</button>
      </form>
      <p v-if="error" class="error">{{ error }}</p>
      <router-link to="/registro" class="link-register"
        >¿Eres nuevo? Regístrate aquí</router-link
      >
    </div>
  </div>
</template>

<style scoped>
.login-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
.login-container {
  max-width: 350px;
  width: 100%;
  padding: 30px;
  background: #c0392b;
  border-radius: 15px;
  border: 6px solid #e74c3c;
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
  color: #2c3e50;
}
input::placeholder {
  color: #7f8c8d;
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
}
.link-register {
  display: block;
  margin-top: 15px;
  color: #f1c40f;
  text-decoration: none;
}
.link-register:hover {
  text-decoration: underline;
}
</style>
