from django.shortcuts import render
import requests
from .models import Coin
from accounts.models import Portfolio

# Create your views here.

def home(request, *args, **kwargs):
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
    
    code = str(kwargs.get('ref_code'))
    
    try:
        portfolio = Portfolio.objects.get(code=code)
        request.session['ref_portfolio'] = portfolio.id
        print('id', portfolio.id)
    except:
        pass
    print(request.session.get_expiry_date())

    coins = Coin.objects.all()
    context = {
        'coins':coins,
        'code':code
    }
    return render(request, 'pages/homepage.html', context)
