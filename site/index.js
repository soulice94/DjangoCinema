const url = 'localhost:8000/cinema/api/';

new Vue({
  el: '#app',
  data() {
    return {
      message: 'hey',
      movieList: Array,
    }
  },
  created() {
    return axios.get(`${url}movies/`)
      .then(response => {
        console.log(response);
      });
  },
})