from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model


User = get_user_model()

class LogoutTest(TestCase):

# Dummy data to test the logout

    def setUp(self) -> None:
        self.username = "testuser12"
        self.email = "test12@crypto.com"
        self.password = "p2ssword###"
        
        User.objects.create_user(
            username = self.username,
            email = self.email,
            password = self.password
        )

    
    def test_logout_user(self):
        self.client.login(username = self.username, password = self.password)
        

        self.assertTrue('_auth_user_id' in self.client.session)

        # Here i made a request to remove the session

        response = self.client.get(reverse('logout'))

        self.assertFalse('_auth_user_id' in self.client.session)