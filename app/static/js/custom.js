// adding row to table
function addRow(table){
  $(table+' > tbody').last().append('\
    <tr>\
      <td class="text-center"><button class="btn btn-link btn-block">00:00</button></td>\
      <td class="text-center"><button class="btn btn-link btn-block">00:00</button></td>\
      <td class="text-center"><button class="btn btn-link btn-block">17</button></td>\
      <td class="text-right"><button class="btn btn-danger delete-row">\
      <span class="glyphicon glyphicon-minus"></span></button></td>\
    </tr>');};

// removing row from table
$(function(){
      $('table').on('click','tr button.delete-row',function(e){
         e.preventDefault();
        $(this).parents('tr').remove();
      });
});

/*function update_value(field_id,rate) {
  (setTimeout( function () {
  $.ajax({
        url: '/dashboard/get_data',
        dataType: "json",
        method: "POST",
        success: function(result){
            $(document.getElementById(field_id)).text(result[field_id])
        }})
},rate*1000)());
};*/
