<script setup>
import { ref, onMounted, computed } from "vue";
import api from "../api/axios";
import { getLocalPath } from "../utils/imagePaths";

const pokemonBox = ref([]);
const cargando = ref(true);

const equipo = computed(() => pokemonBox.value.filter((p) => p.en_equipo));
const caja = computed(() => pokemonBox.value.filter((p) => !p.en_equipo));

const cargarPC = async () => {
  try {
    const res = await api.get("mis-pokemon/");
    pokemonBox.value = res.data;
  } catch (e) {
    console.error(e);
  } finally {
    cargando.value = false;
  }
};

const moverPokemon = async (poke) => {
  if (poke.en_equipo) {
    await actualizarEstado(poke, false);
  } else {
    if (equipo.value.length >= 6) {
      await alert("¡Tu equipo está lleno! Mueve uno a la caja primero.");
      return;
    }
    await actualizarEstado(poke, true);
  }
};

const actualizarEstado = async (poke, nuevoEstado) => {
  try {
    await api.patch(`mis-pokemon/${poke.id}/`, {
      en_equipo: nuevoEstado,
    });
    poke.en_equipo = nuevoEstado;
  } catch (e) {
    await alert("Error de conexión con el servidor de PC.");
  }
};

const liberarPokemon = async (poke, event) => {
  event.stopPropagation();

  const nombrePoke = poke.apodo || poke.especie_info.nombre;
  if (!(await confirm(`¿Liberar a ${nombrePoke}? ¡No podrás recuperarlo!`)))
    return;

  try {
    await api.delete(`mis-pokemon/${poke.id}/`);
    pokemonBox.value = pokemonBox.value.filter((p) => p.id !== poke.id);
  } catch (e) {
    await alert("Error al liberar el Pokémon.");
  }
};

const cambiarApodo = async (poke, event) => {
  event.stopPropagation();

  const nuevoApodo = await window.prettyDialog.prompt(
    poke.apodo || poke.especie_info.nombre,
    "Renombrar Pokémon",
    poke.apodo || poke.especie_info.nombre,
  );

  if (nuevoApodo === null || nuevoApodo === undefined) return; // Canceló

  if (nuevoApodo.trim() === "") {
    await alert("El apodo no puede estar vacío");
    return;
  }

  try {
    await api.patch(`mis-pokemon/${poke.id}/`, {
      apodo: nuevoApodo.trim(),
    });
    poke.apodo = nuevoApodo.trim();
  } catch (e) {
    await alert("Error al cambiar el apodo.");
  }
};

const alternarPiedraEterna = async (poke, event) => {
  event.stopPropagation();

  const estado = poke.piedra_eterna ? "activada" : "desactivada";
  const accion = poke.piedra_eterna ? "quitar la" : "poner la";

  if (
    !(await confirm(
      `¿${accion} Piedra Eterna a ${poke.apodo || poke.especie_info.nombre}?`,
    ))
  )
    return;

  try {
    await api.patch(`mis-pokemon/${poke.id}/`, {
      piedra_eterna: !poke.piedra_eterna,
    });
    poke.piedra_eterna = !poke.piedra_eterna;
  } catch (e) {
    await alert("Error al cambiar el estado de la Piedra Eterna.");
  }
};

onMounted(() => {
  cargarPC();
});
</script>

<template>
  <div class="page-shell">
    <div class="page-card">
      <div class="pc-container">
        <div class="pc-header">
          <h2>SISTEMA DE ALMACENAMIENTO</h2>
          <router-link to="/dashboard" class="btn-volver"
            ><i
              class="bi bi-power"
              aria-hidden="true"
              style="margin-right: 6px"></i>
            Apagar PC</router-link
          >
        </div>

        <div v-if="cargando" class="loading">Iniciando sistema...</div>

        <div class="pc-layout" v-else>
          <div class="columna equipo-col">
            <h3 class="box-title">EQUIPO ACTIVO ({{ equipo.length }}/6)</h3>
            <div class="grid">
              <div
                v-for="poke in equipo"
                :key="poke.id"
                class="card-mini"
                @click="moverPokemon(poke)"
                :class="{ 'card-shiny': poke.es_shiny }">
                <div class="sprite-bg">
                  <img
                    :src="
                      getLocalPath(
                        poke.es_shiny
                          ? poke.especie_info.sprite_shiny_url
                          : poke.especie_info.sprite_url,
                      )
                    "
                    alt="" />
                </div>
                <div class="info">
                  <strong
                    class="nombre-pokemon"
                    @click.stop="cambiarApodo(poke, $event)"
                    title="Clic para renombrar"
                    >{{ poke.apodo || poke.especie_info.nombre }}</strong
                  >
                  <span>Nv. {{ poke.nivel }}</span>
                </div>
                <span class="flecha"
                  >Depositar <i class="bi bi-arrow-right" aria-hidden="true"></i
                ></span>
              </div>
            </div>
          </div>
          <br />
          <div class="columna caja-col">
            <h3 class="box-title">CAJA 1</h3>
            <div class="grid grid-caja">
              <div
                v-for="poke in caja"
                :key="poke.id"
                class="card-mini caja-mini"
                @click="moverPokemon(poke)"
                :class="{ 'card-shiny': poke.es_shiny }">
                <div class="sprite-bg">
                  <img
                    :src="
                      getLocalPath(
                        poke.es_shiny
                          ? poke.especie_info.sprite_shiny_url
                          : poke.especie_info.sprite_url,
                      )
                    "
                    alt="" />
                </div>
                <div class="info">
                  <strong
                    class="nombre-pokemon"
                    @click.stop="cambiarApodo(poke, $event)"
                    title="Clic para renombrar"
                    >{{ poke.apodo || poke.especie_info.nombre }}</strong
                  >
                  <span>Nv. {{ poke.nivel }}</span>
                </div>
                <br />
                <div class="acciones-pokemon">
                  <button
                    @click="cambiarApodo(poke, $event)"
                    class="btn-editar"
                    title="Renombrar Pokémon">
                    <i class="bi bi-pencil" aria-hidden="true"></i>
                  </button>
                  <button
                    @click="alternarPiedraEterna(poke, $event)"
                    class="btn-piedra"
                    :class="{ activa: poke.piedra_eterna }"
                    title="Piedra Eterna - Evita evolucionar">
                    🪨
                  </button>
                  <button
                    @click="liberarPokemon(poke, $event)"
                    class="btn-liberar"
                    title="Liberar Pokémon">
                    <i class="bi bi-trash" aria-hidden="true"></i>
                  </button>
                </div>
                <span class="flecha-hover"> ⬅ Retirar</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.pc-container {
  padding: 20px;
  max-width: 1200px;
  margin: 0 auto;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  color: var(--paragraph);
}
.pc-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 6px solid var(--secondary);
  padding-bottom: 10px;
  margin-bottom: 20px;
}
.pc-header h2 {
  color: var(--headline);
  margin: 0;
  font-size: 2.2rem;
}
.btn-volver {
  background: var(--tertiary);
  color: var(--headline);
  padding: 10px 20px;
  text-decoration: none;
  border: 4px solid var(--stroke);
  border-radius: 8px;
  font-weight: 800;
}
.loading {
  text-align: center;
  font-size: 2rem;
  color: #3498db;
  margin-top: 50px;
}

.pc-layout {
  display: flex;
  gap: 30px;
  flex-grow: 1;
}
.columna {
  flex: 1;
  background: rgba(242, 238, 245, 0.95);
  padding: 18px;
  border-radius: 12px;
  border: 4px solid var(--stroke);
  box-shadow: 6px 6px 0px rgba(153, 79, 243, 0.08) inset;
  overflow-y: auto;
  max-height: 75vh;
}

.box-title {
  text-align: center;
  background: var(--tertiary);
  color: var(--headline);
  padding: 8px;
  border-radius: 6px;
  border: 4px solid var(--stroke);
  margin-bottom: 20px;
  font-size: 1.25rem;
}
.equipo-col .box-title {
  background: var(--highlight);
  border-color: var(--stroke);
}

.grid {
  display: flex;
  flex-direction: column;
  gap: 15px;
}
.grid-caja {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
}

.card-mini {
  display: flex;
  align-items: center;
  gap: 15px;
  background: var(--elements-bg);
  padding: 16px;
  border-radius: 10px;
  cursor: pointer;
  border: 4px solid var(--stroke);
  transition:
    transform 0.1s,
    border-color 0.2s;
}
.card-mini:hover {
  transform: translateX(4px);
  border-color: var(--secondary);
}

.caja-mini {
  flex-direction: column;
  text-align: center;
  gap: 10px;
  position: relative;
  padding: 14px 12px;
  min-height: 220px;
  justify-content: space-between;
}
.sprite-bg {
  background: var(--main);
  border-radius: 50%;
  padding: 6px;
  border: 4px solid var(--stroke);
}
.card-mini img {
  width: 60px;
  height: 60px;
  image-rendering: pixelated;
}

.info {
  display: flex;
  flex-direction: column;
  gap: 4px;
  font-size: 3rem;
}
.info strong {
  color: var(--headline);
  text-transform: uppercase;
  text-shadow: 1px 1px #000;
  font-size: 1rem;
}
.info span {
  color: var(--tertiary);
  font-size: 0.85rem;
  font-weight: 700;
}

.flecha {
  color: #e74c3c !important;
  font-size: 1.2rem;
  margin-left: auto;
  font-weight: bold;
}

.flecha-hover {
  display: none;
  position: absolute;
  background: rgba(0, 0, 0, 0.85);
  color: #2ecc71;
  padding: 5px;
  border-radius: 3px;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-weight: bold;
  font-size: 1.4rem;
  z-index: 10;
  width: 90%;
  border: 2px solid #2ecc71;
}
.caja-mini:hover .flecha-hover {
  display: block;
}

/* Styling para Pokémon shiny */
.card-shiny {
  border-color: #f1c40f !important;
  background: linear-gradient(
    145deg,
    var(--elements-bg),
    rgba(255, 249, 200, 0.3)
  ) !important;
}

/* Contenedor de acciones */
.acciones-pokemon {
  display: flex;
  gap: 8px;
  justify-content: center;
  flex-wrap: wrap;
  width: 100%;
}

.btn-liberar {
  background: #e74c3c;
  border: 2px solid var(--stroke);
  border-radius: 50%;
  width: 28px;
  height: 28px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.9rem;
  transition: all 0.2s;
  box-shadow: 2px 2px 0px var(--stroke);
}

.btn-liberar:hover {
  transform: scale(1.1);
  background: #c0392b;
  box-shadow: 3px 3px 0px var(--stroke);
}

.btn-liberar:active {
  transform: scale(0.95);
  box-shadow: 1px 1px 0px var(--stroke);
}

.caja-mini {
  position: relative;
}

/* Nombre del Pokémon clickeable */
.nombre-pokemon {
  cursor: pointer;
  padding: 4px 8px;
  border-radius: 4px;
  transition: all 0.2s ease;
  display: inline-block;
}

.nombre-pokemon:hover {
  background: rgba(124, 77, 255, 0.2);
  text-decoration: underline;
}

/* Botón para editar apodo */
.btn-editar {
  background: #3498db;
  border: 2px solid var(--stroke);
  border-radius: 50%;
  width: 28px;
  height: 28px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.9rem;
  transition: all 0.2s;
  box-shadow: 2px 2px 0px var(--stroke);
}

.btn-editar:hover {
  transform: scale(1.1);
  background: #2980b9;
  box-shadow: 3px 3px 0px var(--stroke);
}

.btn-editar:active {
  transform: scale(0.95);
  box-shadow: 1px 1px 0px var(--stroke);
}

.btn-piedra {
  background: #95a5a6;
  border: 2px solid var(--stroke);
  border-radius: 50%;
  width: 28px;
  height: 28px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.9rem;
  transition: all 0.2s;
  box-shadow: 2px 2px 0px var(--stroke);
}

.btn-piedra:hover {
  transform: scale(1.1);
  box-shadow: 3px 3px 0px var(--stroke);
}

.btn-piedra:active {
  transform: scale(0.95);
  box-shadow: 1px 1px 0px var(--stroke);
}

.btn-piedra.activa {
  background: #f39c12;
  border-color: #d68910;
  box-shadow:
    0 0 8px rgba(243, 156, 18, 0.6),
    2px 2px 0px var(--stroke);
}
</style>
