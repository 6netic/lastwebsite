from django.urls import path
from . import views

app_name = 'hunting_quizz'

urlpatterns = [
    path('', views.index, name='index'),
    # path('index', views.index, name='index'),
    path('apprentissage', views.apprentissage, name='apprentissage'),
    path('normal_quizz', views.normal_quizz, name='normal_quizz'),
    path('assisted_quizz', views.assisted_quizz, name='assisted_quizz'),
    path('slt_max_questions', views.slt_max_questions, name='slt_max_questions'),
    path('assisted_quizz_results', views.assisted_quizz_results, name='assisted_quizz_results'),
]
