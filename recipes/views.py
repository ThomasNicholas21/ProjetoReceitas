from django.shortcuts import render
from django.shortcuts import get_object_or_404
from recipes.models import Recipe


def home(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes,
    }

    return render(
        request=request,
        template_name='recipes/pages/home.html',
        context=context
    )


def recipe(request, id_recipe):
    recipe = get_object_or_404(
        Recipe,
        id=id_recipe
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
