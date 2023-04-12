from django.test import TestCase
from .. models import Coin
from http import HTTPStatus

# Create your tests here.


class HomePageTest(TestCase):

# Here i created a test data that i will use to test the home page
    def setUp(self) -> None:
        Coin.objects.create(
            name = "name 1",
            symbol = "n1",
            price = 12,
            change = 2
        )

    
# Test for homepage 
    def test_homepage_returns_correct_response(self):
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'pages/homepage.html')
        self.assertEqual(response.status_code, HTTPStatus.OK)
