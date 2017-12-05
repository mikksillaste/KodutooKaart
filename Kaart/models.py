from django.db import models


# Create your models here.
class Kohad(models.Model):
    text = models.CharField(max_length=200)
    lat = models.DecimalField(decimal_places=4, max_digits=8)
    lng = models.DecimalField(decimal_places=4, max_digits=8)
