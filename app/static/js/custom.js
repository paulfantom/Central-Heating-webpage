// adding row to table
function addRow(container){
  var dt = new Date();
  var time = dt.getHours() + ":" + ("0"+dt.getMinutes()).slice(-2);
  var count = $(container+' > .row').length - 1 ;
  var row_name =  container.replace("-rows","-row-") + count.toString();
  $(container).last().append('\
    <div class="row row-schedule clearfix" id="'+row_name.substring(1)+'">\
      <div class="col-xs-3 col-sm-4 text-center">\
        <input type="text" class="form-control clockpicker text-center btn btn-link" name="from" value="'+time+'">\
      </div>\
      <div class="col-xs-3 col-sm-4 text-center">\
        <input type="text" class="form-control clockpicker text-center btn btn-link" name="to" value="'+time+'">\
      </div>\
      <div class="col-xs-3 col-sm-3 text-center">\
        <input type="text" class="form-control text-center btn btn-link" name="temp" value="20.0">\
      </div>\
      <div class="col-xs-3 col-sm-1 text-center">\
        <button class="btn btn-danger" onclick="removeRow(\''+row_name+'\')">\
          <span class="glyphicon glyphicon-minus"></span>\
        </button>\
      </div>\
    </div> <!-- '+row_name+' -->');
  $('.clockpicker').clockpicker({
    placement: "bottom",
    autoclose: "true"
  });
}

function removeRow(row){
  console.log(row);
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
    $('#work_day-rows > .row-schedule').each(function(){
        var obj = {};
        var $fields=$(":input", this);
        obj['from'] = $fields.eq(0).val();
        obj['to'] = $fields.eq(1).val();
        obj['temp'] = $fields.eq(2).val();
        json.push(obj);
    });
    data['work'] = json;
    json = [];
    $('#free_day-rows > .row-schedule').each(function(){
        var obj = {};
        var $fields=$(":input", this);
        obj['from'] = $fields.eq(0).val();
        obj['to'] = $fields.eq(1).val();
        obj['temp'] = $fields.eq(2).val();
        json.push(obj);
    });
    data['free'] = json;
    data['other'] = $('#change_default').val();
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
