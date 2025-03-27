from django.urls import path

from . import views

app_name = "inventory"
urlpatterns = [
    path("", views.home, name="home"),
    path("ingredient/list", views.IngredientList.as_view(), name="ingredient-list"),
    path("ingredient/create", views.IngredientCreate.as_view(), name="ingredient-create"),
    path("ingredient/update/<pk>", views.IngredientUpdate.as_view(), name="ingredient-update"),
    path("ingredient/delete/<pk>", views.IngredientDelete.as_view(), name="ingredient-delete"),
    path("menuitem/list", views.MenuItemList.as_view(), name="menuitem-list"),
    path("menuitem/create", views.MenuItemCreate.as_view(), name="menuitem-create"),
    path("menuitem/update/<pk>", views.MenuItemUpdate.as_view(), name="menuitem-update"),
    path("menuitem/delete/<pk>", views.MenuItemDelete.as_view(), name="menuitem-delete"),
    path("purchase/list", views.PurchaseList.as_view(), name="purchase-list"),
    path("purchase/create", views.PurchaseCreate.as_view(), name="purchase-create"),
    path("purchase/update/<pk>", views.PurchaseUpdate.as_view(), name="purchase-update"),
    path("purchase/delete/<pk>", views.PurchaseDelete.as_view(), name="purchase-delete")
]