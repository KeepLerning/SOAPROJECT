from django.db import models
from django.contrib.auth.models import User
from Stock_Data.models import Stock  # Pastikan ini benar, sesuai dengan app stock Anda

class Alert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Pengguna yang membuat alert
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)  # Saham yang diikuti
    price_target = models.DecimalField(max_digits=10, decimal_places=2)  # Target harga
    alert_type = models.CharField(max_length=20, choices=[('above', 'Above'), ('below', 'Below')])  # Tipe alert: di atas atau di bawah

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.stock.symbol} - {self.alert_type} {self.price_target}"
