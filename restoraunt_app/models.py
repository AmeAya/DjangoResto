from django.db import models

# Create your models here.

class Dishes(models.Model):
    name = models.CharField(max_length=50)
    weight = models.FloatField(max_length=20)
    ingredient1 = models.ForeignKey('ingredients', on_delete=models.CASCADE, related_name='ingr1')
    ingredient2 = models.ForeignKey('ingredients', on_delete=models.CASCADE, related_name='ingr2')
    ingredient3 = models.ForeignKey('ingredients', on_delete=models.CASCADE, related_name='ingr3')
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
