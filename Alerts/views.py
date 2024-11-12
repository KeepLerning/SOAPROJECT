from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Alert
from django.contrib.auth.mixins import LoginRequiredMixin

# Daftar alert pengguna
class AlertListView(LoginRequiredMixin, ListView):
    model = Alert
    template_name = 'alerts.html'
    context_object_name = 'alerts'

    def get_queryset(self):
        return Alert.objects.filter(user=self.request.user)

# Membuat alert baru
class CreateAlertView(LoginRequiredMixin, CreateView):
    model = Alert
    fields = ['stock', 'price_target', 'alert_type']
    template_name = 'create_alert.html'
    success_url = reverse_lazy('alerts')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# Menghapus alert
class DeleteAlertView(LoginRequiredMixin, DeleteView):
    model = Alert
    template_name = 'delete_alert.html'
    success_url = reverse_lazy('alerts')
