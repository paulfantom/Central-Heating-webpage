$(document).ready(function(){
  
  // TABELA HARMONOGRAMU PRACY (DZIEN ROBOCZY)
  var i=1;
  $("#add_working_row").click(function(){
    $('#addr_w'+i).html()
    $('#addr_w'+i).html("<td class='text-center'>\
      <button class='btn btn-link btn-block' id='from_working_"+i+"'>6:00</button></td>\
    <td class='text-center'>\
      <button class='btn btn-link btn-block' id='to_working_"+i+"'>8:00</button></td>\
    <td class='text-center'>\
      <button class='btn btn-link btn-block' id='temp_working_"+i+"'>21</button></td>\
    <td class='text-right'>\
      <button class='btn btn-danger' id='remove_working_row"+i+"'>\
        <span class='glyphicon glyphicon-minus'></span></button></td>"
    );
    $('#table-working-tbody').append('<tr id="addr_w'+(i+1)+'"></tr>');
    
    $("<script>$('#remove_working_row"+i+"').click(function(){$('#addr_w"+i+"').html('');});</script>").appendTo(document.body);
    
    i++;
  });
  $("#remove_working_row0").click(function(){
    $("#addr_w0").html('');
  });
  
  // TABELA HARMONOGRAMU PRACY (DZIEN WOLNY)
  var j=1;
  $("#add_free_row").click(function(){
    $('#addr_f'+j).html()
    $('#addr_f'+j).html("<td class='text-center'>\
      <button class='btn btn-link btn-block' id='from_free_"+j+"'>6:00</button></td>\
    <td class='text-center'>\
      <button class='btn btn-link btn-block' id='to_free_"+j+"'>8:00</button></td>\
    <td class='text-center'>\
      <button class='btn btn-link btn-block' id='temp_free_"+i+"'>21</button></td>\
    <td class='text-right'>\
      <button class='btn btn-danger' id='remove_free_row"+j+"'>\
        <span class='glyphicon glyphicon-minus'></span></button></td>"
    );
    $('#table-free-tbody').append('<tr id="addr_f'+(j+1)+'"></tr>');
    
    $("<script>$('#remove_free_row"+j+"').click(function(){$('#addr_f"+j+"').html('');});</script>").appendTo(document.body);
    
    j++;
  });
  $("#remove_free_row0").click(function(){
    $("#addr_f0").html('');
  });
  
  $('input[type="checkbox"][name="day"]').change(function () {
    if (this.checked) {
      $("label[id="+this.id+"-label]").removeClass("btn-info");
      $("label[id="+this.id+"-label]").addClass("btn-danger");
    }
    else {
      $("label[id="+this.id+"-label]").addClass("btn-info");
      $("label[id="+this.id+"-label]").removeClass("btn-danger");
    }
  });
  
});