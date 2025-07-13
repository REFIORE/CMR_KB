from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .models import Order


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'


@login_required
def order_list(request):
    if request.user.is_superuser:
        orders = Order.objects.all()
    else:
        orders = Order.objects.filter(assigned_to=request.user)
    return render(request, 'orders/order_list.html', {'orders': orders})


@login_required
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'orders/order_detail.html', {'order': order})


def customer_order_status(request, token):
    order = get_object_or_404(Order, access_token=token)
    return render(request, 'orders/customer_status.html', {'order': order})