<script setup></script>

<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<style>
@import url("https://fonts.googleapis.com/css2?family=VT323&display=swap");

/* Estilos globales */
* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: "VT323", monospace; /* Fuente estilo pixel/retro */
  font-size: 1.2rem;
  background-color: #320000;
  color: #ecf0f1;
}

h1,
h2,
h3 {
  margin-top: 0;
  color: #f1c40f;
  text-shadow: 2px 2px #020000;
}

button {
  font-family: "VT323", monospace;
  font-size: 1.2rem;
  transition:
    transform 0.1s,
    filter 0.2s;
}

button:active {
  transform: scale(0.95);
}

/* Scrollbar personalizado */
::-webkit-scrollbar {
  width: 8px;
}
::-webkit-scrollbar-track {
  background: #002346;
}
::-webkit-scrollbar-thumb {
  background: #42b983;
  border-radius: 4px;
}
</style>
