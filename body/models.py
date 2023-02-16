from django.db import models

# Create your models here.
class Body(models.Model):
    name = models.CharField(max_length=50, blank=False, unique = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
