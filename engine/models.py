from django.db import models
from brand.models import Brand

# Create your models here.

class Engine(models.Model):

    FUEL_CHOICES = [
        ("G", "Gas"),
        ("D", "Diesel"),
        ("E", "Eletric"),
        ("H", "Hybrid")
    ]

    manufacter = models.ForeignKey(Brand, on_delete=models.CASCADE)
    engine_code = models.CharField(max_length=20, null = False, blank=False)
    fuel = models.CharField(max_length=1, choices=FUEL_CHOICES, null = False, blank = False)
    year_created = models.IntegerField(null = False, blank = False)

    def __str__(self):
        return self.engine_code + " (" + self.manufacter + ")"
