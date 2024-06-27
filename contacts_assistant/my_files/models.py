from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError
from cloudinary.models import CloudinaryField

def validate_file_size(value):
    filesize = value.size
    if filesize > 50_000_000:  # Увеличен максимальный размер для видео
        raise ValidationError('Максимальный размер файла 50Мб')
    return value

class Picture(models.Model):
    description = models.CharField(max_length=300)
    path = CloudinaryField('image', validators=[validate_file_size])
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default=None)

class Video(models.Model):
    description = models.CharField(max_length=300)
    path = CloudinaryField('video', validators=[validate_file_size])
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default=None)

class Document(models.Model):
    description = models.CharField(max_length=300)
    path = CloudinaryField('raw', validators=[validate_file_size])
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default=None)
