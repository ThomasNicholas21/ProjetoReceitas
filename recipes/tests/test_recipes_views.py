from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views


class RecipeViewsTest(TestCase):
    def test_recipes_home_view_function_is_correct(self):
        home_view = resolve(reverse('recipes:home'))
        self.assertIs(home_view.func, views.home)

    def test_recipes_detail_view_function_is_correct(self):
        recipe_view = resolve(
            reverse(
                'recipes:recipe',
                kwargs={
                    'id_recipe': 1
                    }
                )
            )
        self.assertIs(recipe_view.func, views.recipe)

    def test_recipes_category_view_function_is_correct(self):
        category_view = resolve(
            reverse(
                'recipes:category',
                kwargs={
                    'id_category': 1
                    }
                )
            )
        self.assertIs(category_view.func, views.category)
