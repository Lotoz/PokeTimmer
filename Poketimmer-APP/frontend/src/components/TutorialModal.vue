<script setup>
import { ref } from "vue";

defineProps({
  isOpen: {
    type: Boolean,
    default: false,
  },
});

const emit = defineEmits(["close"]);

const pasoActual = ref(0);

const pasos = [
  {
    titulo: "Bienvenido a PokeTimer",
    descripcion:
      "Una aplicación que combina la técnica Pomodoro con el mundo Pokémon. ¡Entrena mientras estudias!",
    icono: "bi-star-fill",
    color: "#f39c12",
  },
  {
    titulo: "Pokédex - Captura Pokémon",
    descripcion:
      "Explora la Pokédex de Kanto para encontrar y capturar Pokémon. Puedes buscar por nombre o número. Algunos tienen forma Shiny especial.",
    icono: "bi-book-half",
    color: "#3498db",
    imagen: "../public/pictures/pokedexview.png",
  },
  {
    titulo: "PC - Gestiona tu Equipo",
    descripcion:
      "Aquí administras tu equipo activo (máximo 6 Pokémon) y la caja de almacenamiento. Puedes renombrar, activar Piedra Eterna o liberar al Pokémon.",
    icono: "bi-cpu",
    color: "#e74c3c",
    imagen: "../public/pictures/pcview.png",
  },
  {
    titulo: "Pomodoro - Entrena mientras Estudias",
    descripcion:
      "Usa el temporizador Pomodoro (ciclos de trabajo y descanso). Al completar un ciclo (o tareas), ¡tus Pokémon ganan experiencia automáticamente!",
    icono: "bi-stopwatch",
    color: "#9b59b6",
    imagen: "../public/pictures/dashboard1.png",
  },
  {
    titulo: "Piedra Eterna - Evita Evoluciones 🪨",
    descripcion:
      "Activa la Piedra Eterna en un Pokémon para evitar que evolucione. Perfecta si prefieres mantener a tu favorito en su forma actual.",
    icono: "bi-graph-up",
    color: "#2ecc71",
  },
  {
    titulo: "Opciones de Personalización",
    descripcion:
      "En el apartado de perfil, puedes configurar tus tiempos de Pomodoro, cambiar tu contraseña, personalizar tu avatar y gestionar tus datos personales para una experiencia a tu medida.",
    icono: "bi-circle-square",
    color: "#f1c40f",
    imagen: "../public/pictures/profileoptions.png",
  },
  {
    titulo: "Esta aplicacion esta en desarrollo",
    descripcion:
      "Puede presentar errores o fallos, si encuentras alguno no dudes en reportarlo para que pueda solucionarlo lo antes posible",
    icono: "bi-list-task",
    color: "#1abc9c",
  },
  {
    titulo: "¡Ya estás listo!",
    descripcion:
      "Ahora explora el dashboard, crea tu equipo y comienza tus sesiones de estudio con Pomodoro. ¡A por todos los Pokémon y el conocimiento!",
    icono: "bi-check-circle-fill",
    color: "#27ae60",
  },
];

const irAlPaso = (indice) => {
  pasoActual.value = Math.max(0, Math.min(indice, pasos.length - 1));
};

const siguientePaso = () => {
  if (pasoActual.value < pasos.length - 1) {
    pasoActual.value++;
  }
};

const anteriorPaso = () => {
  if (pasoActual.value > 0) {
    pasoActual.value--;
  }
};

const cerrarTutorial = () => {
  // Guardar en localStorage que el usuario ya vio el tutorial, si borra el localstorage volverá a aparecer
  localStorage.setItem("tutorial_completado", "true");
  emit("close");
};
</script>

<template>
  <div v-if="isOpen" class="tutorial-overlay">
    <div class="tutorial-modal">
      <button class="btn-close" @click="cerrarTutorial" title="Cerrar tutorial">
        <i class="bi bi-x-lg"></i>
      </button>

      <div class="tutorial-contenido">
        <div class="tutorial-icono">
          <i
            :class="pasos[pasoActual].icono"
            :style="{ color: pasos[pasoActual].color }"></i>
        </div>

        <h2>{{ pasos[pasoActual].titulo }}</h2>
        <p>{{ pasos[pasoActual].descripcion }}</p>

        <!-- Mostrar imagen si existe -->
        <div v-if="pasos[pasoActual].imagen" class="tutorial-imagen">
          <img
            :src="pasos[pasoActual].imagen"
            :alt="pasos[pasoActual].titulo" />
        </div>

        <div class="tutorial-indicador">
          <span>Paso {{ pasoActual + 1 }} de {{ pasos.length }}</span>
          <div class="progress-dots">
            <button
              v-for="(paso, index) in pasos"
              :key="index"
              @click="irAlPaso(index)"
              :class="{ activo: index === pasoActual }"
              :title="`${paso.titulo}`"></button>
          </div>
        </div>
      </div>

      <div class="tutorial-controles">
        <button
          @click="anteriorPaso"
          :disabled="pasoActual === 0"
          class="btn-control">
          <i class="bi bi-chevron-left"></i>
          Anterior
        </button>

        <button
          v-if="pasoActual === pasos.length - 1"
          @click="cerrarTutorial"
          class="btn-control btn-finish">
          <i class="bi bi-check2"></i>
          ¡Entendido!
        </button>

        <button v-else @click="siguientePaso" class="btn-control btn-siguiente">
          Siguiente
          <i class="bi bi-chevron-right"></i>
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.tutorial-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.7);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  backdrop-filter: blur(4px);
}

.tutorial-modal {
  background: rgba(242, 238, 245, 0.98);
  border-radius: 16px;
  border: 4px solid var(--secondary);
  padding: 40px;
  max-width: 600px;
  width: 90%;
  box-shadow: 0 0 40px rgba(153, 79, 243, 0.4);
  position: relative;
  animation: slideIn 0.3s ease;
}

@keyframes slideIn {
  from {
    transform: scale(0.9);
    opacity: 0;
  }
  to {
    transform: scale(1);
    opacity: 1;
  }
}

.btn-close {
  position: absolute;
  top: 15px;
  right: 15px;
  background: transparent;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  color: var(--headline);
  transition: all 0.2s ease;
  padding: 5px;
}

.btn-close:hover {
  transform: scale(1.2);
  color: #e74c3c;
}

.tutorial-contenido {
  text-align: center;
  margin-bottom: 30px;
}

.tutorial-icono {
  font-size: 4rem;
  margin-bottom: 20px;
  animation: bounce 0.6s ease;
}

@keyframes bounce {
  0%,
  100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-10px);
  }
}

.tutorial-contenido h2 {
  color: var(--headline);
  font-size: 1.8rem;
  margin: 0 0 15px 0;
  font-weight: 800;
}

.tutorial-contenido p {
  color: var(--paragraph);
  font-size: 1.05rem;
  line-height: 1.6;
  margin: 0 0 25px 0;
}

.tutorial-indicador {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.tutorial-indicador span {
  color: var(--highlight);
  font-weight: 700;
  font-size: 0.9rem;
}

.progress-dots {
  display: flex;
  justify-content: center;
  gap: 8px;
  flex-wrap: wrap;
}

.progress-dots button {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  border: 2px solid var(--secondary);
  background: transparent;
  cursor: pointer;
  transition: all 0.2s ease;
}

.progress-dots button:hover {
  transform: scale(1.3);
}

.progress-dots button.activo {
  background: var(--secondary);
  transform: scale(1.5);
}

.tutorial-controles {
  display: flex;
  gap: 12px;
  justify-content: space-between;
  align-items: center;
}

.btn-control {
  padding: 6px 10px;
  border: 2px solid var(--stroke);
  border-radius: 6px;
  background: var(--button);
  color: var(--button-text);
  font-weight: 700;
  cursor: pointer;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  gap: 4px;
  font-size: 0.8rem;
  text-transform: uppercase;
}

.btn-control:hover:not(:disabled) {
  background: var(--tertiary);
  transform: translate(-1px, -1px);
  box-shadow: 2px 2px 0px rgba(24, 24, 24, 0.9);
}

.btn-control:disabled {
  opacity: 0.4;
  cursor: not-allowed;
}

.btn-siguiente {
  background: var(--highlight);
  color: white;
  margin-left: auto;
}

.btn-siguiente:hover {
  background: #3a9fa6;
}

.btn-finish {
  background: #27ae60;
  color: white;
  margin-left: auto;
}

.btn-finish:hover {
  background: #1e8449;
}

.tutorial-imagen {
  margin: auto;
  max-width: 70%;
  border-radius: 10px;
  overflow: hidden;
  border: 2px solid var(--secondary);
}

.tutorial-imagen img {
  width: 100%;
  height: auto;
  display: block;
}

@media (max-width: 600px) {
  .tutorial-modal {
    padding: 25px 20px;
  }

  .tutorial-icono {
    font-size: 3rem;
  }

  .tutorial-contenido h2 {
    font-size: 1.4rem;
  }

  .tutorial-contenido p {
    font-size: 0.95rem;
  }

  .btn-control {
    padding: 5px 8px;
    font-size: 0.75rem;
  }

  .tutorial-controles {
    flex-wrap: wrap;
  }
}
</style>
