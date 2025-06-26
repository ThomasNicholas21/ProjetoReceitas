from django.shortcuts import render
from utils.recipes.data_factory import make_recipe


def home(request):
    return render(
        request=request,
        template_name='recipes/pages/home.html',
        context={
            'recipes': [make_recipe() for _ in range(10)],
        }
    )


def recipe(request, id_recipe):
    return render(
        request=request,
        template_name='recipes/pages/recipe.html',
        context={
            'recipe': make_recipe(),
            'is_detail_page': True
        }
    )
