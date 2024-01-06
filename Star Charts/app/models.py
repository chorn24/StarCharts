from django.db import models
from django.contrib.auth.models import User

# Create your models here.


STARS = (
    ("Yellow Dwarf Star","Yellow Dwarf Star"),
    ("Red Dwarf Star","Red Dwarf Star"),
    ("White Dwarf Star","White Dwarf Star"),
    ("Brown Dwarf Star","Brown Dwarf Star"),
    ("Red Giant Star","Red Giant Star"),
    ("Blue Giant Star","Blue Giant Star"),
    ("Red Supergiant Star","Red Supergiant Star"),
)

class SystemChart(models.Model):
    name = models.CharField(max_length=50)
    planet_amount = models.IntegerField()
    star_name = models.CharField(max_length=50, null=True)
    star_type = models.CharField(max_length=50, choices=STARS, null=True)
    documented_by = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


RATING = (
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
    (6,6),
    (7,7),
    (8,8),
    (9,9),
    (10,10)
)


class PlanetChart(models.Model):
    name = models.CharField(max_length=50)
    habitat_rating = models.IntegerField(choices=RATING, null=True, default=5)
    description = models.TextField(null=True)
    system = models.ForeignKey(SystemChart, on_delete=models.CASCADE, null=True)
    documented_by = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name
