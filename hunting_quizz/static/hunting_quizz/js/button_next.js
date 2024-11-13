
function nextButton(thescore, last, new_list, question_nb, total_questions) {
  // Erase 'Je Valide' button
  const checkBtn = document.getElementById("valid");
  checkBtn.innerHTML = "";
  const formular = document.createElement('form');
  formular.setAttribute("method", "GET");
  // Creates 'ids_list' input
  const ids_list = document.createElement("input");
  ids_list.setAttribute("type", "hidden");
  ids_list.setAttribute("name", "ids_list");
  ids_list.setAttribute("value", new_list);
  // Creates 'score' input
  const score = document.createElement("input");
  score.setAttribute("type", "hidden");
  score.setAttribute("name", "score");
  score.setAttribute("value", thescore);
  // Creates 'current_question_nb' input
  const current_question_nb = document.createElement("input");
  current_question_nb.setAttribute("type", "hidden");
  current_question_nb.setAttribute("name", "current_question_nb");
  current_question_nb.setAttribute("value", question_nb);
  // Creates 'nb_of_questions' input
  const nb_of_questions = document.createElement("input");
  nb_of_questions.setAttribute("type", "hidden");
  nb_of_questions.setAttribute("name", "nb_of_questions");
  nb_of_questions.setAttribute("value", total_questions);
  // Creates 'Question suivante' or 'Afficher les résultats' button
  const nextBtn = document.createElement("button");
  nextBtn.setAttribute("class", "btn btn-success validateBtn");
  if (last === true) {
    nextBtn.textContent = "Afficher les résultats";
    formular.setAttribute("action", "assisted_quizz_results");
    formular.appendChild(nextBtn);
    formular.appendChild(score);
    formular.appendChild(nb_of_questions);
  }
  else {
    nextBtn.textContent = "Question suivante";
    formular.setAttribute("action", "assisted_quizz");
    formular.appendChild(nextBtn);
    formular.appendChild(ids_list);
    formular.appendChild(score);
    formular.appendChild(current_question_nb);
    formular.appendChild(nb_of_questions);
  }
  // Adds the form to formtag tag
  const formtag = document.getElementById("formtag");
  formtag.appendChild(formular);
}
