from django.db import models

class Stock(models.Model):
    symbol = models.CharField(max_length=10, unique=True)  # Contoh: AAPL, GOOGL
    company_name = models.CharField(max_length=255)  # Nama perusahaan
    sector = models.CharField(max_length=100, blank=True, null=True)  # Sektor industri
    current_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Harga saat ini
    market_cap = models.BigIntegerField(null=True, blank=True)  # Kapitalisasi pasar
    high_52_week = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Harga tertinggi dalam 52 minggu
    low_52_week = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Harga terendah dalam 52 minggu
    created_at = models.DateTimeField(auto_now_add=True)  # Waktu dibuat
    updated_at = models.DateTimeField(auto_now=True)  # Waktu terakhir diperbarui

    def __str__(self):
        return f"{self.symbol} - {self.company_name}"


class StockPriceHistory(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='price_history')  # Relasi ke Stock
    date = models.DateField()  # Tanggal harga saham
    open_price = models.DecimalField(max_digits=10, decimal_places=2)  # Harga pembukaan
    close_price = models.DecimalField(max_digits=10, decimal_places=2)  # Harga penutupan
    high = models.DecimalField(max_digits=10, decimal_places=2)  # Harga tertinggi hari itu
    low = models.DecimalField(max_digits=10, decimal_places=2)  # Harga terendah hari itu
    volume = models.BigIntegerField()  # Volume perdagangan saham

    class Meta:
        unique_together = ('stock', 'date')  # Kombinasi unik, tiap tanggal untuk setiap saham
        ordering = ['-date']  # Urutkan berdasarkan tanggal, terbaru terlebih dahulu

    def __str__(self):
        return f"{self.stock.symbol} - {self.date}"
