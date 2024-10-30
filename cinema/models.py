from django.db import models


class Cinema(models.Model):
    time = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    duration = models.IntegerField()
