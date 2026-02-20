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
  background: rgba(242, 238, 245, 0.96);
  border-radius: 12px;
  padding: 18px;
  border: 3px solid var(--stroke);
  box-shadow: 8px 8px 0px rgba(153, 79, 243, 0.06);
}
.pomodoro-panel {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.reloj-marco {
  background: var(--main);
  padding: 18px 32px;
  border-radius: 14px;
  border: 4px solid var(--stroke);
  margin-bottom: 16px;
  box-shadow: inset 0 0 8px rgba(0, 0, 0, 0.04);
}
.timer-display {
  font-size: 4.2rem;
  font-weight: 900;
  color: var(--secondary);
  letter-spacing: 1px;
}
.controls button {
  font-size: 1rem;
  margin: 8px;
  padding: 10px 18px;
  border: 3px solid var(--stroke);
  border-radius: 8px;
  cursor: pointer;
  text-transform: uppercase;
  font-weight: 800;
}
.btn-start {
  background: var(--button);
  color: var(--button-text);
}
.btn-stop {
  background: var(--tertiary);
  color: var(--headline);
}
.btn-reset {
  background: transparent;
  color: var(--paragraph);
  border-style: dashed;
}
.status-text {
  font-size: 1rem;
  color: var(--paragraph);
  margin-top: 12px;
}

@media (max-width: 480px) {
  .timer-display {
    font-size: 2.4rem;
  }
  .reloj-marco {
    padding: 12px 18px;
  }
  .controls button {
    padding: 8px 12px;
    font-size: 0.95rem;
  }
}
</style>
