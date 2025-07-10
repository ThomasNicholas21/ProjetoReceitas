from django.core.exceptions import ValidationError
from parameterized import parameterized
from recipes.tests.test_recipes_fixture import RecipeFixture
from recipes.models import Recipe


class RecipeModelTest(RecipeFixture):
    def setUp(self):
        self.recipe = self.make_recipe()
        return super().setUp()

    def make_recipe_no_defaults(self):
        recipe = Recipe(
            title='Title Test Html',
            description='Description Test Html',
            slug='test-slug-html',
            preparation_time=10,
            preparation_time_unit='minutos',
            servings=5,
            servings_unit='Serving unit Html',
            preparation_steps='Preparation steps Html',
            author=self.make_author(username='Test Auhtor'),
            category=self.make_category(name='Test'),
        )
        recipe.full_clean()
        recipe.save()
        return recipe

    @parameterized.expand(
            [
                ('title', 64),
                ('description', 168),
                ('preparation_time_unit', 64),
                ('servings_unit', 64),
            ]
        )
    def test_recipe_model_fields_with_max_length(self, field, max_length):
        """"Test fields that have max_length param"""
        setattr(self.recipe, field, 'Teste' * max_length)
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    @parameterized.expand(
            [
                ('preparation_steps_is_html', False),
                ('is_published', False),
                ('cover', 'default/hamburguer.png'),
            ]
    )
    def test_recipe_model_fields_with_default(self, field, default):
        """Test fields that have default param"""
        recipe = self.make_recipe_no_defaults()
        current_atribute_value = getattr(recipe, field)
        self.assertEqual(
            current_atribute_value,
            default,
            msg=f'"{field}" default value is not "{current_atribute_value}"'
        )
