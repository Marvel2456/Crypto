from django.contrib import admin
from . models import Portfolio, Wallet, MyUser
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = MyUser
    list_display = ['username', 'email', 'is_staff']

admin.site.register(MyUser, CustomUserAdmin)

admin.site.register(Portfolio)
admin.site.register(Wallet)

