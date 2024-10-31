let div_overlay = document.getElementById("overlay");
let timeoutOverlay = null;
function on() {
    div_overlay.style.display = "none";
}
function displayConfirm(mess) {
    document.getElementById("text").textContent = mess;
    div_overlay.style.display = "block";
    timeoutOverlay = setTimeout(on, 2000);
}

function add_in_cart(art_id, size, color, qty) {
    let formData = new FormData();
    formData.append("art_id", art_id);
    // condition si size != '' alors on récupère dans document.getElementById("sizeSlt").value
    if(size !== '') { size = document.getElementById("sizeSlt").value; }
    formData.append("sizeSlt", size);
    if(color !== '') { color = document.getElementById("colorSlt").value; }
    formData.append("colorSlt", color);
    if(qty === 'val') { qty = document.getElementById("chosenQty").value; }
    formData.append("this_qty", qty);
    let csrfTokenValue = document.querySelector("[name=csrfmiddlewaretoken]").value;
    const request = new Request(
        "/madishop/add_to_cart/", {method: 'POST', body: formData, headers: {'X-CSRFToken': csrfTokenValue}}
    );
    fetch(request)
    .then(response => response.json())
    .then(result => {
        document.getElementById("cart_tag").textContent = result["nb_in_cart"];
        displayConfirm(result["message"]);
    })
    .catch(function(error) {
            console.log("Une erreur s'est produite.")
    });
}
