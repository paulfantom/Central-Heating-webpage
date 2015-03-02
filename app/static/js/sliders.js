$(document).ready(function() {
  // HOME SLIDERS
  $("#sliderRoom").slider({});
  // $("#slider1").slider({
  //   formater: function(value) {
  //     return value + "\xB0C";
  //   }
  // });

  $("#sliderRoom").on('slide', function(slideEvt) {
    var E = parseInt($("#humidity_value").text()) / 100 * 6.105 *
            Math.exp( 17.27 * slideEvt.value / ( 237.7 + slideEvt.value ) );
    // E = (rh/100) * 6.105 * exp(17.27*T/(237.7+T))
    var feel_temp = slideEvt.value + 0.188 * E - 2.777;
    feel_temp = feel_temp.toFixed(1);
    // AT = 0.537 * T + 0.393 * E + 3.94
    $("#feelValTmp").text(feel_temp);
    $("#roomValTmp").text(slideEvt.value);
    
    $("#feelVal").text(feel_temp);
    $("#roomVal").text(slideEvt.value);
  });



  // WATER SLIDERS
  $("#sliderSolarWater").slider({});
  $("#sliderSolarWater").on('slide', function(slideEvt) {
    var array = $("#sliderSolarWater").val().split(",");
    $("#solarWaterMinValTmp").text(array[0]);
    $("#solarWaterMaxValTmp").text(array[1]);
  });
  $("#save-solarWaterVal").on('click', function() {
    var array = $("#sliderSolarWater").val().split(",");
    $("#solarWaterMinVal").text(array[0]);
    $("#solarWaterMaxVal").text(array[1]);
  });
  
  $("#sliderHeaterWater").slider({});
  $("#sliderHeaterWater").on('slide', function(slideEvt) {
    var array = $("#sliderHeaterWater").val().split(",");
    $("#heaterWaterMinValTmp").text(array[0]);
    $("#heaterWaterMaxValTmp").text(array[1]);
  });
  $("#save-heaterWaterVal").on('click', function() {
    var array = $("#sliderHeaterWater").val().split(",");
    $("#heaterWaterMinVal").text(array[0]);
    $("#heaterWaterMaxVal").text(array[1]);
  });
  
  
  // SOLAR SLIDERS
  $("#sliderSolar").slider({});
  $("#sliderSolar").on('slide', function(slideEvt) {
    var array = $("#sliderSolar").val().split(",");
    $("#solarMinValTmp").text(array[0]);
    $("#solarMaxValTmp").text(array[1]);
  });
  $("#save-solarVal").on('click', function() {
    var array = $("#sliderSolar").val().split(",");
    $("#solarMinVal").text(array[0]);
    $("#solarMaxVal").text(array[1]);
  });

  $("#sliderDelta").slider({});
  $("#sliderDelta").on('slide', function(slideEvt) {
    $("#deltaValTmp").text(slideEvt.value);
  });
  $("#save-deltaVal").on('click', function() {
    $("#deltaVal").text($("#sliderDelta").val());
  });

  $("#sliderHysteresis").slider({});
  $("#sliderHysteresis").on('slide', function(slideEvt) {
    $("#hysteresisValTmp").text(slideEvt.value);
  });
  $("#save-hysteresisVal").on('click', function() {
    $("#hysteresisVal").text($("#sliderHysteresis").val());
  });
  
  
  //HEATER SLIDERS
  $("#sliderHeaterHysteresis").slider({});
  $("#sliderHeaterHysteresis").on('slide', function(slideEvt) {
    $("#heaterHysteresisValTmp").text(slideEvt.value);
  });
  $("#save-heaterHysteresisVal").on('click', function() {
    $("#heater_hysteresis1").text($("#sliderHeaterHysteresis").val());
    $("#heater_hysteresis2").text($("#sliderHeaterHysteresis").val());
  });
  
  //OPTIONS SLIDERS
  $("#sliderRefreshRate").slider({});
  $("#sliderRefreshRate").on('slide', function(slideEvt) {
    $("#dataRefreshRateTmp").text(slideEvt.value);
  });
  $("#save-dataRefreshRate").on('click', function() {
    $("#refreshRateValue").text($("#sliderRefreshRate").val());
    //save to database
//    location.reload(); //refresh page
  });
  $("#sliderSupply").slider({});
  $("#sliderSupply").on('slide', function(slideEvt) {
    $("#supplyValueTmp").text(slideEvt.value);
  });
  $("#save-supplyValue").on('click', function() {
    $("#supplyValue").text($("#sliderSupply").val());
  });
  $("#sliderHysteresisSupply").slider({});
  $("#sliderHysteresisSupply").on('slide', function(slideEvt) {
    $("#hysteresisSupplyValueTmp").text(slideEvt.value);
  });
  $("#save-hysteresisSupplyValue").on('click', function() {
    $("#hysteresisSupplyValue").text($("#sliderHysteresisSupply").val());
  });
  
});