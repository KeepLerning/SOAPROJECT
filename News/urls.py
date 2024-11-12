from django.urls import path
from .views import NewsListView, NewsDetailView

urlpatterns = [
    path('', NewsListView.as_view(), name='news'),  # Daftar berita
    path('<int:pk>/', NewsDetailView.as_view(), name='news_detail'),  # Detail berita berdasarkan ID
]
