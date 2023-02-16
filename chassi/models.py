from django.db import models
from line.models import Line
from django.utils import timezone
from body.models import Body

# Create your models here.
class Chassi(models.Model):
    code = models.CharField(max_length=15, null = False, blank = False)
    line = models.ForeignKey(Line, on_delete=models.CASCADE)
    year_created = models.IntegerField(null = False, blank = False)
    year_end_of_production = models.IntegerField()
    updated_at = models.DateTimeField(auto_now = True)
    bodies_available = models.ManyToManyField(Body)

    def __str__(self):
        return self.line.name + " " + self.code
