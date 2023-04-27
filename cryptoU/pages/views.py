from django.shortcuts import render
import requests
from .models import Coin

# Create your views here.

def home(request):
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1&sparkline=false"
    response = requests.get(url)
    data = response.json()

    for coin_data in data:
        coin = Coin.objects.update_or_create(
            symbol=coin_data["symbol"].upper(),
            defaults={
                "name": coin_data["name"],
                "price": coin_data["current_price"],
                "change": coin_data["price_change_percentage_24h"],
            }
        )

    coins = Coin.objects.all()
    context = {
        'coins':coins
    }
    return render(request, 'pages/homepage.html', context)
