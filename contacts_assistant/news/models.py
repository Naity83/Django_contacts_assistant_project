from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    published_date = models.DateField()
