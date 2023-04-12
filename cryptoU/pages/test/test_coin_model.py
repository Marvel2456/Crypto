from django.test import TestCase
from .. models import Coin
from http import HTTPStatus

# Create your tests here.


# Here i will be testing the coin model

class CoinModelTest(TestCase):

# Test to assertain the count model exists 

    def test_coin_model_exists(self):
        coin = Coin.objects.count()

        self.assertEqual(coin,0)


# Test for the string representation of the Coin objects

    def test_string_representaiton_of_objects(self):
        coin = Coin.objects.create(
            name = "Test name",
            symbol = "TN",
            price = 10,
            change = 2
        )

        self.assertEqual(str(coin),coin.name)
