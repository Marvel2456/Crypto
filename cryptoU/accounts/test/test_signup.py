from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from django.contrib.auth.forms import UserCreationForm
from ..forms import UserRegistrationForm
from django.contrib.auth import get_user_model

# Create your tests here.

User = get_user_model()

class AccountCreationTest(TestCase):
    # Here i will write the test for the sign up page.

    def setUp(self) -> None:
        self.form_class = UserRegistrationForm

    def test_signup_page_exist(self):
        response = self.client.get(reverse('signup_page'))

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed('accounts/signup.html')


    def test_signup_form(self):

        self.assertTrue(issubclass(self.form_class, UserCreationForm))
        self.assertTrue('email' in self.form_class.Meta.fields)
        self.assertTrue('username' in self.form_class.Meta.fields)
        self.assertTrue('password1' in self.form_class.Meta.fields)
        self.assertTrue('password2' in self.form_class.Meta.fields)

        sample_data = {
            "email":"testuser@crypto.com",
            "username":"testuser",
            "password1":"p4ssword###",
            "password2":"p4ssword###"
        }

        form = self.form_class(sample_data)

        self.assertTrue(form.is_valid())

    
    def test_signup_form_create_user_in_db(self):
        user = {
            "email":"testuser@crypto.com",
            "username":"testuser",
            "password1":"p4ssword###",
            "password2":"p4ssword###"
        }

        form = self.form_class(user)

        if form.is_valid():
            form.save()

        self.assertEqual(User.objects.count(), 1)