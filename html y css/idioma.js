const selectIdioma = document.getElementsByClassName("goog-te-combo");

function accion(){
    const tabla = document.createElement('tr');
    tabla.innerHTML =`
        <td scope="row">${cliente.id}</th>
            <td>${cliente.cuil}</td>
            <td>${cliente.nombre}</td>
            <td>${cliente.apellido}</td>
            <td>${cliente.barrio}</td>
            <td>${cliente.localidad}</td>
            <td>${cliente.zona}</td>
            <td>${cliente.telefono}</td>
            <td>
                <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#modalModificarCliente" id="modificar${cliente.id}"><i class="bi bi-pencil-square"></i></button>
                <button class="btn btn-danger mx-2" id="eliminar${cliente.id}" ><i class="bi bi-trash-fill"></i></button>
            </td>
        `

    selectIdioma.appendChild();
}