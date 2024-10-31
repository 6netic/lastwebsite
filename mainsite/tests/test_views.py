from django.test import TestCase
from django.urls import reverse, resolve
from mainsite.views import home, realisations, services, contact
from os import path


class ViewTest(TestCase):

    def test_home_view(self):
        """ 1- Tests home url points to 'home' function view, 'home' func returns 200 and has the correct template """
        url1 = resolve("/")
        url2 = resolve("/mainsite/")
        self.assertEqual(url1.func, home)
        self.assertEqual(url2.func, home)

        response = self.client.get(reverse("home"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "mainsite/index.html")

    def test_realisations_view(self):
        """ 2- Tests realisations url points to 'realisations' function view,
            'realisations' func returns 200 and has the correct template with its context.
        """
        url = resolve("/mainsite/realisations/")
        self.assertEqual(url.func, realisations)

        response = self.client.get(reverse("realisations"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "mainsite/realisations.html")
        self.assertIn('realisations', response.context)

    def test_services_view(self):
        """ 3- Tests services url points to 'services' function view, 'services' func returns 200 and has the correct template """
        url = resolve("/mainsite/services/")
        self.assertEqual(url.func, services)

        response = self.client.get(reverse("services"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "mainsite/services.html")

    def test_contact_view(self):
        """ 4- Tests contact url points to 'contact' function view, 'contact' func returns 200 and has the correct template """
        url = resolve("/mainsite/contact/")
        self.assertEqual(url.func, contact)

        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "mainsite/contact.html")











