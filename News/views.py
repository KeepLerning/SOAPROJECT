from django.views.generic import ListView, DetailView
from .models import News
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



@method_decorator(login_required, name='dispatch')  # Terapkan login_required
# Daftar berita saham
class NewsListView(ListView):
    model = News
    template_name = 'news.html'
    context_object_name = 'news_list'

# Detail berita tertentu berdasarkan ID
class NewsDetailView(DetailView):
    model = News
    template_name = 'detail_news.html'
    context_object_name = 'news'
