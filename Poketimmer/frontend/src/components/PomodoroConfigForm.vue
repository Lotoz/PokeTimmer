<script setup>
defineProps({
  pomodoroData: {
    type: Object,
    required: true,
  },
  enviando: {
    type: Boolean,
    default: false,
  },
});

defineEmits(["update:pomodoroData", "save", "cancel"]);
</script>

<template>
  <br />
  <div class="edit-form">
    <h3>
      <i
        class="bi bi-stopwatch"
        aria-hidden="true"
        style="margin-right: 8px"></i>
      Configurar Pomodoro
    </h3>

    <div class="form-group">
      <label for="trabajo">Tiempo de Trabajo (minutos)</label>
      <input
        id="trabajo"
        :value="pomodoroData.pomo_tiempo_trabajo"
        type="number"
        min="1"
        max="120"
        @input="
          $emit('update:pomodoroData', {
            ...pomodoroData,
            pomo_tiempo_trabajo: parseInt($event.target.value),
          })
        "
        class="form-input" />
      <small>Actual: {{ pomodoroData.pomo_tiempo_trabajo }} min</small>
    </div>

    <div class="form-group">
      <label for="descanso">Tiempo de Descanso (minutos)</label>
      <input
        id="descanso"
        :value="pomodoroData.pomo_tiempo_descanso"
        type="number"
        min="1"
        max="60"
        @input="
          $emit('update:pomodoroData', {
            ...pomodoroData,
            pomo_tiempo_descanso: parseInt($event.target.value),
          })
        "
        class="form-input" />
      <small>Actual: {{ pomodoroData.pomo_tiempo_descanso }} min</small>
    </div>

    <div class="form-group">
      <label for="descanso-largo">Tiempo de Descanso Largo (minutos)</label>
      <input
        id="descanso-largo"
        :value="pomodoroData.pomo_tiempo_descanso_largo"
        type="number"
        min="1"
        max="120"
        @input="
          $emit('update:pomodoroData', {
            ...pomodoroData,
            pomo_tiempo_descanso_largo: parseInt($event.target.value),
          })
        "
        class="form-input" />
      <small>Actual: {{ pomodoroData.pomo_tiempo_descanso_largo }} min</small>
    </div>

    <div class="form-group">
      <label for="ciclos">Ciclos Antes del Descanso Largo</label>
      <input
        id="ciclos"
        :value="pomodoroData.pomo_ciclos"
        type="number"
        min="1"
        max="10"
        @input="
          $emit('update:pomodoroData', {
            ...pomodoroData,
            pomo_ciclos: parseInt($event.target.value),
          })
        "
        class="form-input" />
      <small>Actual: {{ pomodoroData.pomo_ciclos }} ciclos</small>
    </div>

    <div class="button-group">
      <button @click="$emit('save')" :disabled="enviando" class="btn-save">
        <span v-if="enviando">Guardando...</span>
        <span v-else
          ><i
            class="bi bi-save"
            aria-hidden="true"
            style="margin-right: 6px"></i>
          Guardar Configuración</span
        >
      </button>
      <button @click="$emit('cancel')" :disabled="enviando" class="btn-cancel">
        <i
          class="bi bi-x-circle"
          aria-hidden="true"
          style="margin-right: 6px"></i>
        Cancelar
      </button>
    </div>
  </div>
</template>

<style scoped>
.edit-form {
  background: rgba(242, 238, 245, 0.92);
  border-radius: 12px;
  padding: 20px;
  border: 3px solid var(--stroke);
  box-shadow: 8px 8px 0px rgba(153, 79, 243, 0.12);
}

.edit-form h3 {
  color: var(--headline);
  font-size: 1.5rem;
  margin-top: 0;
  margin-bottom: 25px;
  padding-bottom: 12px;
  border-bottom: 3px solid var(--secondary);
}

.form-group {
  margin-bottom: 18px;
}

.form-group label {
  display: block;
  font-weight: 800;
  color: var(--headline);
  font-size: 0.95rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 8px;
}

.form-input {
  width: 100%;
  padding: 12px;
  border: 3px solid var(--stroke);
  border-radius: 8px;
  font-family: inherit;
  font-size: 1rem;
  color: var(--paragraph);
  background: var(--elements-bg);
  box-sizing: border-box;
  transition: all 0.2s ease;
}

.form-input:focus {
  outline: none;
  border-color: var(--highlight);
  box-shadow: 0 0 0 4px rgba(79, 196, 207, 0.18);
}

small {
  display: block;
  color: var(--paragraph);
  font-size: 0.85rem;
  margin-top: 4px;
  opacity: 0.8;
}

.button-group {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
  margin-top: 18px;
}

.button-group button {
  flex: 1;
  min-width: 160px;
  padding: 12px 15px;
  font-weight: 800;
  font-size: 1rem;
  border-radius: 8px;
  border: 3px solid var(--stroke);
  cursor: pointer;
  transition: all 0.2s ease;
  text-transform: uppercase;
  box-shadow: 4px 4px 0px rgba(24, 24, 24, 0.9);
}

.btn-save {
  background: #51c91e;
  color: white;
  flex: 1;
}

.btn-save:hover:not(:disabled) {
  background: #40a015;
  transform: translate(-2px, -2px);
  box-shadow: 6px 6px 0px rgba(24, 24, 24, 0.9);
}

.btn-cancel {
  background: #e74c3c;
  color: white;
}

.btn-cancel:hover:not(:disabled) {
  background: #c0392b;
  transform: translate(-2px, -2px);
  box-shadow: 6px 6px 0px rgba(24, 24, 24, 0.9);
}

button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}
</style>
