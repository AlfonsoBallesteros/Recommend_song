<template>
<div id="inicio-fondo">
    <div class="container m-l-a">
        <div class="row">
          <div class="gallery col-lg-12 col-md-12 col-sm-12 col-xs-12">
              <h1 class="gallery-title"><strong>SONGNIFY</strong> </h1>

            <div text-align="center">
                <button class="btn btn-default filter-button" data-filter="all">Todas las canciones</button>
                <button class="btn btn-default filter-button" data-filter="hdpe">Populares</button>
                <button class="btn btn-default filter-button" data-filter="sprinkle">Recomendaciones</button>
           </div>
                   
            <div class="row">
                <div class="gallery_product col-md-4 filter hdpe">
                    <a href="cancion.html"><img :src="require('../assets/img/cancion-cd.jpg')" class="img-fluid trazo"></a>
                    <h5 class="texto"><strong>Canción:</strong> Todo de cabeza <br><strong> Kaleth Morales </strong> </h5>
                </div>

                <div class="gallery_product col-md-4   filter sprinkle">
                    <img :src="require('../assets/img/cancion-cd.jpg')" class="img-fluid trazo">
                </div>

                <div class="gallery_product col-lg-4 col-md-4 col-sm-4 col-xs-6 filter hdpe">
                    <img :src="require('../assets/img/cancion-cd.jpg')" class="img-fluid trazo">
                </div>
            </div>
            <div class="row">
              <div class="gallery_product col-lg-4 col-md-4 col-sm-4 col-xs-6 filter all">
                  <img :src="require('../assets/img/cancion-cd.jpg')" class="img-fluid trazo">
              </div>

              <div class="gallery_product col-lg-4 col-md-4 col-sm-4 col-xs-6 filter hdpe">
                  <img :src="require('../assets/img/cancion-cd.jpg')" class="img-fluid trazo">
              </div>
          </div>
       </div>
  </div>
 </div>
</div>
    
</template>

<script>
import $ from 'jquery';
export default {

    mounted() {
        console.log(localStorage.getItem('user_id'))
        

        $(document).ready(function(){

            $(".filter-button").click(function(){
                var value = $(this).attr('data-filter');
                
                if(value == "all")
                {
                    //$('.filter').removeClass('hidden');
                    $('.filter').show('1000');
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
        }
        </script>
