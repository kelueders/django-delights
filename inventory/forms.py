from django import forms

from .models import Ingredient, MenuItem, RecipeRequirement, Purchase

# Ingredient CRUD
class IngredientCreate(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ("name", "quantity", "unit", "unit_price")

class IngredientUpdate(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ("name", "quantity", "unit", "unit_price")

# Menu Item CRUD
class MenuItemCreate(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ('title', 'price', 'image')

class MenuItemUpdate(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ('title', 'price', 'image')