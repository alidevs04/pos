from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('orders', views.reg_order),
    path('orders/saletoday', views.total_sales_today),
    path('orders/salethismonth', views.sales_this_month)
]