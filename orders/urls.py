from django.urls import path
from .views import register, profile
from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
]
