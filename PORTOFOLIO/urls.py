
# project_root/urls.py
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import login_view,logout_view, register_view



urlpatterns = [
    # path('grappelli/', include('grappelli.urls')), 
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('accounts/', include("allauth.urls")),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('stocks/', include('Stock_Data.urls')),
    path('dashboard/', include('Dashboard.urls')), 
    path('watchlist/', include('Watchlist.urls')),
    path('alerts/', include('Alerts.urls')),
    path('news/', include('News.urls')),
    path('', views.HomePageView.as_view(), name='home'),  # Halaman utama
]
