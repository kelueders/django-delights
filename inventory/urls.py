from django.urls import path

from . import views

app_name = "inventory"
urlpatterns = [
    path("ingredient/list", views.IngredientList.as_view(), name="ingredientlist")
]