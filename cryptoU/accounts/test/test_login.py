from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model


User = get_user_model()


class LoginTest(TestCase):

    def setUp(self) -> None:
        self.username = "testuser"
        self.email = "testuser@crypto.com"
        self.password = "p4ssword###"

        User.objects.create_user(
            username = self.username,
            email = self.email,
            password = self.password
        )


    def test_login_page_exists(self):
        response = self.client.get(reverse('login'))

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'accounts/login.html')

    
    def test_login_page_has_form(self):
        response = self.client.get(reverse('login'))
        form = response.context.get('form')

        self.assertIsInstance(form, AuthenticationForm)



    def test_login_page_logs_in_users(self):
        user_data = {
            'username':self.username,
            'password':self.password
        }

        response = self.client.post(reverse('login'), user_data)

        self.assertRedirects(response, reverse('dashboard'))


   