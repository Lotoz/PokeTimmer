<script setup>
defineProps({
  equipo: Array,
});
</script>

<template>
  <section class="panel equipo-panel">
    <h3>Tu Equipo Actual ({{ equipo.length }}/6)</h3>
    <div class="pokemon-grid">
      <div v-for="poke in equipo" :key="poke.id" class="poke-card">
        <div class="poke-sprite-wrapper">
          <img :src="poke.especie_info.sprite_url" :alt="poke.apodo" />
        </div>
        <div class="poke-info">
          <span class="poke-name">{{
            poke.apodo || poke.especie_info.nombre
          }}</span>
          <div class="barra-exp">
            <div
              class="fill"
              :style="{
                width: (poke.exp_actual / poke.exp_siguiente_nivel) * 100 + '%',
              }" />
          </div>
          <span class="poke-lvl">Nv. {{ poke.nivel }}</span>
        </div>
      </div>
      <div
        v-for="n in 6 - equipo.length"
        :key="'empty-' + n"
        class="poke-card empty-slot">
        <span>Espacio Libre</span>
      </div>
    </div>
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
.equipo-panel {
  height: auto;
}
.pokemon-grid {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  gap: 15px;
}
.poke-card {
  background: #fc9a9a;
  border-radius: 10px;
  padding: 10px;
  text-align: center;
  border: 2px solid #7f8c8d;
}
.poke-sprite-wrapper {
  background: #ecf0f1;
  border-radius: 50%;
  width: 80px;
  height: 80px;
  margin: 0 auto 10px;
  display: flex;
  justify-content: center;
  align-items: center;
  border: 3px solid #bdc3c7;
}
.poke-card img {
  width: 70px;
  height: 70px;
  image-rendering: pixelated;
}
.poke-info {
  display: flex;
  flex-direction: column;
}
.poke-name {
  font-weight: bold;
  font-size: 1.2rem;
  margin-bottom: 5px;
}
.barra-exp {
  height: 6px;
  background: #2c3e50;
  border-radius: 3px;
  margin-bottom: 5px;
  overflow: hidden;
}
.barra-exp .fill {
  height: 100%;
  background: #2bff2b;
}
.poke-lvl {
  color: #733fff;
}
.empty-slot {
  border: 2px dashed #7f8c8d;
  background: transparent;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #7f8c8d;
}
</style>
