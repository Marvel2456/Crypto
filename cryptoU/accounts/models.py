from django.db import models
from pages.models import Coin
from . utils import generate_ref_code
from django.contrib.auth import get_user_model
import uuid



User = get_user_model()

# Create your models here.


class Portfolio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    referral_link = models.CharField(max_length=12, blank=True)
    recommended_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='ref_by')
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return f"{self.user.username}'s portfolio"
    
    def get_recommended_profiles(self):
        qs = Portfolio.objects.all()

        rec_portfolio = []
        for portfolio in qs:
            if portfolio.recommended_by == self.user:
                rec_portfolio.append(portfolio)
        return rec_portfolio

    def save(self, *args, **kwargs):
        if self.referral_link == "":
            referral_link = generate_ref_code()
            self.referral_link = referral_link
        super().save(*args, **kwargs)


    @property
    def get_total_value(self):
        wallet = self.wallet_set.all()
        totalvalue = sum([item.getvalue for item in wallet])
        return totalvalue


class Wallet(models.Model):
    owner = models.ForeignKey(Portfolio, on_delete=models.CASCADE, blank=True, null=True)
    coin = models.ForeignKey(Coin, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    @property
    def getvalue(self):
        value = self.coin.price * self.quantity
        return value