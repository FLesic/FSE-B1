from django.urls import path
from . import cashier_views

urlpatterns = [
    path('unfreeze/', cashier_views.cashier_unfreeze, name = 'all-cashier_unfreeze'),
    path('freeze/', cashier_views.cashier_freeze, name = 'cashier_freeze'),
    path('reportloss/', cashier_views.cashier_reportloss, name = 'cashier_reportloss'),
    path('reissue/', cashier_views.cashier_reissue, name = 'cashier_reissue'),
]