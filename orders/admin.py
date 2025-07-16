from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Customer, Order


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
        ('Дополнительные данные', {'fields': ('phone',)}),
    )


admin.site.register(CustomUser, UserAdmin)
admin.site.register(Customer)
admin.site.register(Order)
