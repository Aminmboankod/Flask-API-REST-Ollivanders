///////////////////////////// CORS ////////////////////////////

const miHeaders = new Headers();



//////////////////////////// GET //////////////////////////////

const inventButton = document.querySelector('#inventario');
inventButton.addEventListener("click", inventario);

function inventario() {
    fetch('http://localhost:5000/inventario')
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




////////////////////////// POST ////////////////////////////

// let formulario = document.querySelector('.add-item');
// formulario.addEventListener('submit', addItem);

// function addItem(e) {
//     e.preventDefault();
//     // elementos del formulario en un array-like object:

//     logForm();

//     let data = { name:    this.elements.name.value,
//                  sell_in: this.elements.sell_in.value,
//                  quality: this.elements.quality.value};

//     fetch('http://127.0.0.1:5000/items', {
//         method: 'POST',
//         body: JSON.stringify(data),
//         headers: {
//             'Content-Type': 'application/json'
//         }
//     })
//         .then((response) => {
//             if (response.ok) {
//                 console.log("Response OK Status:", response.status);
//                 console.log("Reponse OK status text:", response.statusText);
//             }
//         })
//         .catch((error) => {
//             console.log(error.message);
//         });
// }

// //////////////////////////// DELETE ////////////////////////////////////

// formulario.delete.addEventListener('click', deleteItem);

// function deleteItem() {

//     logForm();

//     let data = { name: formulario.elements.name.value,
//                  sell_in: formulario.elements.sell_in.value,
//                  quality: formulario.elements.quality.value };

//     fetch('http://127.0.0.1:5000/items', {
//         method: 'DELETE',
//         body: JSON.stringify(data),
//         headers: {
//             'Content-Type': 'application/json'
//         }
//     })
//         .then((response) => {
//             if (response.ok) {
//                 console.log("Response OK Status:", response.status);
//                 console.log("Reponse OK status text:", response.statusText);
//             }
//         })
//         .catch((error) => {
//             console.log(error.message);
//         });
// }


// function logForm() {

//     let formulario = document.querySelector('.add-item');
//     console.log( formulario.elements.name.value,
//                  formulario.elements.sell_in.value,
//                  formulario.elements.quality.value);
// }
