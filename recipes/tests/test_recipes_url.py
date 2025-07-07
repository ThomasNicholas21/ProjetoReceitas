from django.test import TestCase
from django.urls import reverse


class RecipeURLsTest(TestCase):
    def test_recipes_home_url_is_correct(self):
        home_url = reverse('recipes:home')
        self.assertEqual(home_url, '/')

    def test_recipes_detail_url_is_correct(self):
        recipe_url = reverse(
            'recipes:recipe',
            kwargs={
                'id_recipe': 1
            }
            )
        self.assertEqual(recipe_url, '/recipes/1/')

    def test_recipes_category_url_is_correct(self):
        category_url = reverse(
            'recipes:category',
            kwargs={
                'id_category': 1
                }
            )
        self.assertEqual(category_url, '/recipes/category/1/')
