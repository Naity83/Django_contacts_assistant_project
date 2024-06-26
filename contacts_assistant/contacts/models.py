# models.py
from django.db import models
from django.core.validators import RegexValidator, EmailValidator
from datetime import date, timedelta
from django.contrib.auth.models import User
from django.db.models import Q

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
    def get_upcoming_birthdays(days, user):
        today = date.today()
        upcoming_date = today + timedelta(days=days)

        # Фильтр для контактов, у которых день рождения в текущем месяце и после текущего дня
        current_month_filter = (
            Q(birthday__month=today.month, birthday__day__gte=today.day) |
            Q(birthday__month__gt=today.month)
        )

        # Фильтр для контактов, у которых день рождения в следующем месяце и до или включительно upcoming_date
        next_month_filter = (
            Q(birthday__month=upcoming_date.month, birthday__day__lte=upcoming_date.day) |
            Q(birthday__month__lt=upcoming_date.month)
        )

        # Объединяем фильтры с учетом пользователя
        return Contact.objects.filter(
            current_month_filter & next_month_filter,
            user=user
        )


