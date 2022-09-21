from django.test import TestCase, Client

# Create your tests here.
from .views import show_mywatchlist

class MyWatchListTest(TestCase):
    def test_mywatchlisthtml_url_exists(self):
        response = Client().get('/mywatchlist/html/')
        self.assertEqual(response.status_code,200)
    
    def test_mywatchlistjson_url_exists(self):
        response = Client().get('/mywatchlist/json/')
        self.assertEqual(response.status_code,200)

    def test_mywatchlistxml_url_exists(self):
        response = Client().get('/mywatchlist/xml/')
        self.assertEqual(response.status_code,200)
    
    