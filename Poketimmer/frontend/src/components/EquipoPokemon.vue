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
  background: rgba(242, 238, 245, 0.96);
  border-radius: 12px;
  padding: 18px;
  border: 3px solid var(--stroke);
  box-shadow: 8px 8px 0px rgba(153, 79, 243, 0.06);
}
.equipo-panel {
  height: auto;
}
.pokemon-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(110px, 1fr));
  gap: 12px;
}
.poke-card {
  background: var(--elements-bg);
  border-radius: 10px;
  padding: 12px;
  text-align: center;
  border: 3px solid var(--stroke);
}
.poke-sprite-wrapper {
  background: var(--main);
  border-radius: 50%;
  width: 80px;
  height: 80px;
  margin: 0 auto 10px;
  display: flex;
  justify-content: center;
  align-items: center;
  border: 3px solid var(--stroke);
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
  font-weight: 800;
  font-size: 1.05rem;
  margin-bottom: 6px;
  color: var(--headline);
}
.barra-exp {
  height: 8px;
  background: rgba(0, 0, 0, 0.06);
  border-radius: 6px;
  margin-bottom: 6px;
  overflow: hidden;
}
.barra-exp .fill {
  height: 100%;
  background: var(--highlight);
}
.poke-lvl {
  color: var(--secondary);
  font-weight: 700;
}
.empty-slot {
  border: 2px dashed rgba(0, 0, 0, 0.08);
  background: transparent;
  display: flex;
  align-items: center;
  justify-content: center;
  color: rgba(0, 0, 0, 0.5);
}

@media (max-width: 720px) {
  .pokemon-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}
</style>
