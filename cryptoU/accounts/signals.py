from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyUser
from .models import Portfolio

@receiver(post_save, sender=MyUser)
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

@receiver(post_save, sender=Portfolio)
def delete_portfolio(sender, instance, created, **kwargs):

    pass