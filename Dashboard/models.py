from django.db import models
from Stock_Data.models import Stock  # Mengimpor model Stock dari Stocks App

class Indicator(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='indicators')  # Referensi ke model Stock
    date = models.DateField()  # Tanggal perhitungan indikator
    sma_50 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Simple Moving Average 50 hari
    sma_200 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Simple Moving Average 200 hari
    rsi = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Relative Strength Index
    macd = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)  # Moving Average Convergence Divergence
    signal = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)  # MACD signal line

    class Meta:
        unique_together = ('stock', 'date')  # Kombinasi unik untuk setiap saham pada tanggal tertentu
        ordering = ['-date']  # Urutkan berdasarkan tanggal, terbaru terlebih dahulu

    def __str__(self):
        return f"{self.stock.symbol} - Indicators on {self.date}"
