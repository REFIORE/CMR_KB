from django.contrib import admin
from .models import Customer, Order
from django.contrib.auth.admin import UserAdmin
from .models import Profile
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('title', 'customer', 'status', 'assigned_to', 'created_at')
    list_filter = ('status', 'assigned_to')
    search_fields = ('title', 'customer__name')


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Дополнительно', {'fields': ('phone', 'is_customer', 'is_employee')}),
    )


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)
