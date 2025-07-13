from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('status/<int:order_id>/', views.customer_order_status, name='customer_order_status'),
]
