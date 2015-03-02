window.onload = function(){date()},
                setInterval(
                  function(){
                    date()
                  }, 1000);

function date() {
  var MyDate = new Date(),
  time = MyDate.getHours() + ':' + 
        ('0' + MyDate.getMinutes()).slice(-2);
  date = MyDate.getDate() + '/' + 
        ('0' + (MyDate.getMonth() + 1)).slice(-2) + '/' + 
        MyDate.getFullYear();
  $('#time').html(time);
  $('#date').html(date);
}