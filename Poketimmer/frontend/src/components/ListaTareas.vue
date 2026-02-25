<script setup>
import { ref, onMounted } from "vue";
import Pokeball from "./Pokeball.vue";

const props = defineProps({
  tareas: Array,
});

const emit = defineEmits(["agregar", "toggle", "eliminar", "editar"]);
const nuevaTarea = ref("");
const editingId = ref(null);
const editingTitulo = ref("");

const submitAgregar = () => {
  if (nuevaTarea.value.trim()) {
    emit("agregar", nuevaTarea.value);
    nuevaTarea.value = "";
  }
};

const iniciarEdicion = (tarea) => {
  editingId.value = tarea.id;
  editingTitulo.value = tarea.titulo;
};

const guardarEdicion = (tareaId) => {
  if (editingTitulo.value.trim()) {
    emit("editar", { id: tareaId, titulo: editingTitulo.value });
    editingId.value = null;
    editingTitulo.value = "";
  }
};

const cancelarEdicion = () => {
  editingId.value = null;
  editingTitulo.value = "";
};
</script>
<template>
  <section class="panel tareas-panel">
    <h3>
      <i
        class="bi bi-list-task"
        aria-hidden="true"
        style="margin-right: 8px"></i>
      Misiones Pendientes
    </h3>

    <form @submit.prevent="submitAgregar" class="add-task-form">
      <input
        v-model="nuevaTarea"
        placeholder="Añadir nueva misión..."
        type="text" />
      <button type="submit" class="btn-add">+</button>
    </form>

    <div v-if="tareas.length === 0" class="empty-state">
      No hay misiones activas.
    </div>

    <ul>
      <li
        v-for="tarea in tareas"
        :key="tarea.id"
        class="tarea-item"
        :class="{ completada: tarea.completada }">
        <!-- Vista normal -->
        <template v-if="editingId !== tarea.id">
          <label class="tarea-content">
            <Pokeball
              :completed="tarea.completada"
              :size="32"
              @click="$emit('toggle', tarea)" />
            <span class="tarea-texto">{{ tarea.titulo }}</span>
          </label>
          <div class="tarea-actions">
            <button
              @click="iniciarEdicion(tarea)"
              class="btn-edit-task"
              title="Editar">
              <i class="bi bi-pencil" aria-hidden="true"></i>
            </button>
            <button @click="$emit('eliminar', tarea.id)" class="btn-delete">
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
            class="edit-input"
            placeholder="Editar tarea..." />
          <div class="edit-actions">
            <button @click="guardarEdicion(tarea.id)" class="btn-save">
              <i class="bi bi-check2" aria-hidden="true"></i>
            </button>
            <button @click="cancelarEdicion" class="btn-cancel-edit">
              <i class="bi bi-x" aria-hidden="true"></i>
            </button>
          </div>
        </template>
      </li>
    </ul>
  </section>
</template>

<style scoped>
.panel {
  background: rgba(242, 238, 245, 0.96);
  border-radius: 12px;
  padding: 18px;
  border: 3px solid var(--stroke);
  box-shadow: 8px 8px 0px rgba(153, 79, 243, 0.08);
}
.add-task-form {
  display: flex;
  gap: 8px;
  margin-bottom: 14px;
}
.add-task-form input {
  flex-grow: 1;
  padding: 10px 12px;
  background: var(--elements-bg);
  border: 3px solid var(--stroke);
  color: var(--paragraph);
  font-family: inherit;
  font-size: 1.05rem;
  border-radius: 8px;
}
.btn-add {
  background: var(--button);
  color: var(--button-text);
  border: 3px solid var(--stroke);
  padding: 6px 12px;
  cursor: pointer;
  font-size: 1.3rem;
  border-radius: 8px;
  font-weight: 800;
}
.tareas-panel ul {
  list-style: none;
  padding: 0;
  margin: 0;
  max-height: 320px;
  overflow-y: auto;
}
.tarea-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px;
  border-bottom: 1px solid rgba(0, 0, 0, 0.06);
  background: var(--elements-bg);
  margin-bottom: 8px;
  border-radius: 8px;
}
.tarea-item.completada .tarea-texto {
  text-decoration: line-through;
  color: #9aa2a6;
}
.tarea-content {
  display: flex;
  align-items: center;
  gap: 12px;
  cursor: pointer;
  width: 100%;
}

.tarea-actions {
  display: flex;
  gap: 6px;
  align-items: center;
}

.btn-edit-task {
  background: transparent;
  color: var(--highlight);
  border: none;
  cursor: pointer;
  font-size: 1rem;
  padding: 4px 8px;
  border-radius: 4px;
  transition: all 0.2s ease;
}

.btn-edit-task:hover {
  background: rgba(79, 196, 207, 0.2);
}

.edit-input {
  flex: 1;
  padding: 8px 10px;
  border: 2px solid var(--highlight);
  border-radius: 6px;
  font-family: inherit;
  font-size: 0.95rem;
  color: var(--paragraph);
}

.edit-input:focus {
  outline: none;
  box-shadow: 0 0 0 3px rgba(79, 196, 207, 0.2);
}

.edit-actions {
  display: flex;
  gap: 6px;
}

.btn-save,
.btn-cancel-edit {
  background: transparent;
  border: none;
  cursor: pointer;
  font-size: 1.1rem;
  padding: 4px 8px;
  border-radius: 4px;
  transition: all 0.2s ease;
  font-weight: 800;
}

.btn-save {
  color: #51c91e;
}

.btn-save:hover {
  background: rgba(81, 201, 30, 0.2);
}

.btn-cancel-edit {
  color: #e74c3c;
}

.btn-cancel-edit:hover {
  background: rgba(231, 76, 60, 0.2);
}
.btn-delete {
  background: transparent;
  color: #c0392b;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  padding: 6px 10px;
  font-weight: 800;
}
.btn-delete:hover {
  background: rgba(192, 57, 43, 0.2);
}

@media (max-width: 720px) {
  .pokemon-grid,
  .tareas-panel ul {
    max-height: 240px;
  }
  .add-task-form input {
    font-size: 1rem;
  }
}
</style>
