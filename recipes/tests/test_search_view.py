from django.urls import reverse, resolve
from recipes.tests.test_base_fixture import RecipeFixture
from recipes import views


class RecipeSearchViewTest(RecipeFixture):
    def test_recipes_search_view_function_is_correct(self):
        """Test if search view is correct"""
        search_view = resolve(reverse('recipes:search'))
        self.assertIs(search_view.func, views.search)

    def test_recipe_search_template_loads_recipe(self):
        """Test if search view loads the correct template"""
        response = self.client.get(reverse('recipes:search') + '?q=test')
        self.assertTemplateUsed(response, 'recipes/pages/search.html')

    def test_recipes_search_view_status_code_404_if_no_search_term(self):
        """Test if search view return the correct status code"""
        response = self.client.get(reverse('recipes:search'))
        self.assertEqual(response.status_code, 404)

    def test_recipes_search_request_is_on_page_and_escaped(self):
        """Test if view function is protecting variables sented by user"""
        response = self.client.get(reverse('recipes:search') + '?q=<Test>')
        self.assertIn(
            "Pesquisa: &lt;Test&gt",
            response.content.decode('utf-8')
        )

    def test_recipes_search_view_filter_return_recipe_with_title(self):
        """Test if search filter returns recipes with the correct title"""
        title1 = 'This title1 must be in response content'
        title2 = 'This title2 must be in response content'

        recipe1 = self.make_recipe(
            title=title1,
            slug='one',
            author_data={
                'username': 'one'
            }
        )
        recipe2 = self.make_recipe(
            title=title2,
            slug='two',
            author_data={
                'username': 'two'
            }
        )

        response1 = self.client.get(
            reverse('recipes:search') + f'?q={title1}'
        )
        response2 = self.client.get(
            reverse('recipes:search') + f'?q={title2}'
        )
        response_both = self.client.get(
            reverse('recipes:search') + '?q=this'
        )

        self.assertIn(recipe1, response1.context['recipes'])
        self.assertNotIn(recipe2, response1.context['recipes'])

        self.assertIn(recipe2, response2.context['recipes'])
        self.assertNotIn(recipe1, response2.context['recipes'])

        self.assertIn(recipe1, response_both.context['recipes'])
        self.assertIn(recipe2, response_both.context['recipes'])

    def test_recipes_search_view_filter_return_recipe_with_description(self):
        """
        Test if search filter returns recipes with the correct description
        """
        description1 = 'This description1 must be in response content'
        description2 = 'This description2 must be in response content'

        recipe1 = self.make_recipe(
            description=description1,
            slug='one',
            author_data={
                'username': 'one-'
            }
        )
        recipe2 = self.make_recipe(
            description=description2,
            slug='two-',
            author_data={
                'username': 'two'
            }
        )

        response1 = self.client.get(
            reverse('recipes:search') + f'?q={description1}'
        )
        response2 = self.client.get(
            reverse('recipes:search') + f'?q={description2}'
        )
        response_both = self.client.get(
            reverse('recipes:search') + '?q=this'
        )

        self.assertIn(recipe1, response1.context['recipes'])
        self.assertNotIn(recipe2, response1.context['recipes'])

        self.assertIn(recipe2, response2.context['recipes'])
        self.assertNotIn(recipe1, response2.context['recipes'])

        self.assertIn(recipe1, response_both.context['recipes'])
        self.assertIn(recipe2, response_both.context['recipes'])

    def test_recipes_search_returns_recipe_with_title_and_description(self):
        """
        Test if search filter returns recipes
        with the correct title and description
        """
        description1 = 'This description1 must be in response content'
        title2 = 'This title2 must be in response content'

        recipe1 = self.make_recipe(
            description=description1,
            slug='one',
            author_data={
                'username': 'one'
            }
        )
        recipe2 = self.make_recipe(
            description=title2,
            slug='two-',
            author_data={
                'username': 'two'
            }
        )

        response1 = self.client.get(
            reverse('recipes:search') + f'?q={description1}'
        )
        response2 = self.client.get(
            reverse('recipes:search') + f'?q={title2}'
        )
        response_both = self.client.get(
            reverse('recipes:search') + '?q=this'
        )

        self.assertIn(recipe1, response1.context['recipes'])
        self.assertNotIn(recipe2, response1.context['recipes'])

        self.assertIn(recipe2, response2.context['recipes'])
        self.assertNotIn(recipe1, response2.context['recipes'])

        self.assertIn(recipe1, response_both.context['recipes'])
        self.assertIn(recipe2, response_both.context['recipes'])

    def test_recipes_search_view_return_status_code_404_if_empty(self):
        empty_text = ' '
        response = self.client.get(
            reverse(
                'recipes:search') + f'?q={empty_text}'
                )

        self.assertEqual(response.status_code, 404)
