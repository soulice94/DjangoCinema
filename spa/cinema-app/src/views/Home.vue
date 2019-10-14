<template>
  <div class="home">
    <h1>Powered by Vue!</h1>
    <img alt="Vue logo" src="../assets/logo.png">
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue';
import axios from 'axios';

const url = 'localhost:8000/cinema/api/';

export default {
  name: 'home',
  created() {
    const config = {
      'Access-Control-Allow-Origin': '*'
    };
    return axios.get(`${url}movies/`, config)
      .then(response => {
        console.log(response);
      });
  },
};
</script>
