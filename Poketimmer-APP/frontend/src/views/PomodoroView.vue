<script setup>
import { useRouter } from "vue-router";
import PomodoroTimer from "../components/PomodoroTimer.vue";
import api from "../api/axios";
import showAlert from "../utils/prettyAlert";

const router = useRouter();

const onPomodoroTerminado = async () => {
  try {
    await api.post("entrenamiento/");
    await showAlert(
      "¡Ciclo terminado! Tus Pokémon ganaron experiencia.",
      "success",
    );
    router.push("/dashboard");
  } catch (error) {
    console.error("Error al registrar entrenamiento", error);
    showAlert("Error al registrar entrenamiento", "error");
  }
};
</script>

<template>
  <div class="page-shell">
    <div class="page-card">
      <div style="max-width: 520px; margin: 24px auto">
        <router-link to="/dashboard" class="btn-volver"
          ><i class="bi bi-arrow-left" style="margin-right: 6px"></i> Volver al
          Inicio</router-link
        >
        <PomodoroTimer @pomodoro-terminado="onPomodoroTerminado" />
      </div>
    </div>
  </div>
</template>

<style scoped>
.btn-volver {
  display: inline-block;
  margin-bottom: 12px;
}
</style>
