from django.urls import path
from . import views
from .views import StockDetailView, get_stock_data,get_stock_history

urlpatterns = [
    path('', views.StockListView.as_view(), name='stocks'),  # Daftar saham
    path('<int:pk>/', views.StockDetailView.as_view(), name='stock_detail'),  # Detail saham berdasarkan ID
    path('api/stocks/<int:stock_id>/', get_stock_data, name='get_stock_data'),  # API untuk mendapatkan data saham
    path('get_stock_history/<int:stock_id>/', views.get_stock_history, name='get_stock_history'),
]
