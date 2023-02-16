from django.db import models
from country.models import Country
from group.models import Group

# Create your models here.

class Brand(models.Model):
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=255, null=True, blank=True, unique=True)
    year_founded = models.CharField(max_length=4, null=False, blank=False)
    country_founded = models.ForeignKey(Country, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)


    def __str__(self):
        return self.name