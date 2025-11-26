<script setup>

</script>

<template>
  <header>
    <nav>
      <h1>Agenda de Contactos (SPA)</h1>
    </nav>
  </header>

  <main>
  
    <router-view /> 
  </main>
</template>

<style scoped>
/* Estilos para el encabezado */
nav {
  padding: 1em 0;
  border-bottom: 2px solid #ddd; 
  margin-bottom: 20px;
  text-align: center;
  background-color: #f8f8f8;
  color: #35495e;
}

h1 {
  font-size: 1.5em;
  margin: 0;
}
</style>