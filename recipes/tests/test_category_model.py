from django.core.exceptions import ValidationError
from recipes.tests.test_base_fixture import RecipeFixture


class CategoryModelTest(RecipeFixture):
    def setUp(self):
        self.category = self.make_category()
        return super().setUp()

    def test_category_name_max_length(self):
        """Testing if max_length param is correct"""
        setattr(self.category, 'name', 'Test' * 64)
        with self.assertRaises(ValidationError):
            self.category.full_clean()

    def test_category_model_str_method(self):
        """Testing if __str__ method is correct"""
        self.category.name = 'Testing __str__ special method'
        self.category.full_clean()
        self.category.save()

        self.assertEqual(
            str(self.category),
            f'Categoria: {self.category.name }'
        )
