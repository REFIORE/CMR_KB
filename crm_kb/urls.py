from django.contrib import admin
from django.urls import path, include
from orders.views import CustomLoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('orders/', include('orders.urls', namespace='orders')),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
]
