from django.db import models
from django.contrib.auth.models import User  # Mengimpor model User bawaan Django
from Stock_Data.models import Stock  # Mengimpor model Stock dari Stocks App

class UserWatchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='watchlist')  # Referensi ke pengguna
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='watchlisted_by')  # Referensi ke saham yang dipantau
    added_on = models.DateTimeField(auto_now_add=True)  # Tanggal saham ditambahkan ke watchlist

    class Meta:
        unique_together = ('user', 'stock')  # Kombinasi unik, satu saham hanya bisa dipantau sekali per pengguna
        ordering = ['-added_on']  # Urutkan berdasarkan tanggal ditambahkan, terbaru terlebih dahulu

    def __str__(self):
        return f"{self.user.username} - {self.stock.symbol}"
