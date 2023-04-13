from django.db import models
from pages.models import Coin
from . utils import generate_ref_code
from django.contrib.auth import get_user_model



User = get_user_model()

# Create your models here.


class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cryptos = models.ManyToManyField(Coin, through='Holding')
    link = models.CharField(max_length=12, blank=True)
    recommended_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='ref_by')
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username}'s Wallet"
    
    def get_recommended_profiles(self):
        qs = Wallet.objects.all()

        rec_profile = []
        for profile in qs:
            if profile.recommended_by == self.user:
                rec_profile.append(profile)
        return rec_profile

    def save(self, *args, **kwargs):
        if self.link == "":
            link = generate_ref_code()
            self.link = link
        super().save(*args, **kwargs)
    
    @property
    def portfolio_value(self):
        holdings = self.holding_set.all()
        total_value = 0
        for holding in holdings:
            total_value = holding.value + self.balance
        return total_value
    
class Holding(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    crypto = models.ForeignKey(Coin, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=20, decimal_places=2)
    
    def __str__(self):
        return f"{self.crypto.symbol} - {self.quantity}"
    
    @property
    def value(self):
        return self.crypto.price * self.quantity