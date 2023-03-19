///////////////////////////// CORS ////////////////////////////

const miHeaders = new Headers();



//////////////////////////// GET //////////////////////////////

const inventButton = document.querySelector('#inventario');
inventButton.addEventListener("click", inventario);

function inventario() {
    fetch('http://127.0.0.1/:5000/inventario')
        .then((response) => {
            if(response.ok) {
                console.log("Response Status:", response.status);
                console.log("Reponse statuts text:", response.statusText);
                response.json().then((json) => logItems(json))
            } else {
                console.log("Response Status:", response.status);
                console.log("Reponse statuts text:", response.statusText); 
            }  
        })
        .catch((error) => {
            console.log(error.message);
        });
}

function get_item(name) {
    fetch(`http://localhost:5000/item/${name}`)
        .then((response) => {
            if(response.ok) {
                console.log("Response Status:", response.status);
                console.log("Reponse statuts text:", response.statusText);
                response.json().then((json) => logItems(json))
            } else {
                console.log("Response Status:", response.status);
                console.log("Reponse statuts text:", response.statusText); 
            }  
        })
        .catch((error) => {
            console.log(error.message);
        });
}

