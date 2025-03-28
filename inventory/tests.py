from django.test import TestCase
from django.urls import reverse
from .models import Ingredient, MenuItem, RecipeRequirement

class IngredientListViewTest(TestCase):
    def setUp(self):
        # Create test data
        Ingredient.objects.create(name="Sugar", quantity=10, unit="kg", unit_price=5.0)
        Ingredient.objects.create(name="Salt", quantity=5, unit="kg", unit_price=2.0)

    def test_url_exists_at_desired_location(self):
        response = self.client.get('/ingredient/list/')
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self):
        response = self.client.get(reverse('inventory:ingredient-list'))
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        response = self.client.get(reverse('inventory:ingredient-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'inventory/ingredient_list.html')

    def test_displays_ingredients(self):
        response = self.client.get(reverse('inventory:ingredient-list'))
        self.assertContains(response, "Sugar")
        self.assertContains(response, "Salt")

class IngredientCreateViewTest(TestCase):
    def test_url_exists_at_desired_location(self):
        response = self.client.get('/ingredient/create/')
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self):
        response = self.client.get(reverse('inventory:ingredient-create'))
        self.assertEqual(response.status_code, 200)

    def test_creates_ingredient(self):
        data = {
            'name': 'Lettuce',
            'quantity': 10,
            'unit': 'kg',
            'unit_price': 5.32
        }
        response = self.client.post(reverse('inventory:ingredient-create'), data)
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertTrue(Ingredient.objects.filter(name='Lettuce').exists())

class RecipeRequirementListVewTest(TestCase):
    def setUp(self):
        sugar = Ingredient.objects.create(name="Sugar", quantity=10, unit="kg", unit_price=5.0)
        salt = Ingredient.objects.create(name="Salt", quantity=5, unit="kg", unit_price=2.0)
        butter = Ingredient.objects.create(name="Butter", quantity=12, unit="C", unit_price=2.0)
        cookie = MenuItem.objects.create(title="Cookie", price=1.25, image="https://beyondfrosting.com/wp-content/uploads/2019/03/Chewy-Chocolate-Chip-Cookies-139-2.jpg")
        RecipeRequirement.objects.create(menu_item=cookie, ingredient=sugar, quantity=2)
        RecipeRequirement.objects.create(menu_item=cookie, ingredient=salt, quantity=0.03)
        RecipeRequirement.objects.create(menu_item=cookie, ingredient=butter, quantity=1)
        milk = Ingredient.objects.create(name="Milk", quantity=10, unit="gal", unit_price=3.00)
        oats = Ingredient.objects.create(name="Oats", quantity=50, unit="g", unit_price=0.50)
        oatmeal = MenuItem.objects.create(title="Oatmeal", price=5.00, image="https://djangodelights.com/fillerimage.jpg")
        RecipeRequirement.objects.create(menu_item=oatmeal, ingredient=milk, quantity=0.1)
        RecipeRequirement.objects.create(menu_item=oatmeal, ingredient=oats, quantity=4)


    def test_url_exists_at_desired_location(self):
        response = self.client.get('/recipereq/list/')
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self):
        response = self.client.get(reverse('inventory:recipereq-list'))
        self.assertEqual(response.status_code, 200)
