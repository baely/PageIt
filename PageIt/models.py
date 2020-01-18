from django.db import models


class Page(models.Model):
    id = models.CharField(max_length=8, primary_key=True)
    data = models.CharField(max_length=65536)
