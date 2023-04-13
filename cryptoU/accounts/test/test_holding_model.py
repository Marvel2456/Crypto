from django.test import TestCase
from ..models import Holding
from django.urls import reverse
from django.contrib.auth import get_user_model


User = get_user_model()


class HoldingModelTest(TestCase):

# Test to know if the wallet model exists 
    def test_coin_model_exists(self):
        holding = Holding.objects.count()

        self.assertEqual(holding,0)

    # Test for the string representation of the Wallet objects
    #  I will not be using the user field because i will be using a signal to create the user instance anytime the signup method/test is run
    def test_string_representaiton_of_objects(self):
        holding = Holding.objects.create(
            wallet = "Test user",
            balance = 10
        )

        self.assertEqual(str(holding),holding.wallet)

