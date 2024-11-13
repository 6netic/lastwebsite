from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse, HttpResponse
from hunting_quizz.forms import add_question_form
from hunting_quizz.models import Hunting, Response, Resume, Resumecat
from hunting_quizz.utils import make_newlist
from django.utils.html import escape
import random


def index(request):
    """ Homepage view """

    return render(request, 'hunting_quizz/index.html')


def apprentissage(request):
    """ Leads to Apprentissage page """

    resume = Resume.objects.all()
    resumecat = Resumecat.objects.all()
    return render(request, 'hunting_quizz/apprentissage.html', locals())


def normal_quizz(request):
    """ Normal quizz view """

    picture_id = random.choice([1, 2, 3])
    # Answer submitted by user
    if request.POST.get('ids_list'):
        option_ans = int(escape(request.POST.get('options')))
        question_id = int(request.POST.get('question_id'))
        old_list = escape(request.POST.get('ids_list'))
        ids_list = make_newlist(old_list, question_id)
        current_question_nb = int(request.POST.get('current_question_nb')) + 1
        nb_of_questions = int(request.POST.get('nb_of_questions'))
        minutes = request.POST.get('stop_minutes')
        seconds = request.POST.get('stop_seconds')
        record_answer = Response.objects.create(
            quest=Hunting.objects.get(id=question_id),
            usranswer=option_ans
        )
        # No more questions left, results will be calculated
        if len(ids_list) == 0:
            score = 0
            failed = []
            all_resp = Response.objects.all()
            for one in all_resp:
                if one.usranswer == one.quest.answer:
                    score += 1
                if one.usranswer != one.quest.answer and one.quest.important is True:
                    one_tuple = (one.quest.question, one.quest.ansdesc)
                    failed.append(one_tuple)
            percent = round((score / nb_of_questions) * 100)
            wrong = nb_of_questions - score
            time_spent = minutes + ":" + seconds
            return render(request, 'hunting_quizz/results.html', locals())
        # Other questions to display
        questions = Hunting.objects.filter(pk__in=ids_list)
        return render(request, 'hunting_quizz/normal_quizz.html', locals())
    # First access to the page
    else:
        # Starting point of the program
        nb_of_questions, current_question_nb, iterat, ids_list, minutes, seconds = 5, 1, 1, [], '00', '00'
        Response.objects.all().delete()
        all_questions = Hunting.objects.all().count()
        while iterat <= nb_of_questions:
            i = random.randint(1, all_questions)
            if i not in ids_list:
                ids_list.append(i)
                iterat += 1
        questions = Hunting.objects.filter(pk__in=ids_list)
        return render(request, 'hunting_quizz/normal_quizz.html', locals())


def slt_max_questions(request):
    """ View to define max nb of questions to show """
    return render(request, "hunting_quizz/select_max_questions.html")


def assisted_quizz(request):
    """ Assisted view for Hunting_quizz """

    picture_id = random.choice([1, 2, 3])
    if request.POST.get('ids_list'):
        old_list = escape(request.POST.get('ids_list'))
        question_id = int(request.POST.get('question_id'))
        ids_list = make_newlist(old_list, question_id)
        option_ans = int(escape(request.POST.get('options')))
        current_question_nb = int(request.POST.get('current_question_nb'))
        nb_of_questions = int(request.POST.get('nb_of_questions'))
        score = int(request.POST.get('score'))
        current_question = Hunting.objects. \
            filter(id=question_id).values_list('answer', 'ansdesc', 'important', 'question')
        reponse = ""
        if option_ans == current_question[0][0]:
            score += 1
            reponse = "Bonne réponse"
            if current_question[0][2] == True:
                reponse = "Il s'agit d'une question éliminatoire et la réponse est la bonne."
        if option_ans != current_question[0][0]:
            reponse = "Mauvaise réponse"
            if current_question[0][2] == True:
                reponse = "Il s'agit d'une question éliminatoire et la réponse est fausse. Votre test a donc échoué."
                end = True
                print("end vaut:", end)
                print(reponse)
                return JsonResponse(status=200, data={
                    "end_mess": "Il s'agissait d'une question éliminatoire. Vous avez échoué au test.",
                    "question": current_question[0][3],
                    "bonne_rep": current_question[0][1]
                })
        if len(ids_list) == 0:
            last = True
        else:
            last = False
        return JsonResponse(status=200, data={
            "reponse": reponse,
            "explications": current_question[0][1],
            "score": score,
            "last": last,
            "ids_list": ids_list,
            "current_question_nb": current_question_nb,
            "total_questions": nb_of_questions
        })
    if request.GET.get('ids_list'):
        old_list = escape(request.GET.get('ids_list'))
        ids_list = make_newlist(old_list)
        current_question_nb = int(escape(request.GET.get('current_question_nb'))) + 1
        nb_of_questions = int(request.GET.get('nb_of_questions'))
        score = int(request.GET.get('score'))
        questions = Hunting.objects.filter(pk__in=ids_list)
        return render(request, 'hunting_quizz/assisted_quizz.html', locals())
    # Point de départ
    if request.GET.get("nb_of_quest"):
        nb_of_questions = int(escape(request.GET.get("nb_of_quest")))
        Response.objects.all().delete()
        current_question_nb, iterat, ids_list, score = 1, 1, [], 0
        while iterat <= nb_of_questions:
            i = random.randint(1, Hunting.objects.all().count())
            if i not in ids_list:
                ids_list.append(i)
                iterat += 1
        questions = Hunting.objects.filter(pk__in=ids_list)
        return render(request, 'hunting_quizz/assisted_quizz.html', locals())


def assisted_quizz_results(request):
    """ Results for Assisted view in Hunting_quizz """

    score = int(request.GET.get('score'))
    nb_of_questions = int(request.GET.get('nb_of_questions'))
    percent = round((score / nb_of_questions) * 100)
    wrong = nb_of_questions - score
    return render(request, 'hunting_quizz/results.html', locals())


