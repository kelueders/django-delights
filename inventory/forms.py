from django import forms

from .models import Ingredient, MenuItem, RecipeRequirement, Purchase

# INGREDIENT CRUD
class IngredientCreate(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ("name", "quantity", "unit", "unit_price")

class IngredientUpdate(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ("name", "quantity", "unit", "unit_price")