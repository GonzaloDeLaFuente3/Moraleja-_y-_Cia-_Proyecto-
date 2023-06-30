$(document).ready(function() {
    const inputBusqueda = document.getElementById('buscar-item');
    const btnBuscar = document.getElementById('btn-buscar-item');

      inputBusqueda.addEventListener('keyup', function(event) {
        if (event.keyCode === 13) {
          event.preventDefault();
          $('#btn-buscar-item').click();
        }
      });

  $('#btn-buscar-item').on('click', function() {
    var textoBusqueda = $('#buscar-item').val().toLowerCase();
    var items = $('.testimonial-carousel .product-item');
    var itemEncontrado = false;

    $('#alerta-item-no-encontrado').addClass('d-none');

    items.each(function(index) {
      var nombreitem = $(this).find('.h5').text().toLowerCase();

      if (nombreitem.includes(textoBusqueda)) {
        itemEncontrado = true;
        $('.testimonial-carousel').trigger('to.owl.carousel', index);
        return false; // Detener el bucle each cuando se encuentra el item
      }
    });

    if (!itemEncontrado) {
        $('#alerta-item-no-encontrado').removeClass('d-none');
    }
  });
});
