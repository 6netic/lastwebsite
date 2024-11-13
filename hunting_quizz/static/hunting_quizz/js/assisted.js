
let form = document.querySelector("form");
form.addEventListener("submit", function(e) {
  e.preventDefault();
  // For displaying the response
  let status = document.getElementById("status");
  let verify = document.getElementById("verify");
  // Verify if an option=choice is selected
  let options = form.elements.options.value;
  if (options === "") {
    status.textContent = "Vous devez sélectionner une proposition !";
  }
  else {
    let csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;
    let request = new Request("assisted_quizz", { headers: { 'X-CSRFToken': csrftoken }});
    var formData = new FormData();
	formData.append('options', options);
	formData.append('question_id', form.elements.question_id.value);
	formData.append('current_question_nb', form.elements.current_question_nb.value);
	formData.append('nb_of_questions', form.elements.nb_of_questions.value);
	formData.append('ids_list', form.elements.ids_list.value);
	formData.append('score', form.elements.score.value);
	fetch(request, { method: "POST", mode: "same-origin", body: formData })
    .then(function(response) {
      if(response.status !== 200) {
        console.log("La requête n'a pas abouti à cause d'une erreur.");
      }
      response.json().then(function(data) {
        if (data.end_mess) {
            document.getElementById("infos").innerHTML = "<p></p>";
            document.getElementById("question_form").innerHTML = "<p align='center'><b>" + data.end_mess + "</b></p>";
            document.getElementById("question_form").innerHTML += "<p align='center'>" + data.bonne_rep + "</p>";
        }
        else {
        status.textContent = "";
        verify.innerHTML = data.reponse + "<br>";
        verify.innerHTML += data.explications + "<br>";
        // verify.innerHTML += data.eliminatoire + "<br>";
        const thescore = data.score;
        const last = data.last;
        const total_questions = data.total_questions;
        var new_list = data.ids_list;
        const question_nb = data.current_question_nb;
        nextButton(thescore, last, new_list, question_nb, total_questions);
        }
      })
    })
  }
})
