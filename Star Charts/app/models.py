from django.db import models

# Create your models here.


class Explorer(models.Model):
    name = models.TextField(default="NameE")
    password  = models.CharField(max_length=50)
    password_repeat = models.CharField(max_length=50, null=True)



    def __str__(self):
        return self.name


class Documenter(models.Model):
    name = models.CharField(max_length=50)
    password  = models.CharField(max_length=50)
    password_repeat = models.CharField(max_length=50, null=True)
    document_id = models.IntegerField(default="No")

    def __str__(self):
        return self.name


class SystemChart(models.Model):
    name = models.TextField()
    planet_amount = models.IntegerField()
    documented_by = models.ForeignKey(Documenter, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class PlanetChart(models.Model):
    name = models.TextField()
    habitat_rating = models.IntegerField(null=True)
    description = models.TextField(null=True)
    system = models.ForeignKey(SystemChart, on_delete=models.CASCADE)
    documented_by = models.ForeignKey(Documenter, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
