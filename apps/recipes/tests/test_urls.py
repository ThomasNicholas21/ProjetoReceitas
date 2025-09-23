from django.test import TestCase, override_settings
from django.urls import reverse


class RecipeAppURLsTest(TestCase):
    def test_recipes_home_url_is_correct(self):
        """Test if home url is correct"""
        home_url = reverse('recipes:home')
        self.assertEqual(home_url, '/')

    def test_recipes_detail_url_is_correct(self):
        """Test if detail url is correct"""
        recipe_url = reverse(
            'recipes:recipe',
            kwargs={
                'id_recipe': 1
            }
            )
        self.assertEqual(recipe_url, '/recipes/1/')

    def test_recipes_category_url_is_correct(self):
        """Test if category url is correct"""
        category_url = reverse(
            'recipes:category',
            kwargs={
                'id_category': 1
                }
            )
        self.assertEqual(category_url, '/recipes/category/1/')

    def test_recipes_search_url_is_correct(self):
        """Test if search url is correct"""
        search_url = reverse('recipes:search')
        self.assertEqual(search_url, '/recipes/search/')


class ProjectURLsTest(TestCase):
    @override_settings(DEBUG=False)
    def test_urls_debug_false_import(self):
        """Test DEBUG false to static and media url"""
        import importlib
        import project.urls
        importlib.reload(project.urls)
