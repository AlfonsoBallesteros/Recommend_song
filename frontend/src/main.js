import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import Inicio from './components/Inicio.vue'
import Login from './components/Login.vue'
import Register from './components/Register.vue'
import Cancion from './components/Cancion.vue'
import index from './components/index.vue'
import CancionID from './components/CancionID.vue'
import 'bootstrap'; 
import 'jquery';

import 'popper.js';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle'

import swal from 'sweetalert';

Vue.use(VueRouter)

 
const router = new VueRouter({
    routes: [{
       // rutas aqui
       name: 'inicio',
       path: '/inicio',
       component: Inicio
    },{
      name: 'login',
      path: '/',
      component: Login
    },
    {
      name: 'register',
      path: '/register',
      component: Register
    },
    {
      name: 'cancion',
      path: '/cancion',
      component: Cancion
    },
    {
      name: 'index',
      path: '/index',
      component: index
    },
    {
      name: 'cancionID',
      path: '/cancion/id/:id',
      component: CancionID
    }
  
  ],
  mode: 'history'
});

Vue.component('inicio',require('./components/Inicio').default);

new Vue({
  el: '#app',
  router,
  component: {App},
  template: '<app/>',

  render: h => h(App)
})
