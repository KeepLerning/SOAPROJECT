from django.contrib import admin
from .models import Stock, StockPriceHistory

admin.site.register(Stock)
admin.site.register(StockPriceHistory)
