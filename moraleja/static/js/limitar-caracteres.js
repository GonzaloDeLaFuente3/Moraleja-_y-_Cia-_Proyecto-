document.addEventListener('DOMContentLoaded', function() {
  var maxCaracteres = 140; // Número máximo de caracteres permitidos
  var descripciones = document.getElementsByClassName('descripcion');

  for (var i = 0; i < descripciones.length; i++) {
    var descripcionElement = descripciones[i];
    var descripcionTexto = descripcionElement.textContent;

    if (descripcionTexto.length > maxCaracteres) {
      var textoCortado = descripcionTexto.substring(0, maxCaracteres) + '...';
      descripcionElement.textContent = textoCortado;
    }
  }
});
