from django.db import models
from django.core.exceptions import ValidationError
from cloudinary_storage.storage import RawMediaCloudinaryStorage



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
    image = models.ImageField(upload_to='my_files/', validators=[validate_file_size])
    raw_file = models.ImageField(upload_to='raw/', blank=True, storage=RawMediaCloudinaryStorage())
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
