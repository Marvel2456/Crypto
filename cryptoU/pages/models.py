from django.db import models

# Create your models here.

class Coin(models.Model):
    name = models.CharField(max_length=250)
    symbol = models.CharField(max_length=20, unique=True)
    price = models.DecimalField(max_digits=20, decimal_places=4)
    change = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self) -> str:
        return self.name
