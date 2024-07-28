    
function cargar(){

    fetch(`http://127.0.0.1:8000/api/1.0/Configuracion/`)
    .then(data => data.json())
    .then(data => {
    let company = document.getElementById('company')
    let contact = document.getElementById('cel')
    let correo = document.getElementById('cor')
    let ubicacion = document.getElementById('ubi')


    company.innerText = data[0].nombre
    contact.innerText = `Telefono : ${data[0].contacto}`
    correo.innerText = `Correo : ${data[0].correo}`  
    ubicacion.innerText = `Ubicacion : ${data[0].ubicacion}`

    })

}
    
