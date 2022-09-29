from django.contrib import admin
from .models import Dishes, Ingredients, KitchenTypes
# Register your models here.
admin.site.register(Dishes)
admin.site.register(Ingredients)
admin.site.register(KitchenTypes)
