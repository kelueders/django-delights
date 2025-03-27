from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=30)
    unit_price = models.FloatField(default=0)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    title = models.CharField(max_length=30)
    price = models.FloatField(default=0)
    image = models.URLField(null=True)

    def __str__(self):
        return self.title

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)

    def __str__(self):
        return f"{self.ingredient} required for the menu item {self.menu_item}"

class Purchase(models.Model):
    timestamp = models.DateTimeField(auto_now_add=False)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.menu_item} from {self.timestamp}"
