from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from django.core.paginator import Paginator
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.http import Http404
from django.db.models import Q
from recipes.models import Recipe
from utils.recipes.pagination import make_pagination_range


def home(request: HttpRequest) -> HttpResponse:
    recipes = (
        Recipe
        .objects
        .filter(
            is_published=True
            )
        ).order_by(
            '-id'
        )

    try:
        current_page = int(request.GET.get('page', 1))
    except ValueError:
        current_page = 1

    paginator = Paginator(recipes, 6)
    page_obj = paginator.get_page(current_page)

    pagination_range = make_pagination_range(
        page_range=paginator.page_range,
        pages=4,
        current_page=current_page
    )

    context = {
        'recipes': page_obj,
        'pagination_range': pagination_range
    }

    return render(
        request=request,
        template_name='recipes/pages/home.html',
        context=context
    )


def category(request: HttpRequest, id_category) -> HttpResponse:
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


def recipe(request: HttpRequest, id_recipe) -> HttpResponse:
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


def search(request: HttpRequest) -> HttpResponse:
    search_request: str = request.GET.get('q', '').strip()
    context: dict = {
        'page_title': f'Pesquisa: {search_request}',
        'search_request': search_request
    }

    if not search_request:
        raise Http404()

    recipes = Recipe.objects.filter(
        Q(
            Q(title__icontains=search_request) |
            Q(description__icontains=search_request)
        ),
        is_published=True
    ).order_by('-id')

    context['recipes'] = recipes

    return render(
        request=request,
        template_name='recipes/pages/search.html',
        context=context
    )
