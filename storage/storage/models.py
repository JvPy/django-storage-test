from django.db import models

class RandonClass(models.Model):
    image = models.ImageField(upload_to='img')
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)