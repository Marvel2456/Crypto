from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Portfolio

@receiver(post_save, sender=User)
def create_portfolio(sender, instance, created, **kwargs):

    if created:
        user = instance
        portfolio = Portfolio.objects.create(
            user = user,
            username = user.username,
            email = user.email,
        )


@receiver(post_save, sender=Portfolio)
def update_portfolio(sender, instance, created, **kwargs):

    pass