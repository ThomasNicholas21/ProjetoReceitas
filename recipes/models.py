from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(
        verbose_name=64
    )

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return f'Categoria: {self.name}'


class Recipe(models.Model):
    title = models.CharField(
        max_length=64
        )
    description = models.CharField(
        max_length=168
        )
    slug = models.SlugField()
    prepartion_time = models.IntegerField()
    prepartion_time_unit = models.CharField(
        max_length=64
        )
    servings = models.IntegerField()
    servings_unit = models.CharField(
        max_length=64
    )
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(
        default=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='author_recipe'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='category_recipe'
    )

    class Meta:
        verbose_name = 'Receita'
        verbose_name_plural = 'Receitas'

    def __str__(self):
        return f'Receita {self.title} de {self.author.first_name}'
