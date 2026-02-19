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
  <div class="pc-container">
    <div class="pc-header">
      <h2>SISTEMA DE ALMACENAMIENTO</h2>
      <router-link to="/dashboard" class="btn-volver">⬅ Apagar PC</router-link>
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
            </div>
            <span class="flecha">Depositar ➡</span>
          </div>
        </div>
      </div>

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
            <span class="flecha-hover">⬅ Retirar</span>
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
  color: white;
}
.pc-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 6px solid #2980b9;
  padding-bottom: 10px;
  margin-bottom: 20px;
}
.pc-header h2 {
  color: #3498db;
  margin: 0;
  font-size: 2.5rem;
  text-shadow: 2px 2px #000;
}
.btn-volver {
  background: #e74c3c;
  color: white;
  padding: 10px 20px;
  text-decoration: none;
  border: 4px solid #c0392b;
  border-radius: 5px;
  font-weight: bold;
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
  background: #2c3e50;
  padding: 20px;
  border-radius: 10px;
  border: 6px solid #34495e;
  box-shadow: inset 0 0 15px rgba(0, 0, 0, 0.5);
  overflow-y: auto;
  max-height: 75vh;
}

.box-title {
  text-align: center;
  background: #f1c40f;
  color: #333;
  padding: 8px;
  border-radius: 3px;
  border: 4px solid #f39c12;
  margin-bottom: 20px;
  font-size: 1.5rem;
}
.equipo-col .box-title {
  background: #2ecc71;
  border-color: #27ae60;
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
  background: #34495e;
  padding: 10px;
  border-radius: 8px;
  cursor: pointer;
  border: 4px solid #2c3e50;
  transition:
    transform 0.1s,
    border-color 0.2s;
}
.card-mini:hover {
  border-color: #f1c40f;
  transform: scale(1.02);
}

.caja-mini {
  flex-direction: column;
  text-align: center;
  gap: 5px;
  position: relative;
}
.sprite-bg {
  background: #ecf0f1;
  border-radius: 50%;
  padding: 5px;
  border: 4px solid #bdc3c7;
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
  color: #fff;
  text-transform: uppercase;
  text-shadow: 1px 1px #000;
}
.info span {
  color: #f1c40f;
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
