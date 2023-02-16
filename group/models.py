from django.db import models

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False, unique=True)
    year_created = models.IntegerField(blank= False, null=False)

    def __str__(self):
        return self.name