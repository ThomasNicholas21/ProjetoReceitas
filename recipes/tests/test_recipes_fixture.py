from django.test import TestCase
from recipes import models


class RecipeFixture(TestCase):
    def setUp(self):
        """Fixture to create test models"""
        return super().setUp()

    def make_category(self, name='Category Test'):
        """Create category to test"""
        return models.Category.objects.create(name=name)

    def make_author(
            self,
            first_name='User',
            last_name='Name',
            username='Test',
            email='test@test.com',
            password='123456',
    ):
        """Create author to test"""
        return (
            models
            .User
            .objects
            .create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password,
            )
        )

    def make_recipe(
            self,
            title='Test',
            description='Description test',
            slug='test-slug',
            preparation_time=60,
            preparation_time_unit='minutos',
            servings=5,
            servings_unit='serving test unit',
            preparation_steps='test steps',
            author_data=None,
            category_data=None,
            is_published=True
    ):
        """Create recipe to test"""
        if author_data is None:
            author_data = {}

        if category_data is None:
            category_data = {}

        return (
            models
            .Recipe
            .objects
            .create(
                title=title,
                description=description,
                slug=slug,
                preparation_time=preparation_time,
                preparation_time_unit=preparation_time_unit,
                servings=servings,
                servings_unit=servings_unit,
                preparation_steps=preparation_steps,
                author=self.make_author(**author_data),
                category=self.make_category(**category_data),
                is_published=is_published
            )
        )
