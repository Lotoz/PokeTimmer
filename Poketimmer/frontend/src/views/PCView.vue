<script setup>
import { ref, onMounted, computed } from "vue";
import api from "../api/axios";

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
      alert("¡Tu equipo está lleno! Mueve uno a la caja primero.");
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
    alert("Error de conexión con el servidor de PC.");
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
            >⬅ Apagar PC</router-link
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
                @click="moverPokemon(poke)">
                <div class="sprite-bg">
                  <img :src="poke.especie_info.sprite_url" alt="" />
                </div>
                <div class="info">
                  <strong>{{ poke.apodo || poke.especie_info.nombre }}</strong>
                  <span>Nv. {{ poke.nivel }}</span>
                  <span class="flecha">Depositar ➡ </span>
                </div>
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
                @click="moverPokemon(poke)">
                <div class="sprite-bg">
                  <img :src="poke.especie_info.sprite_url" alt="" />
                </div>
                <div class="info">
                  <strong>{{ poke.apodo || poke.especie_info.nombre }}</strong>
                  <span>Nv. {{ poke.nivel }}</span>
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
  grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
}

.card-mini {
  display: flex;
  align-items: center;
  gap: 15px;
  background: var(--elements-bg);
  padding: 12px;
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
  gap: 5px;
  position: relative;
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
  font-size: 1.2rem;
}
.info strong {
  color: var(--headline);
  text-transform: uppercase;
  text-shadow: 1px 1px #000;
}
.info span {
  color: var(--tertiary);
}

.flecha {
  color: #e74c3c;
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
</style>
