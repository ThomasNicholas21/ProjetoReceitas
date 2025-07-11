from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from recipes.models import Recipe


def home(request):
    recipes = (
        Recipe
        .objects
        .filter(
            is_published=True
            )
        ).order_by(
            '-id'
        )
    context = {
        'recipes': recipes,
    }

    return render(
        request=request,
        template_name='recipes/pages/home.html',
        context=context
    )


def category(request, id_category):
    recipe = (
        Recipe
        .objects
        .order_by(
            '-id'
        )
    )
    recipes = get_list_or_404(
        recipe,
        category__id=id_category,
        is_published=True
    )
    context = {
            'recipes': recipes,
        }
    return render(
        request=request,
        template_name='recipes/pages/category.html',
        context=context
    )


def recipe(request, id_recipe):
    recipe = get_object_or_404(
        Recipe,
        id=id_recipe,
        is_published=True
    )
    context = {
            'recipe': recipe,
            'is_detail_page': True
        }
    return render(
        request=request,
        template_name='recipes/pages/recipe.html',
        context=context
    )


def search():
    pass
