from django.test import TestCase
from hunting_quizz.models import Hunting, Response


class HuntingQuizzTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Hunting.objects.create(question="Première question ?", choice1="Oui", choice2="Non",
                               choice3="Sans doute", imgdir="/dir1/picture1.jpg", answer=3,
                               ansdesc="Il s'agit d'une question de test", important=False)
        Hunting.objects.create(question="Seconde section ?", choice1="Oui", choice2="Non",
                               choice3="Sans doute", imgdir="/dir1/picture2.jpg", answer=1,
                               ansdesc="Il s'agit d'une question de test", important=True)
        Hunting.objects.create(question="Troisième section ?", choice1="Oui", choice2="Non",
                               choice3="Sans doute", imgdir="/dir1/picture3.jpg", answer=2,
                               ansdesc="Il s'agit d'une question de test", important=True)
        Hunting.objects.create(question="Quatrième section ?", choice1="Oui", choice2="Non",
                               choice3="Sans doute", imgdir="/dir1/picture2.jpg", answer=1,
                               ansdesc="Il s'agit d'une question de test", important=False)
        Response.objects.create(
            quest=Hunting.objects.get(id=1), usranswer=3)
        Response.objects.create(
            quest=Hunting.objects.get(id=2), usranswer=2)

    def test_hunting_table(self):
        """ - Tests fields on Hunting table """

        obj1 = Hunting.objects.get(id=1)
        field_name_label = obj1._meta.get_field('question').verbose_name
        self.assertEquals(field_name_label, 'question')
        field_name_max_length = obj1._meta.get_field('question').max_length
        self.assertEquals(field_name_max_length, 255)
        field_siren_unique = obj1._meta.get_field('question').blank
        self.assertEquals(field_siren_unique, False)
        field_name_label = obj1._meta.get_field('choice1').verbose_name
        self.assertEquals(field_name_label, 'choice1')
        field_name_max_length = obj1._meta.get_field('choice1').max_length
        self.assertEquals(field_name_max_length, 200)
        field_siren_unique = obj1._meta.get_field('choice1').blank
        self.assertEquals(field_siren_unique, False)
        field_name_label = obj1._meta.get_field('choice3').verbose_name
        self.assertEquals(field_name_label, 'choice3')
        field_name_max_length = obj1._meta.get_field('choice3').max_length
        self.assertEquals(field_name_max_length, 200)
        field_siren_unique = obj1._meta.get_field('choice3').blank
        self.assertEquals(field_siren_unique, True)
        field_name_label = obj1._meta.get_field('imgdir').verbose_name
        self.assertEquals(field_name_label, 'imgdir')
        field_name_max_length = obj1._meta.get_field('imgdir').max_length
        self.assertEquals(field_name_max_length, 250)
        field_siren_unique = obj1._meta.get_field('imgdir').blank
        self.assertEquals(field_siren_unique, False)
        field_name_label = obj1._meta.get_field('answer').verbose_name
        self.assertEquals(field_name_label, 'answer')
        field_siren_unique = obj1._meta.get_field('answer').blank
        self.assertEquals(field_siren_unique, False)
        field_name_label = obj1._meta.get_field('ansdesc').verbose_name
        self.assertEquals(field_name_label, 'ansdesc')
        field_name_max_length = obj1._meta.get_field('ansdesc').max_length
        self.assertEquals(field_name_max_length, 400)
        field_siren_unique = obj1._meta.get_field('ansdesc').blank
        self.assertEquals(field_siren_unique, False)
        field_name_label = obj1._meta.get_field('important').verbose_name
        self.assertEquals(field_name_label, 'important')
        field_default = obj1._meta.get_field('important').default
        self.assertEquals(field_default, False)

    def test_response_table(self):
        """ - Tests fields on Response table """

        obj1 = Response.objects.get(id=1)
        field_name_label = obj1._meta.get_field('quest').verbose_name
        self.assertEquals(field_name_label, 'quest')
        self.assertEquals(obj1.quest.question, "Première question ?")
        field_name_label = obj1._meta.get_field('usranswer').verbose_name
        self.assertEquals(field_name_label, 'usranswer')
        field_siren_unique = obj1._meta.get_field('usranswer').blank
        self.assertEquals(field_siren_unique, False)