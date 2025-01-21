from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from .models import Stock, StockPriceHistory
from .utils import get_stock_data 
from django.shortcuts import render

class StockListView(ListView):
    model = Stock
    template_name = 'stocks.html'
    context_object_name = 'stocks'

    def get_queryset(self):
        return Stock.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        stocks_info = []
        for stock in context['stocks']:
            stock_info = get_stock_data(stock.symbol, stock.id)  
            if stock_info:
                stock.current_price = stock_info['current_price']
                stock.market_cap = stock_info['market_cap']
                stock.high_52_week = stock_info['high_52_week']
                stock.low_52_week = stock_info['low_52_week']
                stock.change_1d = stock_info.get('change_1d', None)
                stock.change_1w = stock_info.get('change_1w', None)
                stock.change_1m = stock_info.get('change_1m', None)
                stock.change_1y = stock_info.get('change_1y', None)
                stocks_info.append(stock)
        
        context['stocks_info'] = stocks_info
        return context


class StockDetailView(DetailView):
    model = Stock
    template_name = 'stock_detail.html'
    context_object_name = 'stock'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['price_history'] = StockPriceHistory.objects.filter(stock=self.object)

        stock_info = get_stock_data(self.object.symbol, self.object.id)
        if stock_info:
            context['current_price'] = stock_info['current_price']
            context['market_cap'] = stock_info['market_cap']
            context['high_52_week'] = stock_info['high_52_week']
            context['low_52_week'] = stock_info['low_52_week']


            context['change_1d'] = stock_info.get('change_1d', None)
            context['change_1w'] = stock_info.get('change_1w', None)
            context['change_1m'] = stock_info.get('change_1m', None)
            context['change_1y'] = stock_info.get('change_1y', None)

        return context

def get_stock_data_view(request, stock_id):
    try:
        stock = get_object_or_404(Stock, id=stock_id)  
        stock_info = get_stock_data(stock.symbol, stock_id)  
        
        if stock_info:
            return JsonResponse({
                'symbol': stock.symbol,
                'current_price': stock_info.get('current_price', 'Not available'),
                'market_cap': stock_info.get('market_cap', 'Not available'),
                'high_52_week': stock_info.get('high_52_week', 'Not available'),
                'low_52_week': stock_info.get('low_52_week', 'Not available'),
                'change_1d': stock_info.get('change_1d', 'Not available'),
                'change_1w': stock_info.get('change_1w', 'Not available'),
                'change_1m': stock_info.get('change_1m', 'Not available'),
                'change_1y': stock_info.get('change_1y', 'Not available'),
            })
        else:
            return JsonResponse({'error': 'Data not available'}, status=404)
    except Stock.DoesNotExist:
        return JsonResponse({'error': 'Stock not found'}, status=404)

def get_stock_history(request, stock_id):
    try:
        stock = get_object_or_404(Stock, id=stock_id) 
        price_history = stock.price_history.all()  
        data = [
            {
                'date': history.date.strftime('%Y-%m-%d'),  
                'price': history.price
            }
            for history in price_history
        ]
        return JsonResponse({'price_history': data})
    except Stock.DoesNotExist:
        return JsonResponse({'error': 'Stock not found'}, status=404)

