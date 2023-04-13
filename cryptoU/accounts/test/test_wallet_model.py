from django.test import TestCase
from ..models import Wallet
from django.urls import reverse
from django.contrib.auth import get_user_model


User = get_user_model()


class WalletModelTest(TestCase):

# Test to know if the wallet model exists 
    def test_coin_model_exists(self):
        wallet = Wallet.objects.count()

        self.assertEqual(wallet,0)

    # Test for the string representation of the Wallet objects
    #  I will not be using the user field because i will be using a signal to create the user instance anytime the signup method/test is run
    def test_string_representaiton_of_objects(self):
        wallet = Wallet.objects.create(
            cryptos = "TN",
            link = "e3445ww",
            balance = 10
        )

        self.assertEqual(str(wallet),wallet.cryptos.set())

