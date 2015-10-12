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
    var data = {};
    var json = [];
    $('#work_day-table tbody tr').each(function(){
        var obj = {};
        var $td=$(this).find('td');
        var val = [parseInt($td.eq(0).find('span').eq(0).text()),
                   parseInt($td.eq(0).find('span').eq(1).text())];
        obj['from'] = val;
        val = [parseInt($td.eq(1).find('span').eq(0).text()),
               parseInt($td.eq(1).find('span').eq(1).text())];
        obj['to'] = val;
        val = parseFloat( $td.eq(2).text() ).toFixed(2);
        obj['temp'] = val;
        json.push(obj);
    });
    data['work'] = json;
    json = [];
    $('#free_day-table tbody tr').each(function(){
        var obj = {};
        var $td=$(this).find('td');
        obj['from'] = [$td.eq(0).find('span').eq(0).text(),
                       $td.eq(0).find('span').eq(1).text()];
        obj['to']   = [$td.eq(1).find('span').eq(0).text(),
                       $td.eq(1).find('span').eq(1).text()];
        obj['temp'] =  parseFloat($td.eq(2).text());
        json.push(obj);
    }); 
    data['free'] = json;
    data['other'] = parseFloat($('#work_day-table tfoot tr').find('td').eq(2).text());
    data['week'] = [0,0,0,0,0,1,1];
    console.log(JSON.stringify(data));
    $.post('/schedule/change',JSON.stringify(data),"json");
    /*$.ajax({
        type : "POST",
        contentType: "application/json; charset=utf-8",
        url: '/schedule/change',
        data : data,
        dataType : "json"}); */
};
