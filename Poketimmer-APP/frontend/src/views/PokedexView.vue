<script setup>
import { ref, onMounted, computed } from "vue";
import { useRoute } from "vue-router";
import api from "../api/axios";
import showAlert from "../utils/prettyAlert";
import { getLocalPath } from "../utils/imagePaths";

const pokemons = ref([]);
const cargando = ref(true);
const route = useRoute();

const searchName = ref("");
const searchNumber = ref("");

const filteredPokemons = computed(() => {
  return pokemons.value.filter((p) => {
    const matchesName = searchName.value
      ? p.nombre.toLowerCase().includes(searchName.value.toLowerCase())
      : true;
    const matchesNumber = searchNumber.value
      ? String(p.numero).includes(String(searchNumber.value))
      : true;
    return matchesName && matchesNumber;
  });
});

// TIPOS: usamos emojis para los iconos de tipo (me lo pediste así)
const tiposConfig = {
  grass: { color: "#51c91e", emoji: "🌿" },
  poison: { color: "#a040a0", emoji: "☠️" },
  fire: { color: "#ff6b35", emoji: "🔥" },
  water: { color: "#4fc4cf", emoji: "💧" },
  bug: { color: "#a8b820", emoji: "🐛" },
  normal: { color: "#a8a878", emoji: "🔘" },
  electric: { color: "#ffd700", emoji: "⚡" },
  ground: { color: "#915d3a", emoji: "🟫" },
  fairy: { color: "#ee99ac", emoji: "✨" },
  fighting: { color: "#d4492d", emoji: "✊" },
  psychic: { color: "#f85888", emoji: "🧠" },
  rock: { color: "#b8a038", emoji: "🪨" },
  steel: { color: "#b8b8d0", emoji: "⚙️" },
  ice: { color: "#a0e7e8", emoji: "❄️" },
  ghost: { color: "#705898", emoji: "👻" },
  dragon: { color: "#7038f8", emoji: "🐉" },
  dark: { color: "#705848", emoji: "🌑" },
  flying: { color: "#a8a8e8", emoji: "🦅" },
};

const getTypeStyle = (tipo) => {
  if (!tipo) return { color: "#9db3b3", emoji: "❓" };
  const normalized = tipo
    .toLowerCase()
    .trim()
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .replace(/\s+/g, "");
  return tiposConfig[normalized] || { color: "#9db3b3", emoji: "❓" };
};

const adoptar = async (poke) => {
  const modoShiny = !!poke.mostrarShiny;
  const textoForma = modoShiny ? "SHINY" : "NORMAL";

  if (
    !(await confirm(
      `¿Quieres intentar capturar a ${poke.nombre} (${textoForma})?`,
    ))
  )
    return;

  try {
    const response = await api.post("mis-pokemon/", {
      especie: poke.id,
      apodo: poke.nombre,
      en_equipo: false,
      es_shiny: modoShiny, // Enviamos la elección al backend
    });
    showAlert(
      `¡Gotcha! ${poke.nombre} ${textoForma} fue transferido al PC.`,
      "success",
    );
    // Reset mostrarShiny después de capturar
    poke.mostrarShiny = false;
  } catch (error) {
    console.error(error);
    showAlert(
      "Error al capturar. Quizás ya tienes demasiados de esta especie.",
      "error",
    );
  }
};

onMounted(async () => {
  try {
    const res = await api.get("pokedex/");
    // Inicializamos mostrarShiny en false para cada pokemon cargado
    pokemons.value = res.data.map((p) => ({ ...p, mostrarShiny: false }));
    // Si vienen query params desde otra vista, inicializamos búsqueda
    if (route.query.name) searchName.value = route.query.name;
    if (route.query.num) searchNumber.value = route.query.num;
  } catch (e) {
    console.error(e);
    showAlert("Error al cargar pokédex.", "error");
  } finally {
    cargando.value = false;
  }
});
</script>

<template>
  <div class="page-shell">
    <div class="page-card">
      <div class="pokedex-container">
        <div class="pokedex-header">
          <h2>
            <i class="bi bi-book-half" aria-hidden="true"></i> POKÉDEX DE KANTO
          </h2>
          <router-link to="/dashboard" class="btn-volver"
            ><i
              class="bi bi-arrow-left"
              aria-hidden="true"
              style="margin-right: 6px"></i>
            Volver al Inicio</router-link
          >
        </div>

        <div v-if="cargando" class="loading">Cargando base de datos...</div>

        <div v-else>
          <div
            class="search-bar"
            style="
              display: flex;
              gap: 10px;
              margin-bottom: 14px;
              align-items: center;
            ">
            <input
              v-model="searchName"
              placeholder="Buscar por nombre..."
              class="form-input"
              style="flex: 1" />
            <input
              v-model="searchNumber"
              placeholder="# Número"
              type="number"
              class="form-input"
              style="width: 120px" />
            <button
              @click="
                searchName = '';
                searchNumber = '';
              "
              class="btn-volver"
              style="padding: 8px 12px">
              Limpiar
            </button>
          </div>

          <div class="grid-pokedex">
            <div
              v-for="poke in filteredPokemons"
              :key="poke.id"
              class="poke-card"
              :class="{ 'card-shiny': poke.mostrarShiny }">
              <span class="num">N.º {{ poke.numero }}</span>

              <div class="sprite-container">
                <img
                  :src="
                    getLocalPath(
                      poke.mostrarShiny
                        ? poke.sprite_shiny_url
                        : poke.sprite_url,
                    )
                  "
                  :alt="poke.nombre" />

                <button
                  v-if="poke.sprite_shiny_url"
                  @click="poke.mostrarShiny = !poke.mostrarShiny"
                  class="btn-shiny-toggle"
                  :class="{ active: poke.mostrarShiny }"
                  title="Alternar forma Shiny">
                  <i class="bi bi-stars" aria-hidden="true"></i>
                </button>
              </div>

              <h3>{{ poke.nombre }}</h3>

              <div class="tipos-container">
                <span
                  class="tipo"
                  :style="{
                    backgroundColor: getTypeStyle(poke.tipo_principal).color,
                  }">
                  {{ getTypeStyle(poke.tipo_principal).emoji }}
                  {{ poke.tipo_principal }}
                </span>
                <span
                  v-if="poke.tipo_secundario"
                  class="tipo"
                  :style="{
                    backgroundColor: getTypeStyle(poke.tipo_secundario).color,
                  }">
                  {{ getTypeStyle(poke.tipo_secundario).emoji }}
                  {{ poke.tipo_secundario }}
                </span>
              </div>

              <button
                @click="adoptar(poke)"
                class="btn-adoptar"
                :class="{ 'btn-shiny': poke.mostrarShiny }">
                Capturar {{ poke.mostrarShiny ? "Shiny" : "" }}
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.pokedex-container {
  padding: 20px;
  max-width: 1200px;
  margin: 0 auto;
  color: var(--paragraph);
}

/* Inputs styled to match ListaTareas.vue */
.form-input {
  padding: 10px 12px;
  background: var(--elements-bg);
  border: 3px solid var(--stroke);
  color: var(--paragraph);
  font-family: inherit;
  font-size: 1.05rem;
  border-radius: 8px;
}

.form-input[type="number"] {
  width: 120px;
}

.pokedex-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 4px solid var(--secondary);
  padding-bottom: 15px;
  margin-bottom: 25px;
}

.pokedex-header h2 {
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

.grid-pokedex {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
  gap: 18px;
  margin-top: 20px;
}

.poke-card {
  background: rgba(242, 238, 245, 0.92);
  border-radius: 12px;
  padding: 14px;
  border: 3px solid var(--stroke);
  text-align: center;
  box-shadow: 8px 8px 0px rgba(153, 79, 243, 0.12);
  transition:
    transform 0.2s ease,
    box-shadow 0.2s ease,
    background 0.3s ease;
  display: flex;
  flex-direction: column;
}

.poke-card:hover {
  transform: translate(-2px, -2px);
  box-shadow: 10px 10px 0px rgba(153, 79, 243, 0.16);
}

.num {
  display: block;
  text-align: left;
  font-weight: 800;
  color: var(--secondary);
  font-size: 0.95rem;
  margin-bottom: 8px;
}

/* Contenedor sprite - ARREGLADO para mantener consistencia */
.sprite-container {
  position: relative;
  background: var(--elements-bg);
  border-radius: 8px;
  border: 3px solid var(--stroke);
  margin: 10px 0;
  padding: 8px;
  width: 100%;
  height: 120px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
  overflow: hidden;
}

.poke-card img {
  width: auto;
  height: auto;
  max-width: 100%;
  max-height: 100%;
  image-rendering: pixelated;
  object-fit: contain;
  transition: opacity 0.2s ease; /* Transición suave entre normal/shiny */
}

.poke-card h3 {
  color: var(--headline);
  text-transform: uppercase;
  margin: 8px 0;
  font-size: 1.3rem;
  font-weight: 800;
  letter-spacing: 0.5px;
}

.tipos-container {
  display: flex;
  gap: 6px;
  justify-content: center;
  margin: 8px 0;
  flex-wrap: wrap;
}

.tipo {
  padding: 6px 10px;
  border-radius: 6px;
  font-size: 0.85rem;
  border: 2px solid var(--stroke);
  text-transform: capitalize;
  font-weight: 700;
  color: white;
  text-shadow: 1px 1px 0px rgba(0, 0, 0, 0.3);
}

/* Botón flotante para cambiar a Shiny */
.btn-shiny-toggle {
  position: absolute;
  top: 5px;
  right: 5px;
  background: white;
  border: 2px solid var(--stroke);
  border-radius: 50%;
  width: 32px;
  height: 32px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.1rem;
  transition: all 0.2s;
  box-shadow: 2px 2px 0px var(--stroke);
  z-index: 2;
}

.btn-shiny-toggle:hover {
  transform: scale(1.05);
}

.btn-shiny-toggle.active {
  background: #f1c40f;
  transform: scale(1.2);
  box-shadow: 3px 3px 0px var(--stroke);
}

/* Card styling cuando es shiny */
.card-shiny {
  border-color: #f1c40f !important;
  background: linear-gradient(
    145deg,
    rgba(242, 238, 245, 0.92),
    rgba(255, 249, 200, 0.92)
  ) !important;
}

.btn-adoptar {
  background: var(--button);
  color: var(--button-text);
  border: 3px solid var(--stroke);
  padding: 10px 15px;
  cursor: pointer;
  font-weight: 800;
  font-size: 1rem;
  border-radius: 8px;
  margin-top: auto; /* Empuja el botón al fondo */
  width: 100%;
  text-transform: uppercase;
  transition: all 0.2s ease;
  box-shadow: 4px 4px 0px rgba(24, 24, 24, 0.9);
}

.btn-adoptar:hover {
  background: var(--tertiary);
  transform: translate(-2px, -2px);
  box-shadow: 6px 6px 0px rgba(24, 24, 24, 0.9);
}

.btn-adoptar:active {
  transform: translate(2px, 2px);
  box-shadow: 2px 2px 0px rgba(24, 24, 24, 0.9);
}

.btn-shiny {
  background: #f1c40f !important;
  color: #333 !important;
}

@media (max-width: 768px) {
  .pokedex-header {
    flex-direction: column;
    gap: 12px;
    align-items: flex-start;
  }

  .pokedex-header h2 {
    font-size: 1.6rem;
  }

  .grid-pokedex {
    grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
    gap: 15px;
  }

  .poke-card {
    padding: 12px;
  }

  .sprite-container {
    height: 110px;
  }
}

@media (max-width: 480px) {
  .pokedex-container {
    padding: 12px;
  }

  .pokedex-header h2 {
    font-size: 1.4rem;
  }

  .grid-pokedex {
    grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
    gap: 12px;
  }

  .poke-card {
    padding: 10px;
  }

  .sprite-container {
    height: 100px;
    padding: 6px;
  }

  .btn-adoptar {
    padding: 8px 12px;
    font-size: 0.9rem;
  }

  .btn-shiny-toggle {
    width: 28px;
    height: 28px;
    font-size: 0.9rem;
  }
}
</style>
