var typed = new Typed('#typed', {
    stringsElement: '#typed-strings',
    typeSpeed: 40,
    loop: true,
    loopCount: Infinity,
    smartBackSpace: true,
});


$('#myModal').on('shown.bs.modal', function () {
    $('#myInput').trigger('focus')
})

// PRELOADER CODE
var overlay = document.getElementById("overlay");

window.addEventListener('load', function () {
    overlay.style.display = 'none';
})
