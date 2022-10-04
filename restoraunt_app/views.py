from django.shortcuts import render
from .models import Dishes, Ingredients, KitchenTypes
from django.db.models import Q

# Create your views here.

def MenuView(request):
    context = {
        'dishes': Dishes.objects.all(),
        'ingredients': Ingredients.objects.all(),
        'kitchens': KitchenTypes.objects.all()
    }
    return render(request, 'home.html', context=context)

def DishByIngredient(request, ingredientId):
    queryset = Dishes.objects.filter(Q(ingredient1=ingredientId) |
                                     Q(ingredient2=ingredientId) |
                                     Q(ingredient3=ingredientId))
    return render(request, 'dishByIngredient.html', {'dishesByIngredient': queryset})

def DishByWeight(request):
    searchWeight = float(request.GET.get('WeightSearch'))
    queryset = 'Hello'
    return render(request, 'dishByWeight.html', {'dishByWeight': queryset})

