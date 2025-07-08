from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views


class RecipeHomeViewTest(TestCase):
    def test_recipes_home_view_function_is_correct(self):
        """Test if home view is correct"""
        home_view = resolve(reverse('recipes:home'))
        self.assertIs(home_view.func, views.home)

    def test_recipes_home_view_status_code_200(self):
        """Test if home view status code is correct"""
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipes_home_view_loads_correct_template(self):
        """Test if home view status code is correct"""
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        """Test if home view template that doens`t have recipes is correct"""
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            'Nenhuma receita entrada no momento 😔',
            response.content.decode('utf-8'),
            )


class RecipeDetailViewTest(TestCase):
    def test_recipes_detail_view_function_is_correct(self):
        """Test if detail view is correct"""
        recipe_view = resolve(
            reverse(
                'recipes:recipe',
                kwargs={
                    'id_recipe': 1
                    }
                )
            )
        self.assertIs(recipe_view.func, views.recipe)

    def test_recipes_detail_view_status_code_404_if_no_recipes(self):
        """Test if detail view status code is correct"""
        response = self.client.get(
            reverse(
                'recipes:recipe',
                kwargs={
                    'id_recipe': 1000
                    }
                )
            )
        self.assertEqual(response.status_code, 404)


class RecipeCategoryViewTest(TestCase):
    def test_recipes_category_view_function_is_correct(self):
        """Test if category view is correct"""
        category_view = resolve(
            reverse(
                'recipes:category',
                kwargs={
                    'id_category': 1
                    }
                )
            )
        self.assertIs(category_view.func, views.category)

    def test_recipes_category_view_status_code_404_if_no_recipes(self):
        """Test if category view status code is correct"""
        response = self.client.get(
            reverse(
                'recipes:category',
                kwargs={
                    'id_category': 122121
                    }
                )
            )
        self.assertEqual(response.status_code, 404)
