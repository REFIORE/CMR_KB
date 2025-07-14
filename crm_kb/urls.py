from django.contrib import admin
from django.urls import path, include
from orders.views import CustomLoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('orders.urls')),
    path('orders/', include('orders.urls')),
]
