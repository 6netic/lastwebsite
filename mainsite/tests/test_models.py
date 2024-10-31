from django.test import TestCase
from mainsite.models import Realisations
from os import path


class ViewTest(TestCase):

    def setUp(self):
        Realisations.objects.create(
            name="Application 1",
            description="Il s'agit de l'application 1",
            techno="Django",
            url="http://fakeurl",
            picturemain="pituresfiles/image1"
        )

    def test_realisations_table(self):
        """ - Tests fields on Realisations table """

        obj1 = Realisations.objects.get(id=1)
        field_name_label = obj1._meta.get_field('name').verbose_name
        self.assertEquals(field_name_label, 'name')
        field_name_max_length = obj1._meta.get_field('name').max_length
        self.assertEquals(field_name_max_length, 250)
        field_siren_unique = obj1._meta.get_field('name').blank
        self.assertEquals(field_siren_unique, False)

        field_name_label = obj1._meta.get_field('description').verbose_name
        self.assertEquals(field_name_label, 'description')
        field_siren_unique = obj1._meta.get_field('description').blank
        self.assertEquals(field_siren_unique, False)

        field_name_label = obj1._meta.get_field('techno').verbose_name
        self.assertEquals(field_name_label, 'techno')
        field_name_max_length = obj1._meta.get_field('techno').max_length
        self.assertEquals(field_name_max_length, 100)
        field_siren_unique = obj1._meta.get_field('techno').blank
        self.assertEquals(field_siren_unique, False)

        field_name_label = obj1._meta.get_field('url').verbose_name
        self.assertEquals(field_name_label, 'url')
        field_name_max_length = obj1._meta.get_field('url').max_length
        self.assertEquals(field_name_max_length, 200)
        field_siren_unique = obj1._meta.get_field('url').blank
        self.assertEquals(field_siren_unique, False)

        field_name_label = obj1._meta.get_field('picturemain').verbose_name
        self.assertEquals(field_name_label, 'picturemain')
        field_siren_unique = obj1._meta.get_field('picturemain').blank
        self.assertEquals(field_siren_unique, True)














