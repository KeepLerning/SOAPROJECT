from django.db import models
from Stock_Data.models import Stock  # Mengimpor model Stock dari Stocks App

class News(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='news')  # Referensi ke saham terkait
    title = models.CharField(max_length=255)  # Judul berita
    content = models.TextField()  # Isi berita
    source = models.CharField(max_length=255)  # Sumber berita (misalnya, nama situs web atau publikasi)
    url = models.URLField()  # URL ke berita asli
    published_at = models.DateTimeField()  # Tanggal dan waktu berita diterbitkan
    sentiment_score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Skor sentimen (opsional)
    created_at = models.DateTimeField(auto_now_add=True)  # Waktu berita ditambahkan ke database

    class Meta:
        ordering = ['-published_at']  # Urutkan berdasarkan tanggal publikasi, terbaru terlebih dahulu

    def __str__(self):
        return f"{self.stock.symbol} News - {self.title}"

