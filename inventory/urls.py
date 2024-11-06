from django.urls import path

from . import views

app_name = "inventory"
urlpatterns = [
    path("", views.home, name="home"),
    path("ingredient/list", views.IngredientList.as_view(), name="ingredientlist")
]