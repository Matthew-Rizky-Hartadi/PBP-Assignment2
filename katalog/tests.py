
from django.test import TestCase, Client
<<<<<<< HEAD
from django.test import TestCase
=======

from django.test import TestCase

>>>>>>> 34a3e2dbb6856bb1ad9f828ff957b6239ab9172d
from django.urls import resolve
from .views import show_katalog
# Create your tests here.

class KatalogTest(TestCase):
    def test_katalog_url_exists(self):
        response = Client().get('/katalog/')
        self.assertEqual(response.status_code,200)
    
    def test_katalog_using_template(self):
        response = Client().get('/katalog/')
        self.assertTemplateUsed(response, 'katalog.html')

