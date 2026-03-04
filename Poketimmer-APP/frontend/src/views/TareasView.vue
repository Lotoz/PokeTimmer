<script setup>
import { ref, onMounted } from "vue";
import api from "../api/axios";
import { useRouter } from "vue-router";
import Pokeball from "../components/Pokeball.vue";

const router = useRouter();
const tareas = ref([]);
const usuario = ref({ username: "Entrenador" });
const filtro = ref("todas"); // "todas", "pendientes", "completadas"
const nuevaTarea = ref("");
const editingId = ref(null);
const editingTitulo = ref("");

// Cargar datos
const cargarDatos = async () => {
  try {
    const perfilRes = await api.get("perfil/");
    usuario.value = perfilRes.data[0] || { username: "Entrenador" };

    const tareasRes = await api.get("tareas/");
    tareas.value = tareasRes.data;
  } catch (error) {
    if (error.response?.status === 401) router.push("/");
  }
};

// Agregar tarea
const agregarTarea = async () => {
  if (!nuevaTarea.value.trim()) return;
  try {
    const res = await api.post("tareas/", {
      titulo: nuevaTarea.value,
      completada: false,
    });
    tareas.value.push(res.data);
    nuevaTarea.value = "";
  } catch (e) {
    console.error(e);
    alert("Error al crear la tarea");
  }
};

// Toggle completada
const toggleCompletada = async (tarea) => {
  try {
    await api.patch(`tareas/${tarea.id}/`, {
      completada: !tarea.completada,
    });
    tarea.completada = !tarea.completada;
  } catch (e) {
    console.error(e);
    alert("Error al actualizar la tarea");
  }
};

// Editar tarea
const iniciarEdicion = (tarea) => {
  editingId.value = tarea.id;
  editingTitulo.value = tarea.titulo;
};

const guardarEdicion = async (tareaId) => {
  if (!editingTitulo.value.trim()) return;
  try {
    await api.patch(`tareas/${tareaId}/`, { titulo: editingTitulo.value });
    const tarea = tareas.value.find((t) => t.id === tareaId);
    if (tarea) {
      tarea.titulo = editingTitulo.value;
    }
    editingId.value = null;
    editingTitulo.value = "";
  } catch (e) {
    console.error(e);
    alert("Error al editar la tarea");
  }
};

const cancelarEdicion = () => {
  editingId.value = null;
  editingTitulo.value = "";
};

// Eliminar tarea
const eliminarTarea = async (id) => {
  try {
    await api.post("tareas/borrar/", { id: id });
    tareas.value = tareas.value.filter((t) => t.id !== id);
  } catch (e) {
    console.error(e);
    alert("Error al eliminar la tarea");
  }
};

// Filtrar tareas
const tareasFiltradas = () => {
  if (filtro.value === "pendientes") {
    return tareas.value.filter((t) => !t.completada);
  } else if (filtro.value === "completadas") {
    return tareas.value.filter((t) => t.completada);
  }
  return tareas.value;
};

onMounted(cargarDatos);
</script>

<template>
  <div class="page-shell">
    <div class="page-card">
      <div class="tareas-view-container">
        <!-- Header -->
        <header class="tareas-header">
          <div class="header-top">
            <h1>
              <i
                class="bi bi-list-task"
                aria-hidden="true"
                style="margin-right: 8px"></i>
              Gestor de Tareas
            </h1>
            <button @click="router.push('/dashboard')" class="btn-back">
              <i
                class="bi bi-arrow-left"
                aria-hidden="true"
                style="margin-right: 6px"></i>
              Volver
            </button>
          </div>

          <!-- Formulario para agregar tarea -->
          <form @submit.prevent="agregarTarea" class="add-task-form-expanded">
            <input
              v-model="nuevaTarea"
              placeholder="Añadir nueva misión..."
              type="text"
              class="input-new-task" />
            <button type="submit" class="btn-add-large">+ Agregar</button>
          </form>

          <!-- Filtros -->
          <div class="filter-buttons">
            <button
              @click="filtro = 'todas'"
              :class="{ active: filtro === 'todas' }"
              class="btn-filter">
              <i
                class="bi bi-pin-angle"
                aria-hidden="true"
                style="margin-right: 6px"></i>
              Todas ({{ tareas.length }})
            </button>
            <button
              @click="filtro = 'pendientes'"
              :class="{ active: filtro === 'pendientes' }"
              class="btn-filter">
              <i
                class="bi bi-hourglass-split"
                aria-hidden="true"
                style="margin-right: 6px"></i>
              Pendientes ({{ tareas.filter((t) => !t.completada).length }})
            </button>
            <button
              @click="filtro = 'completadas'"
              :class="{ active: filtro === 'completadas' }"
              class="btn-filter">
              <i
                class="bi bi-check2-circle"
                aria-hidden="true"
                style="margin-right: 6px"></i>
              Completadas ({{ tareas.filter((t) => t.completada).length }})
            </button>
          </div>
        </header>

        <!-- Lista de tareas -->
        <main class="tareas-main">
          <div v-if="tareasFiltradas().length === 0" class="empty-state-large">
            <p v-if="filtro === 'todas'">
              <i
                class="bi bi-card-text"
                aria-hidden="true"
                style="margin-right: 6px"></i>
              No hay tareas aún.
            </p>
            <p v-else-if="filtro === 'pendientes'">
              <i
                class="bi bi-emoji-sunglasses"
                aria-hidden="true"
                style="margin-right: 6px"></i>
              ¡No hay tareas pendientes! Excelente trabajo.
            </p>
            <p v-else>
              <i
                class="bi bi-emoji-smile"
                aria-hidden="true"
                style="margin-right: 6px"></i>
              No hay tareas completadas aún.
            </p>
          </div>

          <ul class="tareas-list" v-else>
            <li
              v-for="tarea in tareasFiltradas()"
              :key="tarea.id"
              class="tarea-item-expanded"
              :class="{ completada: tarea.completada }">
              <!-- Vista normal -->
              <template v-if="editingId !== tarea.id">
                <div class="tarea-main-content">
                  <Pokeball
                    :completed="tarea.completada"
                    :size="48"
                    @click="toggleCompletada(tarea)" />
                  <div class="tarea-info">
                    <h3 class="tarea-titulo">{{ tarea.titulo }}</h3>
                    <p class="tarea-status">
                      <i
                        :class="
                          tarea.completada
                            ? 'bi bi-check2-circle'
                            : 'bi bi-hourglass-split'
                        "
                        aria-hidden="true"
                        style="margin-right: 6px"></i>
                      {{ tarea.completada ? "Completada" : "Pendiente" }}
                    </p>
                  </div>
                </div>

                <div class="tarea-actions-expanded">
                  <button
                    @click="iniciarEdicion(tarea)"
                    class="btn-action-edit"
                    title="Editar">
                    <i class="bi bi-pencil" aria-hidden="true"></i>
                  </button>
                  <button
                    @click="eliminarTarea(tarea.id)"
                    class="btn-action-delete"
                    title="Eliminar">
                    <i class="bi bi-trash" aria-hidden="true"></i>
                  </button>
                </div>
              </template>

              <!-- Modo edición -->
              <template v-else>
                <input
                  v-model="editingTitulo"
                  @keyup.enter="guardarEdicion(tarea.id)"
                  @keyup.escape="cancelarEdicion"
                  class="edit-input-expanded"
                  placeholder="Editar tarea..." />
                <div class="edit-actions-expanded">
                  <button
                    @click="guardarEdicion(tarea.id)"
                    class="btn-save-expanded">
                    <i
                      class="bi bi-check2"
                      aria-hidden="true"
                      style="margin-right: 6px"></i>
                    Guardar
                  </button>
                  <button @click="cancelarEdicion" class="btn-cancel-expanded">
                    <i
                      class="bi bi-x"
                      aria-hidden="true"
                      style="margin-right: 6px"></i>
                    Cancelar
                  </button>
                </div>
              </template>
            </li>
          </ul>
        </main>
      </div>
    </div>
  </div>
</template>

<style scoped>
.tareas-view-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  padding: 20px;
  max-width: 900px;
  margin: 0 auto;
}

.tareas-header {
  margin-bottom: 30px;
}

.header-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
  border-bottom: 4px solid var(--secondary);
  padding-bottom: 15px;
}

.header-top h1 {
  color: var(--headline);
  font-size: 2rem;
}

.btn-back {
  background: var(--highlight);
  color: white;
  border: 3px solid var(--stroke);
  padding: 10px 20px;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 800;
  font-size: 1rem;
  transition: all 0.2s ease;
}

.btn-back:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.add-task-form-expanded {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}

.input-new-task {
  flex-grow: 1;
  padding: 12px 15px;
  background: var(--elements-bg);
  border: 3px solid var(--stroke);
  color: var(--paragraph);
  font-family: inherit;
  font-size: 1.1rem;
  border-radius: 8px;
}

.input-new-task:focus {
  outline: none;
  border-color: var(--highlight);
  box-shadow: 0 0 0 3px rgba(79, 196, 207, 0.2);
}

.btn-add-large {
  background: var(--button);
  color: var(--button-text);
  border: 3px solid var(--stroke);
  padding: 10px 25px;
  cursor: pointer;
  font-size: 1.1rem;
  border-radius: 8px;
  font-weight: 800;
  transition: all 0.2s ease;
}

.btn-add-large:hover {
  background: var(--highlight);
  transform: translateY(-2px);
}

.filter-buttons {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

.btn-filter {
  background: rgba(242, 238, 245, 0.96);
  color: var(--paragraph);
  border: 3px solid var(--stroke);
  padding: 10px 18px;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 800;
  font-size: 0.95rem;
  transition: all 0.3s ease;
}

.btn-filter:hover {
  background: var(--highlight);
  color: white;
}

.btn-filter.active {
  background: var(--highlight);
  color: white;
  box-shadow: 0 4px 12px rgba(79, 196, 207, 0.3);
}

.tareas-main {
  flex-grow: 1;
}

.empty-state-large {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 300px;
  font-size: 1.3rem;
  color: #9aa2a6;
  text-align: center;
}

.tareas-list {
  list-style: none;
  padding: 0;
  display: grid;
  grid-template-columns: 1fr;
  gap: 15px;
}

.tarea-item-expanded {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 18px;
  background: rgba(242, 238, 245, 0.96);
  border: 3px solid var(--stroke);
  border-radius: 12px;
  transition: all 0.3s ease;
}

.tarea-item-expanded:hover {
  box-shadow: 0 4px 12px rgba(153, 79, 243, 0.15);
  transform: translateY(-2px);
}

.tarea-item-expanded.completada {
  background: rgba(81, 201, 30, 0.08);
}

.tarea-main-content {
  display: flex;
  align-items: center;
  gap: 18px;
  flex-grow: 1;
}

.tarea-info {
  flex-grow: 1;
}

.tarea-titulo {
  margin: 0;
  color: var(--headline);
  font-size: 1.2rem;
  font-weight: 800;
}

.tarea-status {
  margin: 5px 0 0 0;
  color: #9aa2a6;
  font-size: 0.9rem;
}

.tarea-item-expanded.completada .tarea-titulo {
  text-decoration: line-through;
  color: #9aa2a6;
}

.tarea-actions-expanded {
  display: flex;
  gap: 10px;
  align-items: center;
}

.btn-action-edit,
.btn-action-delete {
  background: transparent;
  border: none;
  cursor: pointer;
  font-size: 1.4rem;
  padding: 8px 12px;
  border-radius: 8px;
  transition: all 0.2s ease;
}

.btn-action-edit {
  color: var(--highlight);
}

.btn-action-edit:hover {
  background: rgba(79, 196, 207, 0.2);
}

.btn-action-delete {
  color: #c0392b;
}

.btn-action-delete:hover {
  background: rgba(192, 57, 43, 0.15);
}

.edit-input-expanded {
  flex-grow: 1;
  padding: 12px 15px;
  border: 3px solid var(--highlight);
  border-radius: 8px;
  font-family: inherit;
  font-size: 1.1rem;
  color: var(--paragraph);
}

.edit-input-expanded:focus {
  outline: none;
  box-shadow: 0 0 0 3px rgba(79, 196, 207, 0.2);
}

.edit-actions-expanded {
  display: flex;
  gap: 10px;
}

.btn-save-expanded,
.btn-cancel-expanded {
  padding: 10px 15px;
  border: 3px solid var(--stroke);
  border-radius: 8px;
  cursor: pointer;
  font-weight: 800;
  font-size: 1rem;
  transition: all 0.2s ease;
}

.btn-save-expanded {
  background: #51c91e;
  color: white;
}

.btn-save-expanded:hover {
  background: #3fa517;
}

.btn-cancel-expanded {
  background: #e74c3c;
  color: white;
}

.btn-cancel-expanded:hover {
  background: #c0392b;
}

@media (max-width: 768px) {
  .tareas-view-container {
    padding: 15px;
  }

  .header-top {
    flex-direction: column;
    align-items: flex-start;
    gap: 15px;
  }

  .header-top h1 {
    font-size: 1.5rem;
  }

  .btn-back {
    align-self: flex-start;
  }

  .add-task-form-expanded {
    flex-direction: column;
  }

  .filter-buttons {
    flex-direction: column;
  }

  .btn-filter {
    width: 100%;
  }

  .tarea-main-content {
    flex-direction: column;
    align-items: flex-start;
  }

  .tarea-item-expanded {
    flex-direction: column;
    align-items: flex-start;
    gap: 15px;
  }

  .tarea-actions-expanded {
    width: 100%;
    justify-content: flex-start;
  }
}
</style>
