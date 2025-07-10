from django.test import TestCase, override_settings
from django.urls import reverse, get_resolver


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


class ProjectURLsTest(TestCase):
    @override_settings(DEBUG=True)
    def test_static_and_media_urls(self):
        resolver = get_resolver()

        static_match = resolver.resolve('/static/test.css')
        media_match = resolver.resolve('/media/test.jpg')

        self.assertIsNotNone(static_match)
        self.assertIsNotNone(media_match)

    @override_settings(DEBUG=False)
    def test_urls_debug_false_import(self):
        import importlib
        import project.urls
        importlib.reload(project.urls)
