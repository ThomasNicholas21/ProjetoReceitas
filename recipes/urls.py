from django.urls import path, include
from recipes import views


app_name = 'recipes'


urlpatterns = [
    # home
    path(
        '',
        views.home,
        name='home'
    ),

    # search
    path(
        'recipes/search/',
        views.search,
        name='search'
    ),

    # recipe
    path(
        'recipes/<int:id_recipe>/',
        views.recipe,
        name='recipe'
    ),

    # category
    path(
        'recipes/category/<int:id_category>/',
        views.category,
        name='category'
    ),
    # apis
    path('api/v2/', include('recipes.api.urls_v2')),
    path('api/v3/', include('recipes.api.urls_v3')),
    path('api/v4/', include('recipes.api.urls_v4'))
]
