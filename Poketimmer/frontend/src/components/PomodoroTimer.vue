<script setup>
import { ref, computed, watch } from "vue";

// Props con las preferencias del usuario (valores por defecto estándar del método Pomodoro)
const props = defineProps({
  tiempoTrabajo: { type: Number, default: 25 },
  tiempoDescanso: { type: Number, default: 5 },
  tiempoDescansoLargo: { type: Number, default: 30 },
  ciclosMax: { type: Number, default: 4 },
});

const emit = defineEmits(["pomodoro-terminado"]);

// Fases: 'trabajo' | 'descanso' | 'descanso-largo'
const fase = ref("trabajo");
const cicloActual = ref(0);
const tiempoRestante = ref(props.tiempoTrabajo * 60);
const timerActivo = ref(false);
let intervalo = null;

// Si cambian los props (el usuario guardó nuevas preferencias) y el timer está parado, se actualiza
watch(
  () => props.tiempoTrabajo,
  (nuevoValor) => {
    if (!timerActivo.value && fase.value === "trabajo") {
      tiempoRestante.value = nuevoValor * 60;
    }
  }
);

const tiempoFaseActual = computed(() => {
  if (fase.value === "trabajo") return props.tiempoTrabajo * 60;
  if (fase.value === "descanso-largo") return props.tiempoDescansoLargo * 60;
  return props.tiempoDescanso * 60;
});

const etiquetaFase = computed(() => {
  if (fase.value === "trabajo") return "Trabajando";
  if (fase.value === "descanso-largo") return "Descanso Largo";
  return "Descansando";
});

// Número de ciclo a mostrar al usuario (siempre entre 1 y ciclosMax)
const numeroCicloMostrado = computed(() => {
  if (fase.value === "trabajo") {
    // cicloActual cuenta los completados; el actual en curso es el siguiente
    return cicloActual.value + 1;
  }
  // En descanso mostramos el número del ciclo que acabamos de completar
  // cicloActual ya fue incrementado (y reiniciado a 0 si llegó al max)
  // Si es 0, es porque acabamos de hacer el descanso largo (ciclo max completado)
  return cicloActual.value === 0 ? props.ciclosMax : cicloActual.value;
});

const relojVisual = computed(() => {
  const min = Math.floor(tiempoRestante.value / 60);
  const sec = tiempoRestante.value % 60;
  return `${min}:${sec < 10 ? "0" + sec : sec}`;
});

const sonarAlarma = () => {
  try {
    const ctx = new (window.AudioContext || window.webkitAudioContext)();

    const tocarTono = (frecuencia, inicio, duracion) => {
      const oscilador = ctx.createOscillator();
      const ganancia = ctx.createGain();
      oscilador.connect(ganancia);
      ganancia.connect(ctx.destination);
      oscilador.type = "sine";
      oscilador.frequency.setValueAtTime(frecuencia, ctx.currentTime + inicio);
      ganancia.gain.setValueAtTime(0, ctx.currentTime + inicio);
      ganancia.gain.linearRampToValueAtTime(0.5, ctx.currentTime + inicio + 0.05);
      ganancia.gain.linearRampToValueAtTime(0, ctx.currentTime + inicio + duracion);
      oscilador.start(ctx.currentTime + inicio);
      oscilador.stop(ctx.currentTime + inicio + duracion);
    };

    // Melodía de 3 tonos: ¡Pomodoro completado!
    tocarTono(880, 0.0, 0.35);   // La5
    tocarTono(1046, 0.4, 0.35);  // Do6
    tocarTono(1318, 0.8, 0.6);   // Mi6 (más largo al final)
  } catch (e) {
    console.warn("No se pudo reproducir la alarma:", e);
  }
};

const finalizarPomodoro = () => {
  clearInterval(intervalo);
  timerActivo.value = false;
  sonarAlarma();
  emit("pomodoro-terminado");

  // Determinar la siguiente fase
  if (fase.value === "trabajo") {
    cicloActual.value++;
    if (cicloActual.value >= props.ciclosMax) {
      // Descanso largo tras completar todos los ciclos
      fase.value = "descanso-largo";
      cicloActual.value = 0;
    } else {
      fase.value = "descanso";
    }
  } else {
    // Tras cualquier descanso, volvemos a trabajar
    fase.value = "trabajo";
  }

  tiempoRestante.value = tiempoFaseActual.value;
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
  fase.value = "trabajo";
  cicloActual.value = 0;
  tiempoRestante.value = props.tiempoTrabajo * 60;
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
        <span v-if="timerActivo"
          ><i
            class="bi bi-pause-fill"
            aria-hidden="true"
            style="margin-right: 8px"></i>
          PAUSAR</span
        >
        <span v-else
          ><i
            class="bi bi-play-fill"
            aria-hidden="true"
            style="margin-right: 8px"></i>
          INICIAR</span
        >
      </button>
      <button @click="resetTimer" class="btn-reset">
        <i
          class="bi bi-arrow-counterclockwise"
          aria-hidden="true"
          style="margin-right: 8px"></i>
        RESET
      </button>
    </div>
    <p class="status-text">
      <span v-if="timerActivo"
        ><i class="bi bi-activity" aria-hidden="true" style="margin-right: 6px"></i
        >{{ etiquetaFase }}...</span
      >
      <span v-else
        ><i class="bi bi-moon" aria-hidden="true" style="margin-right: 6px"></i
        >En espera</span
      >
    </p>
    <p class="ciclo-text">
      <i class="bi bi-arrow-repeat" aria-hidden="true" style="margin-right: 5px"></i>
      Ciclo {{ numeroCicloMostrado }} / {{ props.ciclosMax }}
      &nbsp;·&nbsp;
      <span class="fase-badge" :class="'fase-' + fase">{{ etiquetaFase }}</span>
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
.ciclo-text {
  font-size: 0.9rem;
  color: var(--paragraph);
  margin-top: 6px;
  display: flex;
  align-items: center;
  gap: 4px;
  flex-wrap: wrap;
  justify-content: center;
}
.fase-badge {
  display: inline-block;
  padding: 2px 10px;
  border-radius: 20px;
  font-size: 0.82rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}
.fase-trabajo {
  background: var(--button);
  color: var(--button-text);
}
.fase-descanso {
  background: #4fc3f7;
  color: #003f5c;
}
.fase-descanso-largo {
  background: #81c784;
  color: #1b5e20;
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
