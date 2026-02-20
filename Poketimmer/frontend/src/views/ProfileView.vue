<script setup>
import { ref, onMounted } from "vue";
import api from "../api/axios";
import { useRouter } from "vue-router";
import showAlert from "../utils/prettyAlert";

const router = useRouter();

const usuario = ref({
  username: "",
  email: "",
  foto_perfil: null,
});

const formData = ref({
  username: "",
  email: "",
});

const passwordData = ref({
  current_password: "",
  new_password: "",
  confirm_password: "",
});

const pomodoroData = ref({
  pomo_tiempo_trabajo: 25,
  pomo_tiempo_descanso: 5,
});

const editMode = ref(false);
const passwordMode = ref(false);
const pomodoroMode = ref(false);
const cargando = ref(true);
const enviando = ref(false);
const previewImage = ref(null);
const selectedFile = ref(null);

const cargarPerfil = async () => {
  try {
    const res = await api.get("perfil/");
    if (res.data && res.data.length > 0) {
      usuario.value = res.data[0];
      formData.value = {
        username: usuario.value.username,
        email: usuario.value.email,
      };
      pomodoroData.value = {
        pomo_tiempo_trabajo: usuario.value.pomo_tiempo_trabajo,
        pomo_tiempo_descanso: usuario.value.pomo_tiempo_descanso,
      };
      if (usuario.value.foto_perfil) {
        previewImage.value = usuario.value.foto_perfil;
      }
    }
  } catch (error) {
    console.error("Error al cargar perfil:", error);
    showAlert("Error al cargar el perfil", "error");
  } finally {
    cargando.value = false;
  }
};

const handleImageSelect = (e) => {
  const file = e.target.files[0];
  if (file) {
    selectedFile.value = file;
    const reader = new FileReader();
    reader.onload = (event) => {
      previewImage.value = event.target.result;
    };
    reader.readAsDataURL(file);
  }
};

const guardarPerfil = async () => {
  if (!formData.value.username || !formData.value.email) {
    showAlert("Por favor completa todos los campos", "error");
    return;
  }

  if (!formData.value.email.includes("@")) {
    showAlert("Correo electrónico inválido", "error");
    return;
  }

  enviando.value = true;

  try {
    const data = new FormData();
    data.append("username", formData.value.username);
    data.append("email", formData.value.email);

    if (selectedFile.value) {
      data.append("foto_perfil", selectedFile.value);
    }

    const res = await api.patch(`perfil/${usuario.value.id}/`, data, {
      headers: { "Content-Type": "multipart/form-data" },
    });

    usuario.value = res.data;
    editMode.value = false;
    selectedFile.value = null;
    showAlert("Perfil actualizado correctamente", "success");
  } catch (error) {
    console.error("Error al guardar:", error);
    showAlert("Error al actualizar el perfil", "error");
  } finally {
    enviando.value = false;
  }
};

const cambiarContrasena = async () => {
  if (
    !passwordData.value.current_password ||
    !passwordData.value.new_password ||
    !passwordData.value.confirm_password
  ) {
    showAlert("Por favor completa todos los campos de contraseña", "error");
    return;
  }

  if (passwordData.value.new_password !== passwordData.value.confirm_password) {
    showAlert("Las contraseñas nuevas no coinciden", "error");
    return;
  }

  if (passwordData.value.new_password.length < 8) {
    showAlert("La contraseña debe tener al menos 8 caracteres", "error");
    return;
  }

  enviando.value = true;

  try {
    const res = await api.patch(`perfil/${usuario.value.id}/`, {
      password: passwordData.value.new_password,
    });

    showAlert("Contraseña actualizada correctamente", "success");
    passwordMode.value = false;
    passwordData.value = {
      current_password: "",
      new_password: "",
      confirm_password: "",
    };
  } catch (error) {
    console.error("Error al cambiar contraseña:", error);
    showAlert("Error al actualizar la contraseña", "error");
  } finally {
    enviando.value = false;
  }
};

const guardarPomodoro = async () => {
  if (
    pomodoroData.value.pomo_tiempo_trabajo < 1 ||
    pomodoroData.value.pomo_tiempo_descanso < 1
  ) {
    showAlert("Los tiempos deben ser mayores a 0", "error");
    return;
  }

  enviando.value = true;

  try {
    const res = await api.patch(`perfil/${usuario.value.id}/`, {
      pomo_tiempo_trabajo: pomodoroData.value.pomo_tiempo_trabajo,
      pomo_tiempo_descanso: pomodoroData.value.pomo_tiempo_descanso,
    });

    usuario.value = res.data;
    pomodoroMode.value = false;
    showAlert("Preferencias Pomodoro actualizadas", "success");
  } catch (error) {
    console.error("Error al guardar Pomodoro:", error);
    showAlert("Error al actualizar las preferencias", "error");
  } finally {
    enviando.value = false;
  }
};

const cancelarEdicion = () => {
  editMode.value = false;
  passwordMode.value = false;
  pomodoroMode.value = false;
  formData.value = {
    username: usuario.value.username,
    email: usuario.value.email,
  };
  previewImage.value = usuario.value.foto_perfil;
  selectedFile.value = null;
  passwordData.value = {
    current_password: "",
    new_password: "",
    confirm_password: "",
  };
  pomodoroData.value = {
    pomo_tiempo_trabajo: usuario.value.pomo_tiempo_trabajo,
    pomo_tiempo_descanso: usuario.value.pomo_tiempo_descanso,
  };
};

onMounted(cargarPerfil);
</script>

<template>
  <div class="page-shell">
    <div class="page-card">
      <div class="profile-container">
        <div class="profile-header">
          <h2>⚙️ MI PERFIL</h2>
          <router-link to="/dashboard" class="btn-volver"
            >⬅ Volver al Centro</router-link
          >
        </div>

        <div v-if="cargando" class="loading">Cargando perfil...</div>

        <div v-else class="profile-content">
          <!-- Vista de lectura -->
          <div v-if="!editMode && !passwordMode" class="profile-view">
            <div class="profile-card">
              <div class="profile-picture-container">
                <img
                  v-if="previewImage"
                  :src="previewImage"
                  alt="Foto de perfil"
                  class="profile-picture" />
                <div v-else class="profile-picture-placeholder">
                  {{ usuario.username.substring(0, 2).toUpperCase() }}
                </div>
              </div>

              <div class="profile-info">
                <div class="info-group">
                  <label class="info-label">Usuario</label>
                  <p class="info-value">{{ usuario.username }}</p>
                </div>

                <div class="info-group">
                  <label class="info-label">Correo</label>
                  <p class="info-value">{{ usuario.email }}</p>
                </div>

                <div class="info-group">
                  <label class="info-label">Preferencias Pomodoro</label>
                  <p class="info-value">
                    Trabajo: {{ usuario.pomo_tiempo_trabajo }}min | Descanso:
                    {{ usuario.pomo_tiempo_descanso }}min
                  </p>
                </div>
              </div>
            </div>

            <div class="button-group">
              <button @click="editMode = true" class="btn-edit">
                ✏️ Editar Perfil
              </button>
              <button @click="pomodoroMode = true" class="btn-pomodoro">
                ⏱️ Configurar Pomodoro
              </button>
              <button @click="passwordMode = true" class="btn-password">
                🔐 Cambiar Contraseña
              </button>
              <button @click="router.push('/')" class="btn-logout">
                Cerrar Sesión
              </button>
            </div>
          </div>

          <!-- Modo edición de perfil -->
          <div v-if="editMode && !passwordMode" class="edit-form">
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
                <label for="foto" class="file-label">
                  Seleccionar imagen
                </label>
              </div>
            </div>

            <div class="form-group">
              <label for="username">Nombre de Usuario</label>
              <input
                id="username"
                v-model="formData.username"
                type="text"
                placeholder="Nombre de usuario"
                class="form-input" />
            </div>

            <div class="form-group">
              <label for="email">Correo Electrónico</label>
              <input
                id="email"
                v-model="formData.email"
                type="email"
                placeholder="correo@ejemplo.com"
                class="form-input" />
            </div>

            <div class="button-group">
              <button
                @click="guardarPerfil"
                :disabled="enviando"
                class="btn-save">
                {{ enviando ? "Guardando..." : "💾 Guardar Cambios" }}
              </button>
              <button
                @click="cancelarEdicion"
                :disabled="enviando"
                class="btn-cancel">
                ❌ Cancelar
              </button>
            </div>
          </div>

          <!-- Modo cambio de contraseña -->
          <div v-if="!editMode && passwordMode" class="edit-form">
            <h3>Cambiar Contraseña</h3>

            <div class="form-group">
              <label for="current-password">Contraseña Actual</label>
              <input
                id="current-password"
                v-model="passwordData.current_password"
                type="password"
                placeholder="Tu contraseña actual"
                class="form-input" />
            </div>

            <div class="form-group">
              <label for="new-password">Nueva Contraseña</label>
              <input
                id="new-password"
                v-model="passwordData.new_password"
                type="password"
                placeholder="Nueva contraseña (mín. 8 caracteres)"
                class="form-input" />
            </div>

            <div class="form-group">
              <label for="confirm-password">Confirmar Nueva Contraseña</label>
              <input
                id="confirm-password"
                v-model="passwordData.confirm_password"
                type="password"
                placeholder="Repite la nueva contraseña"
                class="form-input" />
            </div>

            <div class="button-group">
              <button
                @click="cambiarContrasena"
                :disabled="enviando"
                class="btn-save">
                {{ enviando ? "Actualizando..." : "🔐 Cambiar Contraseña" }}
              </button>
              <button
                @click="cancelarEdicion"
                :disabled="enviando"
                class="btn-cancel">
                ❌ Cancelar
              </button>
            </div>
          </div>

          <!-- Modo configurar Pomodoro -->
          <div
            v-if="!editMode && !passwordMode && pomodoroMode"
            class="edit-form">
            <h3>⏱️ Configurar Pomodoro</h3>

            <div class="form-group">
              <label for="trabajo">Tiempo de Trabajo (minutos)</label>
              <input
                id="trabajo"
                v-model.number="pomodoroData.pomo_tiempo_trabajo"
                type="number"
                min="1"
                max="120"
                class="form-input" />
              <small>Actual: {{ pomodoroData.pomo_tiempo_trabajo }} min</small>
            </div>

            <div class="form-group">
              <label for="descanso">Tiempo de Descanso (minutos)</label>
              <input
                id="descanso"
                v-model.number="pomodoroData.pomo_tiempo_descanso"
                type="number"
                min="1"
                max="60"
                class="form-input" />
              <small>Actual: {{ pomodoroData.pomo_tiempo_descanso }} min</small>
            </div>

            <div class="button-group">
              <button
                @click="guardarPomodoro"
                :disabled="enviando"
                class="btn-save">
                {{ enviando ? "Guardando..." : "💾 Guardar Configuración" }}
              </button>
              <button
                @click="cancelarEdicion"
                :disabled="enviando"
                class="btn-cancel">
                ❌ Cancelar
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.profile-container {
  padding: 20px;
  max-width: 800px;
  margin: 0 auto;
  color: var(--paragraph);
}

.profile-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 4px solid var(--secondary);
  padding-bottom: 15px;
  margin-bottom: 25px;
}

.profile-header h2 {
  color: var(--headline);
  margin: 0;
  font-size: 2rem;
  font-weight: 800;
}

.btn-volver {
  background: var(--button);
  color: var(--button-text);
  padding: 10px 18px;
  text-decoration: none;
  border: 3px solid var(--stroke);
  border-radius: 8px;
  font-weight: 800;
  cursor: pointer;
  transition: all 0.2s ease;
  display: inline-block;
}

.btn-volver:hover {
  background: var(--tertiary);
  transform: translate(-2px, -2px);
  box-shadow: 4px 4px 0px rgba(24, 24, 24, 0.9);
}

.loading {
  font-size: 1.5rem;
  text-align: center;
  margin-top: 50px;
  color: var(--highlight);
  animation: blink 1s infinite;
}

@keyframes blink {
  50% {
    opacity: 0.5;
  }
}

/* Vista de lectura */
.profile-view {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.profile-card {
  background: rgba(242, 238, 245, 0.92);
  border-radius: 12px;
  padding: 20px;
  border: 3px solid var(--stroke);
  box-shadow: 8px 8px 0px rgba(153, 79, 243, 0.12);
  display: flex;
  gap: 25px;
  align-items: flex-start;
}

.profile-picture-container {
  flex-shrink: 0;
}

.profile-picture {
  width: 140px;
  height: 140px;
  border-radius: 12px;
  border: 3px solid var(--stroke);
  object-fit: cover;
  box-shadow: 4px 4px 0px rgba(24, 24, 24, 0.15);
}

.profile-picture-placeholder {
  width: 140px;
  height: 140px;
  border-radius: 12px;
  border: 3px solid var(--stroke);
  background: linear-gradient(135deg, var(--highlight), var(--secondary));
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2.5rem;
  font-weight: 800;
  color: white;
  text-shadow: 2px 2px 0px rgba(24, 24, 24, 0.3);
}

.profile-info {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.info-group {
  padding-bottom: 12px;
  border-bottom: 2px solid rgba(24, 24, 24, 0.1);
}

.info-label {
  display: block;
  font-weight: 800;
  color: var(--headline);
  font-size: 0.85rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 4px;
}

.info-value {
  margin: 0;
  font-size: 1.1rem;
  color: var(--paragraph);
}

/* Formularios */
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

/* Carga de imagen */
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

/* Botones */
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

.btn-edit,
.btn-password {
  background: var(--button);
  color: var(--button-text);
}

.btn-edit:hover,
.btn-password:hover {
  background: var(--highlight);
  transform: translate(-2px, -2px);
  box-shadow: 6px 6px 0px rgba(24, 24, 24, 0.9);
}

.btn-pomodoro {
  background: #f39c12;
  color: white;
}

.btn-pomodoro:hover {
  background: #e67e22;
  transform: translate(-2px, -2px);
  box-shadow: 6px 6px 0px rgba(24, 24, 24, 0.9);
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

.btn-cancel,
.btn-logout {
  background: #e74c3c;
  color: white;
}

.btn-cancel:hover:not(:disabled),
.btn-logout:hover {
  background: #c0392b;
  transform: translate(-2px, -2px);
  box-shadow: 6px 6px 0px rgba(24, 24, 24, 0.9);
}

button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

/* Responsive */
@media (max-width: 768px) {
  .profile-card {
    flex-direction: column;
    align-items: center;
    text-align: center;
  }

  .profile-info {
    width: 100%;
  }

  .button-group button {
    min-width: auto;
  }
}

@media (max-width: 480px) {
  .profile-container {
    padding: 12px;
  }

  .profile-header {
    flex-direction: column;
    gap: 12px;
    align-items: flex-start;
  }

  .profile-header h2 {
    font-size: 1.4rem;
  }

  .profile-card {
    flex-direction: column;
    padding: 15px;
    gap: 15px;
  }

  .profile-picture {
    width: 120px;
    height: 120px;
  }

  .profile-picture-placeholder {
    width: 120px;
    height: 120px;
    font-size: 2rem;
  }

  .button-group {
    flex-direction: column;
  }

  .button-group button {
    width: 100%;
    min-width: auto;
  }

  .edit-form {
    padding: 15px;
  }
}
</style>
