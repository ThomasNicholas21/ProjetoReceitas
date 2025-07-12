from django.urls import reverse, resolve
from recipes.tests.test_base_fixture import RecipeFixture
from recipes import views


class RecipeDetailViewTest(RecipeFixture):
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

    def test_recipe_detail_template_loads_one_recipe(self):
        """Test if recipe loads in detail page"""
        needed_title = 'Detail Test'
        needed_preparation_steps = 'Step Description Test'
        self.make_recipe(
            title=needed_title,
            preparation_steps=needed_preparation_steps
            )

        response = self.client.get(
            reverse(
                'recipes:recipe',
                kwargs={
                    'id_recipe': 1
                    }
                )
            )
        content = response.content.decode('utf-8')

        self.assertIn(needed_title, content)
        self.assertIn(needed_preparation_steps, content)

    def test_recipe_detail_template_dont_load_recipe_not_published(self):
        """Test if recipe is_published is False and doesn't loads the recipe"""
        recipe = self.make_recipe(is_published=False)

        response = self.client.get(
            reverse(
                'recipes:recipe',
                kwargs={
                    'id_recipe': recipe.pk
                }
                )
            )

        self.assertEqual(response.status_code, 404)
