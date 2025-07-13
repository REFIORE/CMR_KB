from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    email = models.EmailField(unique=True, verbose_name="Email")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Телефон")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class Order(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новый'),
        ('in_progress', 'В работе'),
        ('done', 'Выполнен'),
        ('issued', 'Выдан'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="Клиент")
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='new',
        verbose_name="Статус"
    )
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Исполнитель"
    )

    def __str__(self):
        return f"{self.title} ({self.get_status_display()})"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ['-created_at']