from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('status/<int:order_id>/', views.customer_order_status, name='order_status'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='user_profile'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
