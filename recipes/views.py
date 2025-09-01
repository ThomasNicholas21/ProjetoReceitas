from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.http import Http404
from django.db.models import Q
from django.contrib import messages
from recipes.models import Recipe
from utils.recipes.pagination import make_pagination
import os


PER_PAGE = os.environ.get('PER_PAGE', 3)


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

    page_obj, pagination_range, current_page = make_pagination(
        request=request,
        queryset=recipes,
        per_page=PER_PAGE,
        pages=4
    )

    if current_page > len(pagination_range.get('page_range')):
        raise Http404()

    current_page_title = f'Página atual: {current_page}'
    context = {
        'recipes': page_obj,
        'pagination_range': pagination_range,
        'page_title': (
            f'Home | {current_page_title}'
            if current_page else 'Home'
        ),
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
    page_obj, pagination_range, current_page = make_pagination(
        request=request,
        queryset=recipes,
        per_page=PER_PAGE,
        pages=4
    )

    if current_page > len(pagination_range.get('page_range')):
        raise Http404()

    category_title = f'Categoria: {recipe.first().category.name}'
    current_page_title = f'Página atual: {current_page}'
    context = {
            'recipes': page_obj,
            'pagination_range': pagination_range,
            'page_title': (
                f'{category_title} | {current_page_title}'
                if current_page else f'{category}'
            ),
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
            'is_detail_page': True,
            'page_title': f'Receita: {recipe.title}'
        }
    return render(
        request=request,
        template_name='recipes/pages/recipe.html',
        context=context
    )


def search(request: HttpRequest) -> HttpResponse:
    search_request: str = request.GET.get('q', '').strip()

    if not search_request:
        raise Http404()

    recipes = Recipe.objects.filter(
        Q(
            Q(title__icontains=search_request) |
            Q(description__icontains=search_request)
        ),
        is_published=True
    ).order_by('-id')

    page_obj, pagination_range, current_page = make_pagination(
        request=request,
        queryset=recipes,
        per_page=PER_PAGE,
        pages=4
    )

    if current_page > len(pagination_range.get('page_range')):
        raise Http404()

    search_title = f'Pesquisa: {search_request}'
    current_page_title = f'Página atual: {current_page}'
    context: dict = {
        'recipes': page_obj,
        'pagination_range': pagination_range,
        'page_title': (
            f'{search_title} | {current_page_title}'
            if current_page else f'Pesquisa: {search_request}'
            ),
        'search_request': search_request,
        'additional_query_string': f'&q={search_request}'
    }
    return render(
        request=request,
        template_name='recipes/pages/search.html',
        context=context
    )
