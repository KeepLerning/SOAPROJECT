from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView
from .models import UserWatchlist
from Stock_Data.models import Stock
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from Stock_Data.utils import get_stock_data

# Daftar watchlist pengguna dengan harga real-time
@method_decorator(login_required, name='dispatch')
class WatchlistView(ListView):
    model = UserWatchlist
    template_name = 'watchlist.html'
    context_object_name = 'watchlist'

    def get_queryset(self):
        watchlist = UserWatchlist.objects.filter(user=self.request.user)
        updated_watchlist = []

        for item in watchlist:
            stock_data = get_stock_data(item.stock.symbol)
            current_price = stock_data.get('current_price') if stock_data else None
            updated_watchlist.append({
                "id": item.stock.id,
                "symbol": item.stock.symbol,
                "company_name": item.stock.company_name,
                "current_price": current_price
            })

        return updated_watchlist


# Menambah saham ke watchlist
@login_required
def add_to_watchlist(request, stock_id):
    stock = get_object_or_404(Stock, id=stock_id)
    UserWatchlist.objects.get_or_create(user=request.user, stock=stock)
    return redirect('watchlist')

# Menghapus saham dari watchlist
@login_required
def remove_from_watchlist(request, stock_id):
    stock = get_object_or_404(Stock, id=stock_id)
    UserWatchlist.objects.filter(user=request.user, stock=stock).delete()
    return redirect('watchlist')

@login_required
def get_real_time_prices(request):
    watchlist = UserWatchlist.objects.filter(user=request.user)
    prices = []
    for item in watchlist:
        stock_data = get_stock_data(item.stock.symbol)  # Fetch real-time data
        if stock_data:
            prices.append({
                "id": item.stock.id,
                "current_price": stock_data.get("current_price")
            })
    return JsonResponse({"prices": prices})