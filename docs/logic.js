
var contador = 1

function inventario() {
    const xhttp = new XMLHttpRequest();

    xhttp.onload = function() {
        let data = JSON.parse(this.responseText);

        // Verificar que la sección exista
        if (!document.getElementById("section")) {
            document.body.innerHTML += "<section id='section'></section>";
        }

        // Crear la tabla
        let table = "<table><tr><th>Nombre</th><th>Caducidad</th><th>Calidad</th></tr>";
        for (let i = 0; i < data.length; i++) {
            let name = data[i].name;
            let sell_in = data[i].sell_in;
            let quality = data[i].quality;

            // Crear una fila para cada conjunto de datos
            let row = "<tr><td>" + name + "</td><td>" + sell_in + "</td><td>" + quality + "</td></tr>";
            table += row;
        }
        table += "</table>";

        // Agregar la tabla a la sección
        document.getElementById("section").innerHTML += table;
    };

    xhttp.open("GET", "http://127.0.0.1:5000/inventario");
    xhttp.send();
}

function actualizar() {
    const xhttp = new XMLHttpRequest();
    xhttp.open("GET", "http://127.0.0.1:5000/actualizar");
    xhttp.send();
    inventario();
}

function reiniciar() {
    const xhttp = new XMLHttpRequest();
    xhttp.open("GET", "http://127.0.0.1:5000/reiniciar");
    xhttp.send();
    inventario();
    
}