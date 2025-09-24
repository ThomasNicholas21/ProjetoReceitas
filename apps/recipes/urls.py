from django.urls import path
from apps.recipes import views


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
        'search/',
        views.search,
        name='search'
    ),

    # recipe
    path(
        '<int:id_recipe>/',
        views.recipe,
        name='recipe'
    ),

    # category
    path(
        'category/<int:id_category>/',
        views.category,
        name='category'
    ),
]
