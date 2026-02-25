<script setup>
const emit = defineEmits([
  "update:formData",
  "update:previewImage",
  "save",
  "cancel",
  "image-selected",
]);

defineProps({
  formData: {
    type: Object,
    required: true,
  },
  previewImage: {
    type: String,
    default: null,
  },
  enviando: {
    type: Boolean,
    default: false,
  },
});

const handleImageSelect = (e) => {
  const file = e.target.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = (event) => {
      emit("update:previewImage", event.target.result);
    };
    reader.readAsDataURL(file);
    emit("image-selected", file);
  }
};
</script>

<template>
  <div class="edit-form">
    <h3>Editar Información</h3>

    <div class="form-group">
      <label for="foto">Foto de Perfil</label>
      <div class="image-upload">
        <div v-if="previewImage" class="image-preview">
          <img :src="previewImage" alt="Preview" />
        </div>
        <input
          id="foto"
          type="file"
          accept="image/*"
          @change="handleImageSelect"
          class="file-input" />
        <label for="foto" class="file-label"> Seleccionar imagen </label>
      </div>
    </div>

    <div class="form-group">
      <label for="username">Nombre de Usuario</label>
      <input
        id="username"
        :value="formData.username"
        type="text"
        placeholder="Nombre de usuario"
        @input="
          $emit('update:formData', {
            ...formData,
            username: $event.target.value,
          })
        "
        class="form-input" />
    </div>

    <div class="form-group">
      <label for="email">Correo Electrónico</label>
      <input
        id="email"
        :value="formData.email"
        type="email"
        placeholder="correo@ejemplo.com"
        @input="
          $emit('update:formData', { ...formData, email: $event.target.value })
        "
        class="form-input" />
    </div>

    <div class="button-group">
      <button @click="$emit('save')" :disabled="enviando" class="btn-save">
        <span v-if="enviando">Guardando...</span>
        <span v-else
          ><i
            class="bi bi-save"
            aria-hidden="true"
            style="margin-right: 6px"></i>
          Guardar Cambios</span
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

.image-upload {
  display: flex;
  flex-direction: column;
  gap: 12px;
  align-items: center;
}

.image-preview {
  width: 100%;
  max-width: 200px;
  overflow: hidden;
  border-radius: 8px;
  border: 3px solid var(--stroke);
}

.image-preview img {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.file-input {
  display: none;
}

.file-label {
  padding: 10px 20px;
  background: var(--button);
  color: var(--button-text);
  border: 3px solid var(--stroke);
  border-radius: 8px;
  font-weight: 800;
  cursor: pointer;
  transition: all 0.2s ease;
}

.file-label:hover {
  background: var(--tertiary);
  transform: translate(-2px, -2px);
  box-shadow: 4px 4px 0px rgba(24, 24, 24, 0.9);
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
