from django.shortcuts import render
from django.views.generic import ListView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from .forms import IngredientCreate, IngredientUpdate, MenuItemCreate, MenuItemUpdate, PurchaseCreate, PurchaseUpdate

# Create your views here.
def home(request):
    return render(request, "inventory/home.html")

'''
INGREDIENT VIEWS
'''
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
    success_url = reverse_lazy('inventory:ingredient-list')

class IngredientDelete(DeleteView):
    model = Ingredient
    template_name = "inventory/ingredient_delete_form.html"
    success_url = reverse_lazy('inventory:ingredient-list')

'''
MENU ITEM VIEWS
'''
class MenuItemList(ListView):
    model = MenuItem

class MenuItemCreate(CreateView):
    model = MenuItem
    template_name = "inventory/menuitem_create_form.html"
    form_class = MenuItemCreate
    success_url = reverse_lazy('inventory:menuitem-list')

class MenuItemUpdate(UpdateView):
    model = MenuItem
    template_name = "inventory/menuitem_update_form.html"
    form_class = MenuItemUpdate
    success_url = reverse_lazy('inventory:menuitem-list')

class MenuItemDelete(DeleteView):
    model = MenuItem
    template_name = "inventory/ingredient_delete_form.html"
    success_url = reverse_lazy('inventory:ingredient-list')

'''
PURCHASE VIEWS
'''
class PurchaseList(ListView):
    model = Purchase

class PurchaseCreate(CreateView):
    model = Purchase
    template_name = "inventory/purchase_create_form.html"
    form_class = PurchaseCreate
    success_url = reverse_lazy('inventory:purchase-list')

class PurchaseUpdate(UpdateView):
    model = Purchase
    template_name = "inventory/purchase_update_form.html"
    form_class = PurchaseUpdate
    success_url = reverse_lazy('inventory:purchase-list')

class PurchaseDelete(DeleteView):
    model = Purchase
    template_name = "inventory/purchase_delete_form.html"
    success_url = reverse_lazy('inventory:purchase-list')

'''
RECIPE REQUIREMENT VIEWS
'''
class RecipeRequirementList(View):
    def get(self, request):
        menu_items = MenuItem.objects.all()
        print(menu_items)
        full_menu_ingredient_list = []
        for menu_item in menu_items:
            required_ingredients = RecipeRequirement.objects.filter(menu_item=menu_item)
            full_menu_ingredient_list.append({
                'menu_item': menu_item,
                'ingredients': required_ingredients
            })
        print(full_menu_ingredient_list)
        return render(request, 'inventory/recipereq_list.html', {'full_menu_ingredient_list': full_menu_ingredient_list})
    
'''
OTHER VIEWS
'''
class FinancialReport(View):
    def get_revenue(self):
        pass

    def get_cost(self):
        pass

    def get_profit(self):
        pass