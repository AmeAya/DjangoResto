from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Dishes(models.Model):
    name = models.CharField(max_length=50)
    weight = models.FloatField(max_length=20)
    ingredients = models.ManyToManyField('Ingredients')
    kitchen = models.ForeignKey('KitchenTypes', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Ingredients(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class KitchenTypes(models.Model):
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.country
