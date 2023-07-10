
function loadGoogleTranslate() {
  new google.translate.TranslateElement({pageLanguage: 'es',
    autoDisplay: false, includedLanguages:'es,en',
    layout: google.translate.TranslateElement.InlineLayout.HORIZONTAL,
     multilanguagePage: true,

}, 'google_element');

}

//Aparece un boton para recargar la página cuando esta no detecta el traductor por x razon
setTimeout(function() {
    const selectElement = document.querySelector('#google_element select');
    if (!(selectElement instanceof HTMLSelectElement)) {
        const reload = document.getElementById('reload');
        reload.classList.remove('d-none');
    }
}, 1000);

