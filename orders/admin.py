from django.contrib import admin
from .models import Customer, Order


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('title', 'customer', 'status', 'assigned_to', 'created_at')
    list_filter = ('status', 'assigned_to')
    search_fields = ('title', 'customer__name')


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
