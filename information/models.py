from django.db import models

# Create your models here.


class Divisions(models.Model):
    name = models.CharField(max_length=60)
    population = models.IntegerField()
    area = models.IntegerField()

    def __str__(self):
        return self.name


class Districts(models.Model):
    name = models.CharField(max_length=60)
    population_density = models.IntegerField(blank=True, null=True)
    education_rate = models.IntegerField()
    visited = models.BooleanField(default=False)
    division = models.ForeignKey(Divisions, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
