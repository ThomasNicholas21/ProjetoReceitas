from django.urls import reverse, resolve
from recipes.tests.test_recipes_fixture import RecipeFixture
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
        """Test if recipe loads in category page"""
        needed_title = 'Detail Test'
        needed_step = 'Step Description Test'
        self.make_recipe(
            title=needed_title,
            preparation_steps=needed_step
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
        self.assertIn(needed_step, content)


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
