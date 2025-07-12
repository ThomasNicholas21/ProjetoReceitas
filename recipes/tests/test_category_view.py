from django.urls import reverse, resolve
from recipes.tests.test_base_fixture import RecipeFixture
from recipes import views


class RecipeCategoryViewTest(RecipeFixture):
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

    def test_recipe_category_template_loads_recipe(self):
        """Test if recipe loads in category page"""
        needed_title = 'Category Test'
        self.make_recipe(title=needed_title)

        response = self.client.get(
            reverse(
                'recipes:category',
                kwargs={
                    'id_category': 1
                    }
                )
            )
        content = response.content.decode('utf-8')

        self.assertIn(needed_title, content)

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

    def test_recipe_category_template_dont_load_recipe_not_published(self):
        """Test if recipe is_published is False and doesn't loads the recipe"""
        recipe = self.make_recipe(is_published=False)

        response = self.client.get(
            reverse(
                'recipes:recipe',
                kwargs={
                    'id_recipe': recipe.category.pk
                }
                )
            )

        self.assertEqual(response.status_code, 404)
