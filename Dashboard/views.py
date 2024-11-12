from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from Stock_Data.models import Stock
from Stock_Data.utils import get_stock_data  # Pastikan untuk menggunakan fungsi yang baru
import logging
from News.models import News


logger = logging.getLogger(__name__)

@method_decorator(login_required, name='dispatch')  # Terapkan login_required
class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Fetch stock data (already implemented in your view)
        context['stocks'] = Stock.objects.all()
        for stock in context['stocks']:
            stock_data = get_stock_data(stock.symbol)
            if stock_data:
                stock.current_price = stock_data['current_price']
                stock.market_cap = stock_data['market_cap']
                stock.high_52_week = stock_data['high_52_week']
                stock.low_52_week = stock_data['low_52_week']
            else:
                stock.current_price = "Tidak tersedia"
                stock.market_cap = "Tidak tersedia"
                stock.high_52_week = "Tidak tersedia"
                stock.low_52_week = "Tidak tersedia"

        # Fetch the latest news articles (e.g., the last 5 articles)
        context['latest_news'] = News.objects.order_by('-published_at')[:5]
        
        return context

# View untuk mendapatkan data saham dalam format JSON
def fetch_stock_data(request):
    stocks = Stock.objects.all()
    stock_data = []

    for stock in stocks:
        stock_info = get_stock_data(stock.symbol)  # Ambil data saham secara real-time
        if stock_info:
            stock_data.append({
                'symbol': stock.symbol,
                'market_cap': stock_info['market_cap'],
                'high_52_week': stock_info['high_52_week'],
                'low_52_week': stock_info['low_52_week'],
                'current_price': stock_info['current_price'],  # Mengambil harga terkini
            })
        else:
            stock_data.append({
                'symbol': stock.symbol,
                'market_cap': "Tidak tersedia",
                'high_52_week': "Tidak tersedia",
                'low_52_week': "Tidak tersedia",
                'current_price': "Tidak tersedia",
            })

    return JsonResponse(stock_data, safe=False)

