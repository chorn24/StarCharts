from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class SystemChart(models.Model):
    name = models.TextField()
    planet_amount = models.IntegerField()
    documented_by = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


RATING = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}


class PlanetChart(models.Model):
    name = models.CharField(max_length=50)
    habitat_rating = models.IntegerField(choices=RATING, null=True)
    description = models.CharField(null=True, max_length=50)
    system = models.ForeignKey(SystemChart, on_delete=models.CASCADE, null=True)
    documented_by = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name
