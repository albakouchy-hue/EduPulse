let time = 0;
setInterval(() => {
  time++;
  document.getElementById("time-bar").innerText = "⏱️ " + new Date(time * 1000).toISOString().substr(14, 5);
}, 1000);
