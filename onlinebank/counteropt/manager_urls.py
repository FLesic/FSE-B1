from django.urls import path
from . import views

urlpatterns = [
    path('all-cashier/', views.all_cashiers, name = 'all-cashiers'),
    path('add/', views.add_cashier, name = 'add_cashier'),
]