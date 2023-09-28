from django.db import models

class SpendStatictic(models.Model):
    name = models.CharField(max_length=255)   
    date = models.DateField()
    spend = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    impressions = models.IntegerField(default=0)
    clicks =  models.IntegerField(default=0)
    conversions = models.IntegerField(default=0)
