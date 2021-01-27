<template>
  <div id="app">
    <h1>Chess Goat</h1>
    <Chessboard />
  </div>
</template>

<script>
import Chessboard from './templates/chessboard.vue'


export default {
  name: 'App',
  components: {
    Chessboard
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

h1 {
  color:"Red";
}
</style>
