
function modifyQuantity(event, prd_id, qty, total) {
    event.preventDefault();
    let formData = new FormData();
    formData.append("prd_id", document.getElementById(prd_id).value);
    formData.append("this_qty", document.getElementById(qty).value);
    let csrfTokenValue = document.querySelector("[name=csrfmiddlewaretoken]").value;
    const request = new Request(
        "", {method: 'POST', body: formData, headers: {'X-CSRFToken': csrfTokenValue}}
    );
    fetch(request)
    .then(response => response.json())
    .then(result => {
        document.getElementById(total).textContent = result["total"] + " €";
        document.getElementById("total_set").textContent = result["total_set"] + " €";
        document.getElementById("cart_tag").textContent = result["nb_in_cart"];
    })
    .catch(function(error) {
            console.log("Impossible de modifier la quantité en question.")
    });
}

function deleteArt(event, prd_id, line) {
    event.preventDefault();
    // let table = document.getElementById("cart-table");
    let formData = new FormData();
    formData.append("prd_id", document.getElementById(prd_id).value);
    let csrfTokenValue = document.querySelector("[name=csrfmiddlewaretoken]").value;
    const request = new Request(
        "/madishop/remove_item/", {method: 'POST', body: formData, headers: {'X-CSRFToken': csrfTokenValue}}
    );
    fetch(request)
    .then(response => response.json())
    .then(result => {
        document.getElementById("cart_tag").textContent = result["nb_in_cart"];
        window.location.href = "/madishop/display_cart/";
    })
    .catch(function(error) {
            console.log("Impossible de modifier la quantité en question.")
    });
}




















































