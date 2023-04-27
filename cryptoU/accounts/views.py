from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import *
# Create your views here.



def register_user(request):
    portfolio_id = request.session.get('ref_wallet')
    form = UserRegistrationForm(request.POST)

    if form.is_valid():
        if portfolio_id is not None:
            recommended_by_profile = Portfolio.objects.get(id=portfolio_id)
            instance = form.save()
            registered_user = User.objects.get(id=instance.id)
            registered_profile = Portfolio.objects.get(user=registered_user)
            registered_profile.recommended_by = recommended_by_profile.user
            registered_profile.save()
        else:
            form.save()
        return redirect('login')
    
    else:
        form = UserRegistrationForm()

    context = {
        'form':form
    }
    return render(request, 'accounts/signup.html', context)

def referral_signup(request, referral_link):
    referring_user = Wallet.objects.get(link=referral_link)
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
        user = form.save(commit=False)
        user.referred_by = referring_user
        user.save()
        Portfolio.objects.create(user=user)
        referring_user.balance += 10.0  # add bonus points
        referring_user.save()
        return redirect('home')
    
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

                return redirect(reverse('dashboard'))

    context = {
        'form':form
    }
    return render(request, 'accounts/login.html', context)


def dashboard_view(request):
    
    portfolio = Portfolio.objects.all().filter(user = request.user)


    context = {
        'portfolio':portfolio,
    }
    return render(request, 'accounts/dashboard.html', context)


def logout_view(request):
    logout(request)
    return redirect(reverse('homepage'))