python manage.py createsuperuser:
login = Andrey
email = aras_andrey@bk.ru
password = Vfvjxrf1



AttributeError: Manager isn't available; 'auth.User' has been swapped for 'orders.CustomUser'

После регистрации, появляется ошибка
Вот ссылка на мой GitHub: https://github.com/REFIORE/CMR_KB
1. Проверь кастомную форму регистрации(orders/forms.py)
2. Обнови view регистрации (orders/views.py)
3. Обновите URL (orders/urls.py) (Если это нужно)
4. Убедитесь, что в (orders/models.py) модель определена правильно