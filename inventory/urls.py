from django.urls import path

from . import views

app_name = "inventory"
urlpatterns = [
    path("", views.home, name="home"),
    path("ingredient/list", views.IngredientList.as_view(), name="ingredient-list"),
    path("ingredient/delete/<pk>", views.IngredientDelete.as_view(), name="ingredient-delete"),
    path("menuitem/list", views.MenuItemList.as_view(), name="menuitem-list"),
    path("purchase/list", views.PurchaseList.as_view(), name="purchase-list")
]