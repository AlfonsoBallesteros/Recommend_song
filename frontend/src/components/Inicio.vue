<template>
<div id="inicio-fondo">
    <div class="container m-l-a">
        <div class="row">
          <div class="gallery col-lg-12 col-md-12 col-sm-12 col-xs-12">
              <h1 class="gallery-title"><strong>SONGNIFY</strong> </h1>

            <div text-align="center">
                <button class="btn btn-default filter-button" data-filter="irrigation">Recomendacion</button>
                <button class="btn btn-default filter-button" data-filter="hdpe">Populares</button>
                <button class="btn btn-default filter-button" data-filter="all">Todas las canciones</button>
           </div>
                   
            <div class="row">
                <!---aqui va las populares tanks!!--->
                <div v-for="(r_old, index) in song_recommend_old" :key="index" class="gallery_product col-md-4 filter hdpe">
                    <router-link :to="'/cancion/id/' + r_old.song"><img :src="require('../assets/img/cancion-cd.jpg')" class="img-fluid trazo"></router-link>
                    <h5 class="texto"><strong>Canción:</strong> {{r_old.song}} <br></h5>
                </div>
            </div>
            <div class="row">
                <!---aqui va las todas las canciones tanks!!--->
                <div v-for="(song, index) in songs" :key="index" class="gallery_product col-md-4 filter all">
                    <img :src="require('../assets/img/cancion-cd.jpg')" class="img-fluid trazo">
                     <h5 class="texto"><strong>Canción:</strong> {{song._id.song}} <br></h5>
                </div>
            </div>
            <!---aqui va la recomendacion tanks!!--->
            <div class="row">
              <div v-for="(r_new, index) in song_recommend_new" :key="index" class="gallery_product col-md-4 filter irrigation">
                  <img :src="require('../assets/img/cancion-cd.jpg')" class="img-fluid trazo">
                  <h5 class="texto"><strong>Canción:</strong> {{r_new.song}} <br></h5>
              </div>
          </div>
       </div>
  </div>
 </div>
</div>
    
</template>

<script>
import Axios from "axios";
import $ from 'jquery';
export default {
    data() {
        return {
            song_recommend_new: [],
            song_recommend_old: [],
            songs: []
        }
    },

    mounted() {
        console.log(localStorage.getItem('user_id'))
        this.menus();
        this.recomendacion_new();
        this.recommend_old();
        this.get_all()
    },  
    methods: {
        menus(){
            $(document).ready(function(){

            $(".filter-button").click(function(){
                var value = $(this).attr('data-filter');
                
                if(value == "sprinkle")
                {
                    //$('.filter').removeClass('hidden');
                    $('.filter').show('');
                }
                else
                {
        //            $('.filter[filter-item="'+value+'"]').removeClass('hidden');
        //            $(".filter").not('.filter[filter-item="'+value+'"]').addClass('hidden');
                    $(".filter").not('.'+value).hide('3000');
                    $('.filter').filter('.'+value).show('3000');
                    
                }
            });
            
            if ($(".filter-button").removeClass("active")) {
                $(this).removeClass("active");
            }
            $(this).addClass("active");

            });
        },
    
        recomendacion_new(){
            Axios.post('http://127.0.0.1:5000/recommend/new',{
                user_id: localStorage.getItem('user_id')
            }).then( res => {
                this.song_recommend_new = res.data
                console.log(this.song_recommend_new)
            }).catch(err => {
                console.log(err)
            })

        },
        get_all(){  
            Axios.get('http://127.0.0.1:5000/all/song')
            .then( res => {
                this.songs = res.data
                console.log(this.songs)
            }).catch( err =>{
                console.log(err)
            })
        },
        recommend_old(){
            Axios.post('http://127.0.0.1:5000/recommend/old', {
                user_id: localStorage.getItem('user_id')
            }).then( res => {
                this.song_recommend_old = res.data
                console.log(this.song_recommend_old)
            }).catch(err => {
                console.log(err)
            })
        }

    },
}
</script>
