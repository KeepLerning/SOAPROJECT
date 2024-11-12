from django.urls import path
from .views import AlertListView, CreateAlertView, DeleteAlertView

urlpatterns = [
    path('', AlertListView.as_view(), name='alerts'),
    path('create/', CreateAlertView.as_view(), name='create_alert'),
    path('delete/<int:pk>/', DeleteAlertView.as_view(), name='delete_alert'),
]
