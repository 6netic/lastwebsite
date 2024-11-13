from django.test import TestCase
from hunting_quizz.models import Hunting, Response
from hunting_quizz.views import *
from django.urls import reverse, resolve


class ViewsTest(TestCase):

    def setUp(self):
        Hunting.objects.create(question="Première question ?", choice1="Oui", choice2="Non",
                               choice3="Sans doute", imgdir="/dir1/picture1.jpg", answer=3,
                               ansdesc="Il s'agit d'une question de test", important=False)
    #     Hunting.objects.create(question="Seconde section ?", choice1="Oui", choice2="Non",
    #                            choice3="Sans doute", imgdir="/dir1/picture2.jpg", answer=1,
    #                            ansdesc="Il s'agit d'une question de test", important=True)
    #     Hunting.objects.create(question="Troisième section ?", choice1="Oui", choice2="Non",
    #                            choice3="Sans doute", imgdir="/dir1/picture3.jpg", answer=2,
    #                            ansdesc="Il s'agit d'une question de test", important=True)
    #     Hunting.objects.create(question="Quatrième section ?", choice1="Oui", choice2="Non",
    #                            choice3="Sans doute", imgdir="/dir1/picture2.jpg", answer=1,
    #                            ansdesc="Il s'agit d'une question de test", important=False)
        Response.objects.create(
            quest=Hunting.objects.get(id=1), usranswer=3)
        Response.objects.create(
            quest=Hunting.objects.get(id=1), usranswer=2)


    ###### Testing normal_quizz view ######
    def test_empty_Response_table_in_normal_quizz_view(self):
        """ 1 - Tests if Response table is empty when accessing normal_quizz view function """

        # before_access = Response.objects.all().count()
        response = self.client.get(reverse('hunting_quizz:normal_quizz'))
        # self.client.get(reverse('hunting_quizz:normal_quizz'), {'ids_list': '', 'question_id': ''})
        # after_access = Response.objects.all().count()
        # self.assertEqual(before_access + 1, 2)
        # self.assertEquals(before_access - 2, after_access)

    # def test_ids_list_contains_same_nb_of_questions_than_nb_of_questions(self):
    #     """ 2 - Tests if len(ids_list) equals nb_of_questions """
    #     # In this case, nb_of_questions = 3
    #     self.client = Client()
    #     response = self.client.get(reverse('hunting_quizz:normal_quizz'))
    #     self.assertEquals(len(response.context['ids_list']), 3)

    # def test_normal_quizz_url_points_points_to_correct_view(self):
    #     """ 3 - Tests if normal_quizz url points to correct view function """
    #     url = resolve('/hunting_quizz/normal_quizz')
    #     self.assertEqual(url.func, normal_quizz)

    # def test_normal_quizz_view_200_and_template(self):
    #     """ 4 - Tests if 'normal_quizz' view returns 200 status code and has correct template """
    #     self.client = Client()
    #     response = self.client.get('hunting_quizz/normal_quizz', {'ids_list': '', 'question_id': ''})
    #
    #     # response = self.client.get(reverse('hunting_quizz:normal_quizz'), {'ids_list': '', 'question_id': ''})
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'hunting_quizz/normal_quizz.html')

    # def test_response_is_registered(self):
    #     """ 5 - Tests if chosen response is registered in Response table """
    #     self.client = Client()
    #     response = self.client.get('/hunting_quizz/normal_quizz',
    #                 {'ids_list': '[4, 1, 3]', 'question_id': '4', 'current_question_nb': '1',
    #                  'nb_of_questions': '3', 'stop_time': '10', 'option_ans': 1})
    #     entries = Response.objects.all().count()
    #     self.assertEquals(entries, 3)

    # def test_len_ids_list_is_reduced(self):
    #     """ 6 - Tests if len(ids_list) is reduced when response is given """
    #     self.client = Client()
    #     response = self.client.get(reverse('hunting_quizz:normal_quizz'),
    #                 {'ids_list': '[4, 1, 3]', 'question_id': '4', 'current_question_nb': '1',
    #                  'nb_of_questions': '3', 'stop_time': '10', 'option_ans': 'Oui'})
    #     self.assertEquals(response.context['ids_list'], [1, 3])

    # def test_template_with_empty_list(self):
    #     """ 7 - Tests template when ids_list is empty and number of wrong answers """
    #     self.client = Client()
    #     response = self.client.get(reverse('hunting_quizz:normal_quizz'),
    #                 {'ids_list': '[3]', 'question_id': '3', 'current_question_nb': '3',
    #                  'nb_of_questions': '3', 'stop_time': '100', 'option_ans': 'Oui'})
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'hunting_quizz/results.html')
    #     self.assertEquals(response.context['wrong'], 2)

    ###### Testing assisted_quizz view ######
    # def test_empty_Response_table_in_assisted_quizz_view(self):
    #     """ 1 - Tests if Response table is empty when accessing assisted_quizz view function """
    #     before_access = Response.objects.using('huntingquizz').count()
    #     self.client = Client()
    #     self.client.get('/hunting_quizz/assisted_quizz')
    #     after_access = Response.objects.using('huntingquizz').count()
    #     self.assertEquals(before_access - 2, after_access)

    # def test_len_ids_list_in_assisted_quizz_view(self):
    #     """ 2 - Tests if len(ids_list) equals nb_of_questions in assisted_quizz view """
    #     # In this case, nb_of_questions = 3
    #     self.client = Client()
    #     response = self.client.get(reverse('hunting_quizz:assisted_quizz'))
    #     self.assertEquals(len(response.context['ids_list']), 3)

    # def test_url_code_template_in_assisted_quizz_view(self):
    #     """ 3 - Tests url, status_code and template in assisted_quizz view function """
    #     url = resolve('/hunting_quizz/assisted_quizz')
    #     self.assertEqual(url.func, assisted_quizz)
    #     self.client = Client()
    #     response = self.client.get(reverse('hunting_quizz:assisted_quizz'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'hunting_quizz/assisted_quizz.html')

    # def test_GET_in_assisted_quizz_view(self):
    #     """ 4 - Tests current_question_nb, len(ids_list) in assisted_quizz view """
    #     self.client = Client()
    #     response = self.client.get(reverse('hunting_quizz:assisted_quizz'),
    #                 {'ids_list': '[4, 1, 3]', 'question_id': '4', 'current_question_nb': '1',
    #                  'nb_of_questions': '3', 'score': '0'})
    #     self.assertEquals(response.context['ids_list'], [1, 3])
    #     self.assertEquals(response.context['current_question_nb'], 2)
    #     response = self.client.get(reverse('hunting_quizz:assisted_quizz'),
    #                 {'ids_list': '[3]', 'question_id': '3', 'current_question_nb': '2',
    #                  'nb_of_questions': '3', 'score': '2'})
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'hunting_quizz/results.html')
    #     self.assertEquals(response.context['wrong'], 1)

    # def test_POST_in_assisted_quizz_view(self):
    #     """ 5 - Tests score and Json response in POST method """
    #     self.client = Client()
    #     response = self.client.post(reverse('hunting_quizz:assisted_quizz'),
    #                 {'ids_list': '[3]', 'question_id': '3', 'current_question_nb': '3',
    #                  'nb_of_questions': '3', 'score': '0', 'options': 'Sans doute'})
    #     self.assertEquals(response.json()['reponse'], "Bonne réponse.")
    #     self.assertEquals(response.json()['score'], 1)
    #     self.assertEquals(response.json()['last'], True)
