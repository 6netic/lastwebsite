
let minutes = document.getElementById('minutes');
let seconds = document.getElementById('seconds');
let m = Number(document.getElementById('min').value);
let s = Number(document.getElementById('sec').value);
setInterval(function () {
  s += 1;
  if (s < 10) { seconds.textContent = "0" + s; }
  else if (10 < s < 60) { seconds.textContent = s; }
  if (s == 60) {
    m += 1; s = 0; seconds.textContent = "00";
    if (m < 10) {
      minutes.textContent = "0" + m;
    } else {
      minutes.textContent = m;
    }
  }
}, 1000)
