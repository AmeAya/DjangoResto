from django.urls import path
from .views import MenuView, DishByIngredient, DishByWeight

urlpatterns = [
    path('', MenuView, name='home'),
    path('dishByIngredient/<int:ingredientId>/', DishByIngredient, name='dishByIngredient'),
    path('dishByWeight/', DishByWeight, name='dishByWeight'),
]
