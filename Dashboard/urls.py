from django.urls import path
from .views import DashboardView, get_stock_data

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),  # Halaman Dashboard
    path('api/stocks/', get_stock_data, name='get_stock_data'),  # Endpoint untuk data saham

]
