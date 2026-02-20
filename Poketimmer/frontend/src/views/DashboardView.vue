<script setup>
import { ref, onMounted } from "vue";
import api from "../api/axios";
import { useRouter } from "vue-router";

// Importamos nuestros nuevos componentes
import ListaTareas from "../components/ListaTareas.vue";
import PomodoroTimer from "../components/PomodoroTimer.vue";
import EquipoPokemon from "../components/EquipoPokemon.vue";

const router = useRouter();

// Estado Global del Dashboard
const tareas = ref([]);
const equipo = ref([]);
const usuario = ref({ username: "Entrenador" });

// --- LÓGICA DE LA API ---
const cargarDatos = async () => {
  try {
    const perfilRes = await api.get("perfil/");
    usuario.value = perfilRes.data[0] || { username: "Entrenador" };

    const tareasRes = await api.get("tareas/");
    tareas.value = tareasRes.data;

    const pokemonRes = await api.get("mis-pokemon/");
    equipo.value = pokemonRes.data.filter((p) => p.en_equipo);
  } catch (error) {
    if (error.response?.status === 401) router.push("/");
  }
};
const actualizarNivel = async () => {
  try {
    const pokemonRes = await api.get("mis-pokemon/");
    equipo.value = pokemonRes.data.filter((p) => p.en_equipo);
  } catch (error) {
    if (error.response?.status === 401) router.push("/");
  }
};

const agregarTarea = async (titulo) => {
  try {
    const res = await api.post("tareas/", { titulo, completada: false });
    tareas.value.push(res.data);
  } catch (e) {
    console.error(e);
  }
};

const toggleCompletada = async (tarea) => {
  try {
    await api.patch(`tareas/${tarea.id}/`, { completada: !tarea.completada });
    tarea.completada = !tarea.completada;

    // Si la tarea se completó, desaparece después de 5 segundos
    if (tarea.completada) {
      setTimeout(() => {
        tareas.value = tareas.value.filter((t) => t.id !== tarea.id);
      }, 5000);
    }

    actualizarNivel(); // Actualizamos el nivel del equipo después de completar una tarea
  } catch (e) {
    console.error(e);
  }
};

const editarTarea = async (tareaData) => {
  try {
    await api.patch(`tareas/${tareaData.id}/`, { titulo: tareaData.titulo });
    const tareaIndex = tareas.value.findIndex((t) => t.id === tareaData.id);
    if (tareaIndex !== -1) {
      tareas.value[tareaIndex].titulo = tareaData.titulo;
    }
  } catch (e) {
    console.error(e);
  }
};

const eliminarTarea = async (id) => {
  try {
    await api.post("tareas/borrar/", { id: id });
    tareas.value = tareas.value.filter((t) => t.id !== id);
    actualizarNivel(); // Actualizamos el nivel del equipo después de eliminar una tarea
  } catch (e) {
    console.error(e);
  }
};

// Se ejecuta cuando el PomodoroTimer emite el evento de finalizar
const registrarEntrenamiento = async () => {
  try {
    // Endpoint que registra el entrenamiento y otorga experiencia a los Pokémon del equipo
    await api.post("entrenamiento/");
    alert("¡Ciclo terminado! Tus Pokémon ganaron experiencia.");
    await cargarDatos(); // Recargamos para ver si subieron de nivel
  } catch (error) {
    console.error("Error al registrar entrenamiento", error);
  }
};

const logout = () => {
  localStorage.removeItem("access_token");
  localStorage.removeItem("refresh_token");
  router.push("/");
};

onMounted(cargarDatos);
</script>

<template>
  <div class="page-shell">
    <div class="page-card">
      <div class="dashboard-container">
        <header class="top-bar">
          <h2>⭐ Entrenador {{ usuario.username }}</h2>
          <div class="nav-buttons">
            <button @click="router.push('/pc')" class="btn-nav">🖥️ PC</button>
            <button @click="router.push('/pokedex')" class="btn-nav">
              📖 Pokedex
            </button>
            <button @click="router.push('/perfil')" class="btn-nav">
              ⚙️ Perfil
            </button>
            <button @click="logout" class="btn-logout">Salir</button>
          </div>
        </header>

        <div class="main-layout">
          <ListaTareas
            :tareas="tareas"
            @agregar="agregarTarea"
            @toggle="toggleCompletada"
            @editar="editarTarea"
            @eliminar="eliminarTarea" />

          <PomodoroTimer @pomodoro-terminado="registrarEntrenamiento" />
        </div>

        <EquipoPokemon :equipo="equipo" />
      </div>
    </div>
  </div>
</template>

<style scoped>
.dashboard-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  padding: 20px;
  max-width: 1200px;
  margin: 0 auto;
}
.top-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
  border-bottom: 4px solid var(--secondary);
  padding-bottom: 10px;
}
.top-bar h2 {
  color: var(--headline);
}
.nav-buttons button {
  margin-left: 10px;
  padding: 8px 15px;
  border-radius: 8px;
  cursor: pointer;
  border: 3px solid var(--stroke);
  font-weight: 800;
  background: var(--button);
  color: var(--button-text);
}
.btn-nav {
  background: var(--highlight);
}
.btn-logout {
  background: var(--tertiary);
  color: var(--headline);
  border-color: var(--stroke);
}
.main-layout {
  display: grid;
  grid-template-columns: 350px 1fr;
  gap: 20px;
  margin-bottom: 20px;
  flex-grow: 1;
}

@media (max-width: 880px) {
  .main-layout {
    grid-template-columns: 1fr;
  }
  .nav-buttons {
    margin-top: 10px;
  }
}
</style>
