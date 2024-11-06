from django.shortcuts import render
from django.views.generic import ListView

from .models import Ingredient, MenuItem, RecipeRequirement, Purchase

# Create your views here.
def home(request):
    return render(request, "inventory/home.html")

class IngredientList(ListView):
    model = Ingredient