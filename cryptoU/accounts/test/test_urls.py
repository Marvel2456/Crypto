from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import *
from django.contrib.auth import views as auth_views


class TestUrls(SimpleTestCase):

    def test_signup_url_resolves(self):
        url = reverse('signup_page')
        print(resolve(url))
        self.assertEquals(resolve(url).func, register_user)

    def test_login_url_resolves(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func, login_view)

    def test_logout_url_resolves(self):
        url = reverse('logout')
        print(resolve(url))
        self.assertEquals(resolve(url).func, logout_view)

    def test_dashboard_url_resolves(self):
        url = reverse('dashboard')
        print(resolve(url))
        self.assertEquals(resolve(url).func, dashboard_view)

    def test_wallet_url_resolves(self):
        url = reverse('wallet')
        print(resolve(url))
        self.assertEquals(resolve(url).func, walletView)

    def test_create_wallet_url_resolves(self):
        url = reverse('addwallet')
        print(resolve(url))
        self.assertEquals(resolve(url).func, createWallet)

    def test_update_wallet_url_resolves(self):
        url = reverse('update_wallet', args=['some-id'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, updateWallet)

    def test_delete_wallet_url_resolves(self):
        url = reverse('delete_wallet', args=['some-id'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, deleteWallet)

    

