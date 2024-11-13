
let form = document.querySelector("form");
form.addEventListener("submit", function(e) {
  let status = document.getElementById("status");
  const options = form.elements.options.value;
  if (options === "") {
    e.preventDefault();
    status.textContent = "Vous devez sélectionner une proposition !";
  }
  else {
    let csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;
    let stop_minutes = document.getElementById("stop_minutes");
    let stop_seconds = document.getElementById("stop_seconds");
    stop_minutes.value = document.getElementById("minutes").textContent;
    stop_seconds.value = document.getElementById("seconds").textContent;
    let question_id = form.elements.question_id.value;
    let current_question_nb = form.elements.current_question_nb.value;
    let nb_of_questions = form.elements.nb_of_questions.value;
    let ids_list = form.elements.ids_list.value;
  }
})