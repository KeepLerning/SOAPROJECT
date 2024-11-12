from django.urls import path
from . import views

urlpatterns = [
    path('', views.WatchlistView.as_view(), name='watchlist'),
    path('add/<int:stock_id>/', views.add_to_watchlist, name='add_to_watchlist'),
    path('remove/<int:stock_id>/', views.remove_from_watchlist, name='remove_from_watchlist'),
    path('get_real_time_prices/', views.get_real_time_prices, name='get_real_time_prices'),  # New URL
]
