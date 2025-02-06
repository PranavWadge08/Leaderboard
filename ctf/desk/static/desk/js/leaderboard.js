// ws stuff below

var url = 'ws://' + window.location.host + '/ws/ctf/leaderboard';
const socket = new WebSocket(url);
socket.addEventListener('close', function (event) {
    triggerAlert("danger", 'Connection closed. Try refreshing the page.');
});

socket.addEventListener('error', function (event) {
    triggerAlert("danger", `Connection Error: ${event}`);
});

socket.addEventListener('message', function (event) {
    data = JSON.parse(event.data);
    renderMessage(data);
});

// utility functions below

function triggerAlert(tag, msg) {
    const messageContainer = document.getElementById('message-box');
    messageContainer.innerHTML = `<div class="alert alert-${tag} px-4 py-2 m-0" role="alert">${msg}</div>`;
    setTimeout(() => { messageContainer.innerHTML = ''; }, 5000)
}

function highlightChange(active) {
    document.getElementById('update-audio').play();
    setTimeout(() => { document.getElementById(active.id).style.border = '1px solid #141a39'; }, 100);
    triggerAlert("info", `${active.name} submitted a flag.`);
    setTimeout(() => { document.getElementById(active.id).style.border = 'none'; }, 600);
}

function updateScore(contestants) {
    const tableBody = document.querySelector('#leaderboard table'); innerCode = '';
    if (contestants.length > 0) {
        contestants.forEach((contestant, index) => {
            trophy = (index == 0 && contestant.points != 0) ? '<img class="gold-medal" src="/static/desk/assets/images/gold-medal.png" alt="gold medal"/>' : '';
            innerCode += `<tr id="${contestant.contestant}"><td class="number">${index + 1}</td><td class="name">${contestant.contestant__first_name} ${contestant.contestant__last_name}<p class='submission-time'>Last Flag Submit at ${new Date(contestant.last * 1000).toLocaleTimeString([], {
                hour: '2-digit', minute: '2-digit', second: '2-digit'
            })}</p></td><td class="points"><i class="ph ph-flag"></i>&nbsp;${contestant.flags} &nbsp;&nbsp; <i class="ph ph-gauge"></i>&nbsp; ${contestant.points} ${trophy}</td></tr>`
        });
    } else {
        innerCode += `<tr><td class="name">No Flags have been submitted yet.</td></tr>`
    }
    tableBody.innerHTML = innerCode;

}

function renderMessage(message) {
    if (message.hasOwnProperty('score')) {
        updateScore(JSON.parse(message.score));
        if (message.hasOwnProperty('active')) {
            highlightChange(JSON.parse(message.active));
        }
    } else if (message.hasOwnProperty('message')) {
        triggerAlert("info", message.message);
    }
}

// particle js stuff below
var pconf= {
    "particles": {
      "number": {
        "value": 80,
        "density": {
          "enable": true,
          "value_area": 800
        }
      },
      "color": {
        "value": "#118fff"
      },
      "shape": {
        "type": "triangle",
        "stroke": {
          "width": 0,
          "color": "#000000"
        },
        "polygon": {
          "nb_sides": 5
        },
        "image": {
          "src": "img/github.svg",
          "width": 100,
          "height": 100
        }
      },
      "opacity": {
        "value": 0.5,
        "random": false,
        "anim": {
          "enable": false,
          "speed": 1,
          "opacity_min": 0.1,
          "sync": false
        }
      },
      "size": {
        "value": 11.83721462448409,
        "random": true,
        "anim": {
          "enable": true,
          "speed": 40,
          "size_min": 0.1,
          "sync": false
        }
      },
      "line_linked": {
        "enable": true,
        "distance": 150,
        "color": "#ffffff",
        "opacity": 0.4,
        "width": 1
      },
      "move": {
        "enable": true,
        "speed": 6,
        "direction": "none",
        "random": false,
        "straight": false,
        "out_mode": "out",
        "bounce": false,
        "attract": {
          "enable": false,
          "rotateX": 600,
          "rotateY": 1200
        }
      }
    },
    "interactivity": {
      "detect_on": "canvas",
      "events": {
        "onhover": {
          "enable": true,
          "mode": "grab"
        },
        "onclick": {
          "enable": true,
          "mode": "push"
        },
        "resize": true
      },
      "modes": {
        "grab": {
          "distance": 400,
          "line_linked": {
            "opacity": 1
          }
        },
        "bubble": {
          "distance": 400,
          "size": 40,
          "duration": 2,
          "opacity": 8,
          "speed": 3
        },
        "repulse": {
          "distance": 200,
          "duration": 0.4
        },
        "push": {
          "particles_nb": 4
        },
        "remove": {
          "particles_nb": 2
        }
      }
    },
    "retina_detect": true
  };
particlesJS("particles-js", pconf); var count_particles, update; count_particles = document.querySelector('.js-count-particles'); update = function () { if (window.pJSDom[0].pJS.particles && window.pJSDom[0].pJS.particles.array) { count_particles.innerText = window.pJSDom[0].pJS.particles.array.length; } requestAnimationFrame(update); }; requestAnimationFrame(update);;