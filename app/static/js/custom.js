// adding row to table
function addRow(table){
  t_name = table.replace("-table","");
  count = $(table+' tbody tr').length;
  $(table+' > tbody').last().append('\
    <tr id='+t_name.replace("#","")+'_row_'+count+'>\
      <td class="text-center"><button class="btn btn-link btn-block">0:00</button></td>\
      <td class="text-center"><button class="btn btn-link btn-block">0:00</button></td>\
      <td class="text-center"><button class="btn btn-link btn-block">17.0</button></td>\
      <td class="text-right"><button class="btn btn-danger" onclick="removeRow(\''+t_name+'_row_'+count+'\')">\
      <span class="glyphicon glyphicon-minus"></span></button></td>\
    </tr>');
};

function removeRow(row){
  $(row).remove();
};

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

function new_schedule(csrf_token){
    //'/schedule/change'
    /*$.ajax({
        url: '/schedule/change',
        dataType: "json",
        method: "POST",
        success: 
    }*/

};
