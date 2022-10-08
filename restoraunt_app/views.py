from django.shortcuts import render, redirect
from .models import Dishes, Ingredients, KitchenTypes
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

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

@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Dishes.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")

@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Dishes.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Dishes.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Dishes.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')

def cart_test_view(request):
    new = Dishes(name='Test',
                 weight=200,
                 kitchen=KitchenTypes.objects.get(id=1),
                 price=500.0)
    Ingredient1 = Ingredients.objects.get(id=1)
    Ingredient2 = Ingredients.objects.get(id=2)
    new.save()
    new.ingredients.add(Ingredient1, Ingredient2)
    return render(request, 'test.html')
