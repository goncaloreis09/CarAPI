from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    acronym = models.CharField(max_length=2, null=False, blank=False, unique=True)

    def __str__(self):
        return self.name + " | " + self.acronym