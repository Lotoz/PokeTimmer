<script setup>
import { ref, computed } from "vue";

const emit = defineEmits(["pomodoro-terminado"]);

const tiempoTrabajo = 25 * 60;
const tiempoRestante = ref(tiempoTrabajo);
const timerActivo = ref(false);
let intervalo = null;

const relojVisual = computed(() => {
  const min = Math.floor(tiempoRestante.value / 60);
  const sec = tiempoRestante.value % 60;
  return `${min}:${sec < 10 ? "0" + sec : sec}`;
});

const finalizarPomodoro = () => {
  clearInterval(intervalo);
  timerActivo.value = false;
  tiempoRestante.value = tiempoTrabajo;
  // Avisamos al Dashboard que terminamos
  emit("pomodoro-terminado");
};

const toggleTimer = () => {
  if (timerActivo.value) {
    clearInterval(intervalo);
    timerActivo.value = false;
  } else {
    timerActivo.value = true;
    intervalo = setInterval(() => {
      if (tiempoRestante.value > 0) {
        tiempoRestante.value--;
      } else {
        finalizarPomodoro();
      }
    }, 1000);
  }
};

const resetTimer = () => {
  clearInterval(intervalo);
  timerActivo.value = false;
  tiempoRestante.value = tiempoTrabajo;
};
</script>

<template>
  <section class="panel pomodoro-panel">
    <div class="reloj-marco">
      <div class="timer-display">{{ relojVisual }}</div>
    </div>
    <div class="controls">
      <button
        @click="toggleTimer"
        :class="timerActivo ? 'btn-stop' : 'btn-start'">
        {{ timerActivo ? "⏸ PAUSAR" : "▶ INICIAR" }}
      </button>
      <button @click="resetTimer" class="btn-reset">↺ RESET</button>
    </div>
    <p class="status-text">
      {{ timerActivo ? "Entrenando...🏋️‍♂️" : "En espera 💤" }}
    </p>
  </section>
</template>

<style scoped>
.panel {
  background: #b93f37;
  border-radius: 10px;
  padding: 20px;
  border: 4px solid #ae7a00;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
}
.pomodoro-panel {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.reloj-marco {
  background: #2f0300;
  padding: 20px 40px;
  border-radius: 15px;
  border: 6px solid #c48300;
  margin-bottom: 20px;
  box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.8);
}
.timer-display {
  font-size: 7rem;
  font-weight: bold;
  color: #952ecc;
  text-shadow: 0 0 10px #240059;
}
.controls button {
  font-size: 1.5rem;
  margin: 10px;
  padding: 15px 30px;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  text-transform: uppercase;
}
.btn-start {
  background: #e67e22;
  color: white;
  border-bottom: 4px solid #d35400;
}
.btn-stop {
  background: #e74c3c;
  color: white;
  border-bottom: 4px solid #c0392b;
}
.btn-reset {
  background: #95a5a6;
  color: white;
  border-bottom: 4px solid #7f8c8d;
}
.status-text {
  font-size: 1.5rem;
  color: #f1c40f;
  margin-top: 15px;
}
</style>
