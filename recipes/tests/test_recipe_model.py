from django.core.exceptions import ValidationError
from parameterized import parameterized
from recipes.tests.test_recipes_fixture import RecipeFixture


class RecipeModelTest(RecipeFixture):
    def setUp(self):
        self.recipe = self.make_recipe()
        return super().setUp()

    @parameterized.expand(
            [
                ('title', 64),
                ('description', 168),
                ('preparation_time_unit', 64),
                ('servings_unit', 64),
            ]
        )
    def test_recipe_model_fields_max_length(self, field, max_length):
        """"Test fields that have max_length"""
        setattr(self.recipe, field, 'Teste' * max_length)
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()
