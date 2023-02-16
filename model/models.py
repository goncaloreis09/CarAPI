from django.db import models
from engine.models import Engine
from chassi.models import Chassi


# Create your models here.
class Model(models.Model):
    name = models.CharField(max_length=50, blank = False)
    engine = models.ForeignKey(Engine, on_delete=models.CASCADE)
    chassi = models.ForeignKey(Chassi, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    body_type = models.CharField(max_length=30, blank = False)

    def __str__(self):
        return self.chassi.line.manufacturer.name + " " + self.name + " " + self.chassi.code