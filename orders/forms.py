from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from orders.models import CustomUser


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'email', 'phone']


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'avatar']
