<script setup>
import { ref, onMounted } from "vue";

const props = defineProps({
  tareas: Array,
});

//SI esto falla de nuevo, seguramente iniciaste antes el electron y luego el vite.
const emit = defineEmits(["agregar", "toggle", "eliminar"]);
const nuevaTarea = ref("");

const submitAgregar = () => {
  console.log("Intentando agregar tarea:", nuevaTarea.value);
  if (nuevaTarea.value.trim()) {
    emit("agregar", nuevaTarea.value);
    nuevaTarea.value = "";
  }
};
</script>
<template>
  <section class="panel tareas-panel">
    <h3>📋 Misiones Pendientes</h3>

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
        <label class="tarea-content">
          <input
            type="checkbox"
            :checked="tarea.completada"
            @change="$emit('toggle', tarea)" />
          <span class="tarea-texto">{{ tarea.titulo }}</span>
        </label>
        <form @submit.prevent="$emit('eliminar', tarea.id)" style="margin: 0">
          <button type="submit" class="btn-delete">X</button>
        </form>
      </li>
    </ul>
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
.add-task-form {
  display: flex;
  margin-bottom: 15px;
}
.add-task-form input {
  flex-grow: 1;
  padding: 10px;
  background: #1a252f;
  border: 2px solid #7f8c8d;
  color: white;
  font-family: inherit;
  font-size: 1.1rem;
}
.btn-add {
  background: #2ecc71;
  color: white;
  border: none;
  padding: 0 20px;
  cursor: pointer;
  font-size: 1.5rem;
}
.tareas-panel ul {
  list-style: none;
  padding: 0;
  margin: 0;
  max-height: 300px;
  overflow-y: auto;
}
.tarea-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px;
  border-bottom: 2px solid #34495e;
  background: #34495e;
  margin-bottom: 5px;
  border-radius: 5px;
}
.tarea-item.completada .tarea-texto {
  text-decoration: line-through;
  color: #7f8c8d;
}
.tarea-content {
  display: flex;
  align-items: center;
  gap: 10px;
  cursor: pointer;
  width: 100%;
}
.btn-delete {
  background: #e74c3c;
  color: white;
  border: none;
  border-radius: 3px;
  cursor: pointer;
  padding: 5px 10px;
}
</style>
