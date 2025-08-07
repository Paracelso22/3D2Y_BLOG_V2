//Interactividad en el menu lateral
document.querySelectorAll('.sidebar__dropdown-title').forEach(title => {
  title.addEventListener('click', () => {
    title.nextElementSibling.classList.toggle('active');
  });
});

//Carrusel automatico
let currentIndex = 0;
const items = document.querySelectorAll('.carousel__item');
const track = document.querySelector('.carousel__track');

function showSlide(index) {
  track.style.transform = `translateX(-${index * 100}%)`;
}

setInterval(() => {
  currentIndex = (currentIndex + 1) % items.length;
  showSlide(currentIndex);
}, 4000);

//Fecha actual en el footer
const yearSpan = document.getElementById('year');
if (yearSpan) {
  yearSpan.textContent = new Date().getFullYear();
}

//Cambiar al modo oscuro
const btnModoNoche = document.getElementById('btnModoNoche');

if (btnModoNoche) {
  btnModoNoche.addEventListener('click', () => {
    document.body.classList.toggle('modo-nocturno');

    // Cambiar el icono y texto del botón según el modo actual
    if (document.body.classList.contains('modo-nocturno')) {
      btnModoNoche.textContent = '☀️ Modo Día';
    } else {
      btnModoNoche.textContent = '🌙 Modo Noche';
    }
  });
}

