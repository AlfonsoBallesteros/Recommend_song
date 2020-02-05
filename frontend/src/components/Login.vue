<template>
<div class="bg-container">
    <div class="container">
	<div class="d-flex justify-content-center h-100">
		<div class="card">
        <br>
			<div class="card-header">
				<h3>Ingresar</h3>
				<div class="d-flex justify-content-end social_icon">
					<span><i class="fab fa-facebook-square"></i></span>
					<span><i class="fab fa-google-plus-square"></i></span>
					<span><i class="fab fa-twitter-square"></i></span>
				</div>
			</div>
			<div class="card-body">
				<form id="login">
					<div class="input-group form-group">
						<div class="input-group-prepend " >
							<span class="input-group-text"><i class="fas fa-user"></i></span>
						</div>
                        <input v-model="usuario" type="email" class="form-control" name="uname1" id="uname1" required="" placeholder="usuario">
                        <div class="invalid-feedback" style="color: aliceblue;">Oops, debes ingresar un nombre de usuario.</div>
						
					</div>
					<div class="input-group form-group">
						<div class="input-group-prepend">
							<span class="input-group-text"><i class="fas fa-key"></i></span>
						</div>
						<input v-model="password" type="password" class="form-control  rounded-0" id="pwd1" required="" autocomplete="new-password" placeholder="password">
                        <div class="invalid-feedback" style="color: aliceblue;">Ingresa tu contraseña también!</div>
                    </div>
					<div class="row align-items-center remember">
						<input type="checkbox">Recordarme
					</div>
					<div class="form-group">
                        <button type="button" class="btn float-right login_btn" @click="login()">Login</button>
					</div>
				</form>
			</div>
			<div class="card-footer">
				<div class="d-flex justify-content-center links">
					No tienes una cuenta?<a href="">Registrarme</a>
				</div>
				<div class="d-flex justify-content-center">
					<a href="#">Olvidaste tu contraseña?</a>
				</div>
			</div>
		</div>
	</div>
</div>
</div>
</template>
<style scoped>
    @import url('https://fonts.googleapis.com/css?family=Numans');

    .login-fondo{
    background-image: 'url(' + require('@/assets/img/fondo.png') + ')';
    background-size: cover;
    background-repeat: no-repeat;
    height: 100%;
    font-family: 'Numans', sans-serif;
    }

    .container{
    height: 100%;
    align-content: center;
    margin: 20px;
    }

    .card{
    height: 370px;
    margin-top: auto;
    margin-bottom: auto;
    width: 400px;
    background-color: rgba(0,0,0,0.5) !important;
    margin-left: 35%;
    }

    .social_icon span{
    font-size: 60px;
    margin-left: 10px;
    color: #FFC312;
    }

    .social_icon span:hover{
    color: white;
    cursor: pointer;
    }

    .card-header h3{
    color: white;
    }

    .social_icon{
    position: absolute;
    right: 20px;
    top: -45px;
    }

    .input-group-prepend span{
    width: 50px;
    background-color: #FFC312;
    color: black;
    border:0 !important;
    }

    input:focus{
    outline: 0 0 0 0  !important;
    box-shadow: 0 0 0 0 !important;

    }

    .remember{
    color: white;
    }

    .remember input
    {
    width: 20px;
    height: 20px;
    margin-left: 15px;
    margin-right: 5px;
    }

    .login_btn{
    color: black;
    background-color: #FFC312;
    width: 100px;
    }

    .login_btn:hover{
    color: black;
    background-color: white;
    }

    .links{
    color: white;
    }

    .links a{
    margin-left: 4px;
    }

</style>
<script>
import Axios from "axios";
import router from "../main";

export default {
    data(){
        return{
        usuario: '',
        password: ''
        }
    },
    methods: {
        login(){
            Axios.post('http://127.0.0.1:5000/user/login',{
                correo: this.usuario,
                password: this.password
            }).then( res => {
                if(res.data == 'usuario incorrecto'){
                    console.log(res.data)
                    swal({
                        title: 'Usuario incorrecto',
                        text: 'Datos incorrectos',
                        icon: 'error',
                        closeOnClickOutside: false,
                        closeOnEsc: false
                    })
                }else if(res.data == 'contraseña incorrecta'){
                    console.log(res.data)
                    swal({
                        title: 'Contraseña incorrecta',
                        text: 'Datos incorrectos',
                        icon: 'error',
                        closeOnClickOutside: false,
                        closeOnEsc: false
                    })
                }else{
                    console.log((res.data.user_id))
                    swal({
                        title: 'Has iniciado sesion',
                        text: 'Datos correctos',
                        icon: 'success',
                        closeOnClickOutside: false,
                        closeOnEsc: false
                    }).then( select =>{
                        if( select ){
                            this.$router.push({path:'/inicio'})
                            localStorage.setItem('user_id', res.data.user_id)
                        //window.location.href = '/app#/cliente'  
                        }
                    });
                }
            }).catch( error => {
                
            });
        }
    },
    
}

</script>
