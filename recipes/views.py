from django.shortcuts import render


def home(request):
    return render(
        request=request,
        template_name='recipes/pages/home.html',
    )


def recipe(request, id_recipe):
    return render(
        request=request,
        template_name='recipes/pages/recipe.html',
    )
