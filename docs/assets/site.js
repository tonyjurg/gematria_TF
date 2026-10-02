// Keep the menu available without JavaScript; collapse it on small screens.
const menu = document.querySelector('.navigation');
const narrow = window.matchMedia('(max-width: 680px)');
function adaptMenu() { menu.open = !narrow.matches; }
adaptMenu();
narrow.addEventListener('change', adaptMenu);
