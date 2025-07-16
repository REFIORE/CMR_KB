from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'orders'

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('status/<int:order_id>/', views.customer_order_status, name='order_status'),
    path('', include('orders.urls')),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
