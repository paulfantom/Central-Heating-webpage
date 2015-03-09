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