from django.db import models
from django.core.exceptions import ValidationError


def validate_file_size(value):
    filesize = value.size

    if filesize > 1_000_000:
        raise ValidationError('Максимальний розмір файлу 1Мб')
    return value


# Create your models here.
# class MyFile(models.Model):
#     description = models.CharField(max_length=300)
#     path = models.FileField(upload_to='myfiles', validators=[validate_file_size])
#     added_at = models.DateTimeField(auto_now_add=True)


# models.py

# from django.db import models

class MyFile(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='files/', validators=[validate_file_size])
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
