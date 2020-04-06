<template>
<div class="bg-container">
  <div class="container m-l-a">

    <div class=" col-lg-12 col-md-12 col-sm-12 col-xs-12">
        <h1 class="h1"><strong>Escoge tus canciones favoritas</strong> </h1>
    </div>
<div class="row">
  <div v-for="(song,index) in songs" :key="index" class="card col-md-4 nopad text-center" style="height: 0% !important;">
    <button @click="checked(song._id.id, song._id.title, song._id.artist_name, song._id.release, song._id.year, song._id.song)">
    <label class="image-checkbox" :class="estilos">
      <img class="img-fluid" src="https://www.lavanguardia.com/r/GODO/LV/p5/WebSite/2018/02/19/Recortada/img_rpeco_20180219-142613_imagenes_lv_otras_fuentes_istock-108195157-kGfE-U44920520729RIE-992x558@LaVanguardia-Web.jpg" />
      <!---<input type="checkbox" name="image[]" value="true" v-model="checked" />-->
      
      <i class="fa fa-check hidden"></i>
    </label>
    </button>
    <div class="card-body">
      <h4 class="card-title cancion">{{song._id.title}}</h4>
      <h6 class="card-subtitle artista">{{song._id.artist_name}}</h6>
      <p class="release">{{song._id.release}}</p>
    </div>
  </div>
  
</div>
  <br><br>
  <div class="col-md-12">
      <button type="submit" class="btn btn-warning btn-lg btn-block" @click="recomendar()">Siguiente</button>
  </div>

</div>
</div>
</template>

<style>
 .artista{
  font-family: 'love';
	font-size: 20px;
	
	color: white;
 }
 .cancion{
   font-family: 'love';
	  font-size: 28px;
	  
	  color: white;
 }
 .release{
    font-family: 'love';
	  font-size: 15px;
	  
	  color: white;
 }
 .card-body{
   padding: 3% 0 0 8% !important;
   text-align: start !important;
}
</style>
<script>
import $ from 'jquery';
import Axios from "axios";

export default {

  data() {
    return {
      songs: [],
      estilos: "",
      recomend: []
    }
  },
    
    mounted() {
        this.selectChecked();
        this.get_allSong();
    },

    methods: {
      selectChecked(){
        $(".image-checkbox").each(function () {
            if ($(this).find('input[type="checkbox"]').first().attr("checked")) {
                $(this).addClass('image-checkbox-checked');
            }
            else {
                $(this).removeClass('image-checkbox-checked');
            }
        });

        const countChecked = () => {
            var checkedElements = document.querySelectorAll(".image-checkbox-checked");
            return checkedElements.length;
        };
        
        // sync the state to the input
        $(".image-checkbox").on("click", function (e) {
            if(countChecked() >= 3){
                alert('no puedes agregar mas de 3');
                return true;
            }
            $(this).toggleClass('image-checkbox-checked');
            var $checkbox = $(this).find('input[type="checkbox"]');
            $checkbox.prop("checked",!$checkbox.prop("checked"))
        
            e.preventDefault();
        });
      },
      get_allSong(){
        Axios.get('http://127.0.0.1:5000/populate/song')
        .then(res => {
          this.songs = res.data
          console.log(this.songs[0]['_id'])
        }).catch( err => {
          console.log(err)
        })
      },

      checked(id, title, release, artist, year, song){
        this.recomend.push({
          "user_id": localStorage.getItem('user_id'),
          "song_id": id,
          "listen_count": 1,
          "title": title,
          "release": release,
          "artist_name": artist,
          "year": year,
          "song": song
          })
        if(this.estilos == ''){
          this.estilos = 'image-checkbox-checked'
        }else{
          this.estilos = ''
        }
        console.log(this.recomend)  
      },
      recomendar(){
        Axios.post('http://127.0.0.1:5000/build-model/user-new', this.recomend)
        .then(res => {
          if(res.data){
            swal({
              title: 'Envio Succefully',
              text: 'Datos correctos',
              icon: 'success',
              closeOnClickOutside: false,
              closeOnEsc: false
					    }).then( select => {
						    if(select){
                  this.$router.push('/inicio')
						    }
					  })
          }
        }).catch(err => {
          console.log(err)
        })
      }
    }
   
}
</script>