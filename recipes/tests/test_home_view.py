from django.urls import reverse, resolve
from unittest.mock import patch
from recipes.tests.test_base_fixture import RecipeFixture
from recipes import views


class RecipeHomeViewTest(RecipeFixture):
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

    def test_recipe_home_template_loads_recipe(self):
        """Test if recipe loads in home page"""
        self.make_recipe()

        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        response_context_recipes = response.context['recipes']

        self.assertIn('Test', content)
        self.assertIn('Description test', content)
        self.assertIn('60', content)
        self.assertIn('minutos', content)
        self.assertIn('5', content)
        self.assertIn('serving test unit', content)
        self.assertEqual(len(response_context_recipes), 1)

    def test_recipe_home_template_dont_load_recipes_not_published(self):
        """Test if recipe is_published is False and doesn't loads the recipe"""
        self.make_recipe(is_published=False)

        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        response_context_recipes = response.context['recipes']

        self.assertEqual(len(response_context_recipes), 0)
        self.assertIn(
            'Nenhuma receita entrada no momento 😔',
            content,
        )

    def test_home_pagination_returns_status_code_200(self):
        """Testing status code returned by pagination"""
        for iterator in range(6):
            self.make_recipe(
                title=f'testing-pagination{iterator}',
                slug=f'testing-pagination-{iterator}',
                author_data={
                    'username': f'testing-pagination-{iterator}'
                }
            )
        response = self.client.get(reverse('recipes:home') + '?page=2')
        self.assertEqual(response.status_code, 200)

    def test_home_pagination_returns_status_code_404(self):
        """Test if client trys to access a invalid page"""
        for iterator in range(6):
            self.make_recipe(
                title=f'testing-pagination{iterator}',
                slug=f'testing-pagination-{iterator}',
                author_data={
                    'username': f'testing-pagination-{iterator}'
                }
            )
        response = self.client.get(reverse('recipes:home') + '?page=5')
        self.assertEqual(response.status_code, 404)

    def test_home_pagination_and_objects_per_page(self):
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
            response = self.client.get(reverse('recipes:home'))
            recipes = response.context['recipes']
            paginator = recipes.paginator

            self.assertEqual(paginator.num_pages, 2)
            self.assertEqual(len(paginator.get_page(1)), 3)
            self.assertEqual(len(paginator.get_page(2)), 3)

    def test_home_pagination_value_error(self):
        """
        Testing if Value Error is been trated appropriately
        by the make_pagination() function
        """
        response = self.client.get(
            reverse('recipes:home') + '?page=1'
        )
        response_except_value_error = self.client.get(
            reverse('recipes:home') + '?page=a'
        )

        self.assertEqual(
            response.content, response_except_value_error.content
        )
