<template>
<div id="register-fondo">
<div class="container">
<div class=" justify-content-center  h-100 ">
    <div class=" card col-xs-12 col-sm-8 col-md-6 col-sm-offset-2 col-md-offset-3">
		<div role="form">
			<h2>Regístrate <small>La única verdad es la música!</small></h2>
			<hr class="colorgraph">
			<!---<div class="row">
				<div class="col-xs-12 col-sm-6 col-md-6">
					<div class="form-group">
                        <input type="text" name="first_name" id="first_name" class="form-control input-lg" placeholder="Nombre" tabindex="1">
					</div>
				</div>
				<div class="col-xs-12 col-sm-6 col-md-6">
					<div class="form-group">
						<input type="text" name="last_name" id="last_name" class="form-control input-lg" placeholder="Apellido" tabindex="2">
					</div>
				</div>
			</div>-->
			<div class="form-group">
				<input v-model="nombre" type="text" name="display_name" id="display_name" class="form-control input-lg" placeholder="Nombre de Usuario" tabindex="3">
			</div>
			<div class="form-group">
				<input v-model="correo" type="email" name="email" id="email" class="form-control input-lg" placeholder="Email" tabindex="4">
			</div>
			<div class="row">
				<div class="col-xs-12 col-sm-6 col-md-6">
					<div class="form-group">
						<input  v-model="password" type="password" name="password" id="password" class="form-control input-lg" placeholder="Contraseña" tabindex="5" ref="password">
					</div>
				</div>
				<div class="col-xs-12 col-sm-6 col-md-6">
					<div class="form-group">
						<input type="password" name="password_confirmation" id="confirme contraseña" class="form-control input-lg" placeholder="Confirm Password" tabindex="6" data-vv-as="password">
					</div>
				</div>
			</div>
			<div class="row">
				<div class="col-xs-4 col-sm-3 col-md-3">
					<span class="button-checkbox">
						<button type="button" class="btn" data-color="info" tabindex="7">I Agree</button>
                        <input type="checkbox" name="t_and_c" id="t_and_c" class="hidden" value="1">
					</span>
				</div>
				<div class="col-xs-8 col-sm-9 col-md-9 letra">
					 Haciendo Click <strong class="label label-primary">Aceptar</strong>, Estás de acuerdo con <a href="#" data-toggle="modal" data-target="#t_and_c_m">Términos y condiciones</a> Establecido por este sitio, incluyendo el uso de Cookies.
				</div>
			</div>
			
			<hr class="colorgraph">
			<div class="row">
				<div class="col-xs-12 col-md-6"><button class="btn btn-primary btn-block btn-lg" @click="registrar()">registrar</button></div>
				<div class="col-xs-12 col-md-6"><button class="btn btn-success btn-block btn-lg" @click="Ingresar()">ingresar</button></div>
			</div>
		</div>
	</div>
</div>
<!-- Modal -->
<div class="modal fade" id="t_and_c_m" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
	<div class="modal-dialog modal-lg">
		<div class="modal-content">
			<div class="modal-header">
				<button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
				<h4 class="modal-title" id="myModalLabel">Terminos y condiciones</h4>
			</div>
			<div class="modal-body">
				<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Similique, itaque, modi, aliquam nostrum at sapiente consequuntur natus odio reiciendis perferendis rem nisi tempore possimus ipsa porro delectus quidem dolorem ad.</p>
				<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Similique, itaque, modi, aliquam nostrum at sapiente consequuntur natus odio reiciendis perferendis rem nisi tempore possimus ipsa porro delectus quidem dolorem ad.</p>
				<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Similique, itaque, modi, aliquam nostrum at sapiente consequuntur natus odio reiciendis perferendis rem nisi tempore possimus ipsa porro delectus quidem dolorem ad.</p>
				<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Similique, itaque, modi, aliquam nostrum at sapiente consequuntur natus odio reiciendis perferendis rem nisi tempore possimus ipsa porro delectus quidem dolorem ad.</p>
				<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Similique, itaque, modi, aliquam nostrum at sapiente consequuntur natus odio reiciendis perferendis rem nisi tempore possimus ipsa porro delectus quidem dolorem ad.</p>
				<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Similique, itaque, modi, aliquam nostrum at sapiente consequuntur natus odio reiciendis perferendis rem nisi tempore possimus ipsa porro delectus quidem dolorem ad.</p>
				<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Similique, itaque, modi, aliquam nostrum at sapiente consequuntur natus odio reiciendis perferendis rem nisi tempore possimus ipsa porro delectus quidem dolorem ad.</p>
			</div>
			<div class="modal-footer">
				<button type="button" class="btn btn-primary" data-dismiss="modal">Estoy de acuerdo</button>
			</div>
		</div><!-- /.modal-content -->
	</div><!-- /.modal-dialog -->
</div><!-- /.modal -->
</div>
</div>

</template>
<style scoped>
    /* Credit to bootsnipp.com for the css for the color graph */
.colorgraph {
    height: 20px;
    border-top: 0;
    background: #c4e17f;
    border-radius: 5px;
    background-image: -webkit-linear-gradient(left, #c4e17f, #c4e17f 12.5%, #f7fdca 12.5%, #f7fdca 25%, #fecf71 25%, #fecf71 37.5%, #f0776c 37.5%, #f0776c 50%, #db9dbe 50%, #db9dbe 62.5%, #c49cde 62.5%, #c49cde 75%, #669ae1 75%, #669ae1 87.5%, #62c2e4 87.5%, #62c2e4);
    background-image: -moz-linear-gradient(left, #c4e17f, #c4e17f 12.5%, #f7fdca 12.5%, #f7fdca 25%, #fecf71 25%, #fecf71 37.5%, #f0776c 37.5%, #f0776c 50%, #db9dbe 50%, #db9dbe 62.5%, #c49cde 62.5%, #c49cde 75%, #669ae1 75%, #669ae1 87.5%, #62c2e4 87.5%, #62c2e4);
    background-image: -o-linear-gradient(left, #c4e17f, #c4e17f 12.5%, #f7fdca 12.5%, #f7fdca 25%, #fecf71 25%, #fecf71 37.5%, #f0776c 37.5%, #f0776c 50%, #db9dbe 50%, #db9dbe 62.5%, #c49cde 62.5%, #c49cde 75%, #669ae1 75%, #669ae1 87.5%, #62c2e4 87.5%, #62c2e4);
    background-image: linear-gradient(to right, #c4e17f, #c4e17f 12.5%, #f7fdca 12.5%, #f7fdca 25%, #fecf71 25%, #fecf71 37.5%, #f0776c 37.5%, #f0776c 50%, #db9dbe 50%, #db9dbe 62.5%, #c49cde 62.5%, #c49cde 75%, #669ae1 75%, #669ae1 87.5%, #62c2e4 87.5%, #62c2e4);
  }
  .register-fondo{
    background-image: 'url(' + require('@/assets/css/img/fondo.jpg') + ')';
    background-size: cover;
    background-repeat: no-repeat;
    height: 100%;
    font-family: 'Numans', sans-serif;
    font-size: large;
    }
    .card{
        height: 100%;
        padding-bottom: 3%;
    }
    .container{
        height: 100%;
        display: flex;
        margin-top: 20px;
        margin-left: 30%;
        }
    h2{
        color: white;
    }
    .letra{
        color: white;
    }
    .btn{
        color: white;
    }
</style>
<script>
import Axios from "axios";
export default {
	data(){
		return{
        nombre: '',
		correo:'',
        password: ''
        }
	},
	methods: {
		register(){
			Axios.post('http://127.0.0.1:5000/user/register',{
				nombre: this.nombre,
				correo: this.correo,
				password: this.password
			}).then( res => {
				console.log(res.data)
				if(res.data.ok){
					swal({
						title: 'Usuario creado',
                    	text: 'Datos correctos',
                    	icon: 'success',
                    	closeOnClickOutside: false,
                    	closeOnEsc: false
					}).then( select => {
						if(select){
							this.$router.push({path:'/login'})
						}
					})
				}
			}).catch( err => {
				console.log(err)
			})
		},

		Ingresar(){
			Axios.post('http://127.0.0.1:5000/user/register',{
				nombre: this.nombre,
				correo: this.correo,
				password: this.password
			}).then( res => {
				console.log(res.data)
				if(res.data.ok){
					swal({
						title: 'Usuario creado',
                    	text: 'Datos correctos',
                    	icon: 'success',
                    	closeOnClickOutside: false,
                    	closeOnEsc: false
					}).then( select => {
						if(select){
							this.$router.push({path:'/inicio'})
							localStorage.setItem('user_id', res.data.user_id)
						}
					})
				}
			}).catch( err => {
				console.log(err)
			});
		}
	},
}
</script>