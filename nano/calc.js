var calculate = document.querySelector('#calculate');
var userInput = document.querySelector('#user-input');
var goal = document.querySelector('#monthgoal');
var result = document.querySelector('#result');
var date = document.querySelector('#datefield');
var target = document.querySelector('#target');
var wordsleft = document.querySelector('#wordsleft');                           
var wpdtfv = document.querySelector('#wpdtf');                                   
var t_wpdtf = document.querySelector('#t_wpdtf');                               
var t_math = document.querySelector('#t_math');                                 
var h_wpdtf = document.querySelector('#h_wpdtf');                             
var h_math = document.querySelector('#h_math');                                 
var k_wpdtf = document.querySelector('#k_wpdtf');                               
var k_math = document.querySelector('#k_math');                                 
var avg_wpd = document.querySelector('#avg_wpd');                               
var dday = document.querySelector('#dday');
var perday = 1667;
var todaybutton = document.querySelector('#today');

todaybutton.addEventListener('click', function(ev){
  var day = new Date().getDate();                             
  date.value = day;                        
});

function round(num, divisor){
  return num - (num % divisor);
}

calculate.addEventListener('click', function(ev) {
  var finish = parseInt(goal.value);
  var count = parseInt(userInput.value);
  var tgt = perday * date.value;
  var wleft = finish - count;
  var dleft = 30 - date.value;
  var wpdtf = parseInt(wleft / dleft);
  target.textContent = tgt;
  skew.textContent = (count - tgt)/perday;
  wordsleft.textContent = wleft;
  wpdtfv.textContent = wpdtf;
  //yes this bit should be a function
  var tw = round(wpdtf, 10);
  console.log(tw);
  var hw = round(wpdtf, 100);
  var kw = round(wpdtf, 1000);
  var tmath = finish - ((tw * dleft) + count);
  console.log(finish);
  console.log(dleft);
  console.log(count);
  console.log(tmath);
  var hmath = finish - ((hw * dleft) + count);
  var kmath = finish - ((kw * dleft) + count);

  t_wpdtf.textContent = tw;
  t_math.textContent = tmath;
  h_wpdtf.textContent = hw;
  h_math.textContent = (hmath);
  k_wpdtf.textContent = kw;
  k_math.textContent = (kmath);
  var avg = count/parseInt(date.value);
  var dd = finish/(count/parseInt(date.value));
  avg_wpd.textContent = avg;
  dday.textContent = parseInt(dd);
});
