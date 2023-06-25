const boton = document.getElementById('boton123');
boton.addEventListener('click', () =>{
    customTranslate();
})



function customTranslate() {
    var $frame = $('.skiptranslate:first');
//    if (!$frame.size()) {
//        alert("Error: Could not find Google translate frame.");
//        return false;
//    }

    console.log($frame.contents()[0].firstChild);
    $frame.contents()[0].firstChild.classList.add("select-form");
    //$frame.contents()[1].value = "GB";


    //$frame.contents().setAttribute("class",'selectpicker');


    //return false;
}