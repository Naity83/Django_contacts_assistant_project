# models.py
from django.db import models
from django.core.validators import RegexValidator, EmailValidator
from datetime import date, timedelta
from django.contrib.auth.models import User

class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(
        max_length=15,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")]
    )
    email = models.EmailField(validators=[EmailValidator(message="Enter a valid email address.")])
    birthday = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.full_name}"

    @staticmethod
    def get_upcoming_birthdays(days):
        today = date.today()
        upcoming_date = today + timedelta(days=days)
        # Фильтр для получения контактов, у которых день рождения в диапазоне от сегодняшнего дня до заданного числа дней
        return Contact.objects.filter(
            birthday__month__gte=today.month,
            birthday__month__lte=upcoming_date.month,
            birthday__day__gte=today.day,
            birthday__day__lte=upcoming_date.day
        )

