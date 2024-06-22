from django.db import models
from django.core.exceptions import ValidationError


def validate_file_size(value):
    filesize = value.size

    if filesize > 1_000_000:
        raise ValidationError('Максимальний розмір файлу 1Мб')
    return value


# Create your models here.
class MyFile(models.Model):
    description = models.CharField(max_length=300)
    path = models.FileField(upload_to='myfiles', validators=[validate_file_size])
    added_at = models.DateTimeField(auto_now_add=True)
