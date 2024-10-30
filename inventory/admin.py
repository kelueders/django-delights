from django.contrib import admin

from .models import MenuItem, RecipeRequirement, Ingredient, Purchase

# Register your models here.
admin.site.register(MenuItem)
admin.site.register(RecipeRequirement)
admin.site.register(Ingredient)
admin.site.register(Purchase)
