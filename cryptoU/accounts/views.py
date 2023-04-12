from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

# Create your views here.



def register_user(request):
    form = UserRegistrationForm(request.POST)

    if form.is_valid():
        form.save()

        return redirect('login')

    context = {
        'form':form
    }
    return render(request, 'accounts/signup.html', context)


def login_view(request):
    form = AuthenticationForm()

    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

                return redirect(reverse('homepage'))

    context = {
        'form':form
    }
    return render(request, 'accounts/login.html', context)


def logout_view(request):
    logout(request)
    return redirect(reverse('homepage'))