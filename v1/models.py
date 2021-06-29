from django.db import models

# Create your models here.
from django.db import models


class Article(models.Model):
    site = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    date = models.DateField(blank=True, null=True)
    case = models.CharField(blank=True, null=True, max_length=255)
    content = models.TextField()
