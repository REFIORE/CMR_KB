from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order


@login_required
def order_list(request):
    if request.user.is_superuser:
        orders = Order.objects.all().order_by('-created_at')
    else:
        orders = Order.objects.filter(assigned_to=request.user).order_by('-created_at')
    return render(request, 'orders/order_list.html', {'orders': orders})


def customer_order_status(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/customer_order_status.html', {'order': order})


def home_page(request):
    return render(request, 'orders/home.html')


def current_host(request):
    from django.http import HttpResponse
    return HttpResponse(f"Текущий хост: {request.get_host()}")
