from django.urls import reverse, resolve
from recipes.tests.base_fixture import RecipeFixture
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
