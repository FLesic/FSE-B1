from django.urls import path
from . import views

urlpatterns = [
    path('all-cashier/', views.all_cashiers, name = 'all-cashiers'),
    path('add/', views.add_cashier, name = 'add_cashier'),
    path('delete/', views.delete_cashier, name = 'delete_cashier'),
    path('modify-base/', views.modify_cashier, name = 'modify_cashier'),
    path('modify-authority/', views.modify_authority, name = 'modify_authority')
]