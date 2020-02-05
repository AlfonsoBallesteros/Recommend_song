<template>
<div class="bg-container">
  <div class="container">

    <div class=" col-lg-12 col-md-12 col-sm-12 col-xs-12">
        <h1 class="h1"><strong>Escoge tus canciones favoritas</strong> </h1>
    </div>
<div class="row">
  <div class="col-xs-4 col-sm-3 col-md-4 nopad text-center">
    <label class="image-checkbox">
      <img class="img-fluid" src="https://dummyimage.com/600x400/000/fff" />
      <input type="checkbox" name="image[]" value="" />
      <i class="fa fa-check hidden"></i>
    </label>
  </div>
  <div class="col-xs-4 col-sm-3 col-md-4 nopad text-center">
    <label class="image-checkbox">
      <img class="img-fluid" src="https://dummyimage.com/600x400/000/fff" />
      <input type="checkbox" name="image[]" value="" />
      <i class="fa fa-check hidden"></i>
    </label>
  </div>
  <div class="col-xs-4 col-sm-3 col-md-4 nopad text-center">
    <label class="image-checkbox">
      <img class="img-fluid" src="https://dummyimage.com/600x400/000/fff" />
      <input type="checkbox" name="image[]" value="" />
      <i class="fa fa-check hidden"></i>
    </label>
  </div>
</div>
<div class="row"> 
  <div class="col-xs-4 col-sm-3 col-md-4 nopad text-center">
    <label class="image-checkbox">
      <img class="img-fluid" src="https://dummyimage.com/600x400/000/fff" />
      <input type="checkbox" name="image[]" value="" />
      <i class="fa fa-check hidden"></i>
    </label>
  </div>
  <div class="col-xs-4 col-sm-3 col-md-4 nopad text-center">
    <label class="image-checkbox">
      <img class="img-fluid" src="https://dummyimage.com/600x400/000/fff" />
      <input type="checkbox" name="image[]" value="" />
      <i class="fa fa-check hidden"></i>
    </label>
  </div>
  <div class="col-xs-4 col-sm-3 col-md-4 nopad text-center">
    <label class="image-checkbox">
      <img class="img-fluid" src="https://dummyimage.com/600x400/000/fff" />
      <input type="checkbox" name="image[]" value="" />
      <i class="fa fa-check hidden"></i>
    </label>
  </div>
  
</div>
  <br><br>
  <div class="col-md-12">
      <button type="submit" class="btn btn-warning btn-lg btn-block ">Siguiente</button>
  </div>

</div>
</div>
</template>

<script>
export default {

}
</script>

<style>
    
</style>
<script>
import $ from 'jquery';

export default {
    
    mounted() {
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
   
}
</script>