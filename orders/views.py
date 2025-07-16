from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model, login
from .models import Order
from .forms import ProfileForm
from django.contrib.auth.forms import UserCreationForm


User = get_user_model()


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


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('orders:order_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'registration/profile.html', {'form': form})
