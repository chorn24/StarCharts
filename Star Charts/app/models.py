from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class SystemChart(models.Model):
    name = models.TextField()
    planet_amount = models.IntegerField()
    documented_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


RATING = (
    (10,10),
    (9,9),
    (8,8),
    (7,7),
    (6,6),
    (5,5),
    (4,4),
    (3,3),
    (2,2),
    (1,1),

)
class PlanetChart(models.Model):
    name = models.CharField(max_length=50)
    habitat_rating = models.CharField(max_length=10,choices=RATING,default=5, null=True)
    description = models.CharField(null=True,max_length=50)
    system = models.ForeignKey(SystemChart, on_delete=models.CASCADE, null=True)
    documented_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
