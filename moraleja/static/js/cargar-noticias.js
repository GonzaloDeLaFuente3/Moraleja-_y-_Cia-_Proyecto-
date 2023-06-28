
$(document).ready(function() {
  // Llamada inicial a cargarNoticias con offset 0
  cargarNoticias(0);

  $('#cargar-noticias-btn').on('click', function(event) {
    event.preventDefault();
    var offset = $(this).data('offset');
    cargarNoticias(offset);
  });

  function cargarNoticias(offset) {
    var url = '/noticias/cargar/' + offset + '/';
    $.ajax({
      url: url,
      success: function(data) {
        $('#noticias-adicionales-container').append(data);
        $('#cargar-noticias-btn').data('offset', offset+3); // Actualizar el atributo data-offset del botón

        // Verificar si hay menos de 3 noticias adicionales y ocultar el botón
        if ($(data).filter('.noticia-adicional').length < 3) {
            $('#no-more-noticias').show();
          $('#cargar-noticias-btn').hide();

        }
      },
      error: function() {
        console.log('Error al cargar las noticias adicionales');
      }
    });
  }
});