<script setup>
import { ref, onMounted } from "vue";
import api from "../api/axios";

const pokemons = ref([]);
const cargando = ref(true);

const adoptar = async (poke) => {
  if (!confirm(`¿Quieres intentar capturar a ${poke.nombre}?`)) return;

  try {
    await api.post("mis-pokemon/", {
      especie: poke.id,
      apodo: poke.nombre,
      en_equipo: false,
    });
    alert(`¡Gotcha! ${poke.nombre} fue transferido al PC.`);
  } catch (error) {
    console.error(error);
    alert("Error al capturar. Quizás ya tienes demasiados de esta especie.");
  }
};

onMounted(async () => {
  try {
    const res = await api.get("pokedex/");
    pokemons.value = res.data;
  } catch (e) {
    console.error(e);
  } finally {
    cargando.value = false;
  }
});
</script>

<template>
  <div class="pokedex-container">
    <div class="pokedex-header">
      <h2>POKÉDEX DE KANTO</h2>
      <router-link to="/dashboard" class="btn-volver"
        >⬅ Volver al Centro</router-link
      >
    </div>

    <div v-if="cargando" class="loading">Cargando base de datos...</div>

    <div class="grid-pokedex">
      <div v-for="poke in pokemons" :key="poke.id" class="poke-card">
        <span class="num">N.º {{ poke.numero }}</span>
        <div class="sprite-container">
          <img :src="poke.sprite_url" :alt="poke.nombre" />
        </div>
        <h3>{{ poke.nombre }}</h3>
        <span class="tipo">{{ poke.tipo_principal }}</span>

        <button @click="adoptar(poke)" class="btn-adoptar">
          Lanzar Poké Ball
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.pokedex-container {
  padding: 20px;
  max-width: 1200px;
  margin: 0 auto;
  color: #ecf0f1;
}
.pokedex-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 6px solid #c0392b;
  padding-bottom: 10px;
  margin-bottom: 20px;
}
.pokedex-header h2 {
  color: #e74c3c;
  margin: 0;
  font-size: 2.5rem;
  text-shadow: 2px 2px #000;
}
.btn-volver {
  background: #34495e;
  color: white;
  padding: 10px 20px;
  text-decoration: none;
  border: 4px solid #2c3e50;
  border-radius: 5px;
  font-weight: bold;
}
.btn-volver:hover {
  background: #2c3e50;
}
.loading {
  font-size: 1.5rem;
  text-align: center;
  margin-top: 50px;
  color: #f1c40f;
  animation: blink 1s infinite;
}
@keyframes blink {
  50% {
    opacity: 0;
  }
}

.grid-pokedex {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 20px;
}
.poke-card {
  background: #e74c3c;
  border-radius: 10px;
  padding: 15px;
  border: 4px solid #c0392b;
  text-align: center;
  box-shadow: 5px 5px 0px rgba(0, 0, 0, 0.3);
}
.num {
  display: block;
  text-align: left;
  font-weight: bold;
  color: #f1c40f;
  font-size: 1.2rem;
}
.sprite-container {
  background: #ecf0f1;
  border-radius: 5px;
  border: 4px solid #bdc3c7;
  margin: 10px 0;
  padding: 10px;
}
.poke-card img {
  width: 100px;
  height: 100px;
  image-rendering: pixelated;
}
.poke-card h3 {
  color: white;
  text-transform: uppercase;
  margin: 10px 0 5px;
  font-size: 1.5rem;
  text-shadow: 1px 1px #000;
}
.tipo {
  background: #34495e;
  padding: 4px 10px;
  border-radius: 3px;
  font-size: 1rem;
  border: 2px solid #2c3e50;
  text-transform: uppercase;
}
.btn-adoptar {
  background: #f1c40f;
  color: #333;
  border: 4px solid #f39c12;
  padding: 8px 15px;
  cursor: pointer;
  font-weight: bold;
  font-size: 1.2rem;
  border-radius: 5px;
  margin-top: 15px;
  width: 100%;
  text-transform: uppercase;
}
.btn-adoptar:hover {
  background: #f39c12;
}
</style>
