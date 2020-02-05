<template>
<body>
<div id="inicio">
    <div class="container">
        <div class="row">
          <div class="gallery col-lg-12 col-md-12 col-sm-12 col-xs-12">
              <h1 class="gallery-title"><strong>SONGNIFY</strong> </h1>
                   
            <div class="row">
                <div class="gallery_product col-md-4 filter hdpe">
                    <a href="cancion.html"><img :src="require('../assets/img/cancion-cd.jpg')" class="img-fluid trazo"></a>
                    <h4 class="texto"><strong>Canción:</strong> Todo de cabeza <br> <strong> Kaleth Morales </strong> </h4>
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
</body>
    
</template>
<script>
import img from '../assets/img/cancion-cd.jpg'
export default {
  name: 'inicio',
  data () {
    return {
      
    }
  }
}
</script>
<style scoped>
    .gallery-title
    {
        font-size: 80px;
        color: white;
        text-align: center;
        font-weight: 500;
        margin-bottom: 70px;
        font-family: 'love';
    }
    .gallery-title:after {
        content: "";
        position: absolute;
        width: 7.5%;
        left: 46.5%;
        height: 45px;
        /*border-bottom: 1px solid #5e5e5e;*/
    }

    .texto{
        position: absolute;
        bottom: 10px;
        right: 60px;
        color: black;
        height: 50px;
        font-size: 20px;
    }
    .filter-button
    {
        font-size: 18px;
        border: 1px solid black;
        border-radius: 5px;
        align-items: center;
        color: black;
        margin-bottom: 30px;

    }
    .filter-button:hover
    {
        font-size: 18px;
        border: 1px solid black;
        border-radius: 5px;
        text-align: center;
        color: #ffffff;
        background-color: darkblue;

    }
    .btn-default:active .filter-button:active
    {
        background-color: #42B32F;
        color: white;
    }

    .port-image
    {
        width: 100%;
    }

    .gallery_product
    {
        margin-bottom: 30px;
    }



    #inicio{
        background-image: 'url(' + require('@/assets/img/fondo.png') + ')';
        background-size: cover;
        background-repeat: no-repeat;
        height: 100%;
        font-family: 'Numans', sans-serif;
        }
    
    /*
        @font-face {
            font-family: "love";
            src: url("img/love.ttf");
        }*/
</style>
<script>
export default {

    mounted() {
        console.log(localStorage.getItem('user_id'))
    },
}
</script>
