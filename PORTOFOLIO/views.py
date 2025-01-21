from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from Stock_Data.models import Stock
from News.models import News
from Stock_Data.utils import get_stock_data  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


class HomePageView(TemplateView):
    template_name = 'Home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Define the top 10 Nasdaq stock symbols
        nasdaq_symbols = ["AAPL", "MSFT", "AMZN", "GOOGL", "FB", "TSLA", "NVDA", "PYPL", "NFLX", "ADBE"]

        # Get real-time data for each symbol
        nasdaq_stocks_data = []
        for symbol in nasdaq_symbols:
            stock_data = get_stock_data(symbol)
            if stock_data:
                nasdaq_stocks_data.append({
                    'symbol': symbol,
                    **stock_data
                })

        # Add the stock data to the context
        context['nasdaq_stocks'] = nasdaq_stocks_data
        context['latest_stocks'] = Stock.objects.all()[:5]
        context['latest_news'] = News.objects.all()[:5]

        # Sample data for market cap and trading volume
        context['market_cap'] = "$2,397,781,723,907"  # Replace with real data if available
        context['trading_volume'] = "$110,904,272,676"  # Replace with real data if available

        # Add trending stocks and largest gainers
        context['trending_stocks'] = [
            {'symbol': 'AAPL', 'price': '$150.00', 'change': '+1.5%'},
            {'symbol': 'TSLA', 'price': '$700.00', 'change': '+2.0%'},
            {'symbol': 'AMZN', 'price': '$3,200.00', 'change': '+3.0%'},
        ] 
        
        context['largest_gainers'] = [
            {'symbol': 'GME', 'price': '$150.00', 'change': '+10.0%'},
            {'symbol': 'AMC', 'price': '$50.00', 'change': '+8.5%'}, 
            {'symbol': 'TSLA', 'price': '$700.00', 'change': '+6.0%'},
        ]
        return context




# Authentication views (login, logout, register)
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Username atau password salah'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            try:
                User.objects.create_user(username=username, password=password1)
                messages.success(request, "Pendaftaran berhasil! Silakan login.")
                return redirect('login')
            except Exception as e:
                messages.error(request, f"Error: {e}")
        else:
            messages.error(request, "Password tidak cocok.")
    return render(request, 'register.html')
