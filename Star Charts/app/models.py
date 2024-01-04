from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class SystemChart(models.Model):
    name = models.TextField()
    planet_amount = models.IntegerField()
    documented_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class PlanetChart(models.Model):
    name = models.TextField()
    habitat_rating = models.IntegerField(null=True)
    description = models.TextField(null=True)
    system = models.ForeignKey(SystemChart, on_delete=models.CASCADE)
    documented_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
