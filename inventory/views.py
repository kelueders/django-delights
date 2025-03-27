from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from .forms import IngredientCreate, IngredientUpdate

# Create your views here.
def home(request):
    return render(request, "inventory/home.html")

# INGREDIENT VIEWS
class IngredientList(ListView):
    model = Ingredient

class IngredientCreate(CreateView):
    model = Ingredient
    template_name = "inventory/ingredient_create_form.html"
    form_class = IngredientCreate
    success_url = reverse_lazy('inventory:ingredient-list')  # Redirect to the ingredient list page

class IngredientUpdate(UpdateView):
    model = Ingredient
    template_name = "inventory/ingredient_update_form.html"
    form_class = IngredientUpdate
    # fields = ["name", "quantity", "unit", "unit_price"]
    success_url = reverse_lazy('inventory:ingredient-list')

class IngredientDelete(DeleteView):
    model = Ingredient
    template_name = "inventory/ingredient_delete_form.html"
    success_url = reverse_lazy('inventory:ingredient-list')

# MENU ITEM VIEWS
class MenuItemList(ListView):
    model = MenuItem

# PURCHASE VIEWS
class PurchaseList(ListView):
    model = Purchase