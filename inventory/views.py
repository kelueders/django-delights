from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import DeleteView

from .models import Ingredient, MenuItem, RecipeRequirement, Purchase

# Create your views here.
def home(request):
    return render(request, "inventory/home.html")

class IngredientList(ListView):
    model = Ingredient

class IngredientDelete(DeleteView):
    model = Ingredient
    success_url = "/ingredient/list"

class MenuItemList(ListView):
    model = MenuItem

class PurchaseList(ListView):
    model = Purchase