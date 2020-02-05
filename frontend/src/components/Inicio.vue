<template>
<div id="inicio-fondo">
    <div class="container">
        <div class="row">
          <div class="gallery col-lg-12 col-md-12 col-sm-12 col-xs-12">
              <h1 class="gallery-title"><strong>SONGNIFY</strong> </h1>

            <div text-align="center">
                <button class="btn btn-default filter-button" data-filter="all">Todas las canciones</button>
                <button class="btn btn-default filter-button" data-filter="hdpe">Tendencia</button>
                <button class="btn btn-default filter-button" data-filter="sprinkle">Sprinkle Pipes</button>
                <button class="btn btn-default filter-button" data-filter="spray">Spray Nozzle</button>
                <button class="btn btn-default filter-button" data-filter="irrigation">Irrigation Pipes</button>
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
              <div class="gallery_product col-lg-4 col-md-4 col-sm-4 col-xs-6 filter irrigation">
                  <img :src="require('../assets/img/cancion-cd.jpg')" class="img-fluid trazo">
              </div>

              <div class="gallery_product col-lg-4 col-md-4 col-sm-4 col-xs-6 filter spray">
                  <img :src="require('../assets/img/cancion-cd.jpg')" class="img-fluid trazo">
              </div>
          </div>
       </div>
  </div>
 </div>
</div>
    
</template>

<script>
export default {

    mounted() {
        console.log(localStorage.getItem('user_id'))
    },
}
</script>
