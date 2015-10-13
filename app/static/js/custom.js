// adding row to table
function addRow(container){
  var dt = new Date();
  var time = dt.getHours() + ":" + ("0"+dt.getMinutes()).slice(-2);
  var count = $(container+' > .row').length - 1 ;
  var row_name =  container.replace("-rows","-row-") + count.toString();
  $(container).last().append('\
    <div class="row row-schedule clearfix" id="'+row_name.substring(1)+'">\
      <div class="col-xs-3 col-sm-4 text-center">\
        <input type="text" readonly="true" class="form-control clockpicker text-center btn btn-link" name="from" value="'+time+'">\
      </div>\
      <div class="col-xs-3 col-sm-4 text-center">\
        <input type="text" readonly="true" class="form-control clockpicker text-center btn btn-link" name="to" value="'+time+'">\
      </div>\
      <div class="col-xs-3 col-sm-3 text-center">\
        <input type="text" readonly="true" class="form-control text-center btn btn-link changetemp" name="temp" value="20.0">\
      </div>\
      <div class="col-xs-3 col-sm-1 text-center">\
        <button class="btn btn-danger" onclick="removeRow(\''+row_name+'\')">\
          <span class="glyphicon glyphicon-minus"></span>\
        </button>\
      </div>\
    </div> <!-- '+row_name+' -->');
  $('.clockpicker').clockpicker({
    placement: "bottom",
    align: "top",
    autoclose: "true"
  });
  $('.changetemp').plusminus({
    placement: "bottom",
    align: "right",
    step: 0.25,
    precision: 2,
    min: 15,
    max: 28
  });
}

function removeRow(row){
  $(row).remove();
};

function toggleButton(button){
  
};

function sendSchedule(csrf_token){
    //'/schedule/change'
    setTimeout(function(){
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
    var states = [];
    $('#week-tab').find('.well > button').each(function(){
        if ($(this).hasClass('active') || $(this).hasClass('focus active')) {
            states.push(1);
        } else {
            states.push(0);
        }
    });
    console.log(states);
    data['week'] = states;
    console.log(JSON.stringify(data));
    $.post('/schedule/change',JSON.stringify(data),"json");
    /*$.ajax({
        type : "POST",
        contentType: "application/json; charset=utf-8",
        url: '/schedule/change',
        data : data,
        dataType : "json"}); */
    },100);
};
