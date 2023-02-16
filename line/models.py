from django.db import models
from brand.models import Brand

# Create your models here.

class Line(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    manufacturer = models.ForeignKey(Brand, on_delete=models.CASCADE)


    def __str__(self):
        return self.name