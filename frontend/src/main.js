import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import Inicio from './components/Inicio.vue'
import Login from './components/Login.vue'
import Register from './components/Register.vue'
import 'bootstrap'; 
import 'bootstrap/dist/css/bootstrap.min.css';
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
