from django.urls import reverse, resolve
from unittest.mock import patch
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

    def test_category_pagination_returns_status_code_200(self):
        """Testing status code returned by pagination"""
        for iterator in range(6):
            self.make_recipe(
                title=f'testing-pagination{iterator}',
                slug=f'testing-pagination-{iterator}',
                author_data={
                    'username': f'testing-pagination-{iterator}'
                },
                category_data={
                    'name': 'testing-pagination'
                }
            )

        response = self.client.get(
            reverse(
                'recipes:category',
                kwargs={
                    'id_category': 1
                }
            ) + '?page=2'
        )
        self.assertEqual(response.status_code, 200)

    def test_category_pagination_returns_status_code_404(self):
        """Test if client trys to access a invalid page"""
        for iterator in range(6):
            self.make_recipe(
                title=f'testing-pagination{iterator}',
                slug=f'testing-pagination-{iterator}',
                author_data={
                    'username': f'testing-pagination-{iterator}'
                }
            )
        response = self.client.get(
            reverse(
                'recipes:category',
                kwargs={
                    'id_category': 1
                }
            ) + '?page=5'
        )
        self.assertEqual(response.status_code, 404)

    def test_category_pagination_and_objects_per_page(self):
        """
        Test if there are 3 objects per page in pagination.
        This test may be useless if PER_PAGE != 3
        """
        for iterator in range(6):
            self.make_recipe(
                title=f'testing-pagination{iterator}',
                slug=f'testing-pagination-{iterator}',
                author_data={
                    'username': f'testing-pagination-{iterator}'
                }
            )

        with patch('recipes.views.PER_PAGE', new=3):
            response = self.client.get(
                reverse(
                    'recipes:category',
                    kwargs={
                        'id_category': 1
                    }
                )
            )
            recipes = response.context['recipes']
            paginator = recipes.paginator

            self.assertEqual(paginator.num_pages, 2)
            self.assertEqual(len(paginator.get_page(1)), 3)
            self.assertEqual(len(paginator.get_page(2)), 3)

    def test_category_pagination_value_error(self):
        """
        Testing if Value Error is been trated appropriately
        by the make_pagination() function
        """
        response = self.client.get(
            reverse(
                'recipes:category',
                kwargs={
                    'id_category': 1
                }
            ) + '?page=1'
        )
        response_except_value_error = self.client.get(
            reverse(
                'recipes:category',
                kwargs={
                    'id_category': 1
                }
            ) + '?page=a'
        )

        self.assertEqual(
            response.content, response_except_value_error.content
        )
