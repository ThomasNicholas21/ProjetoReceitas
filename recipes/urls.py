from django.urls import path
from recipes import views


app_name = 'recipes'


urlpatterns = [
    # home
    path(
        '',
        views.home,
        name='home'
    ),

    # recipe
    path(
        'recipes/<int:id_recipe>/',
        views.recipe, name='recipe'
    ),

    # category
    path(
        'recipes/category/<int:id_category>/',
        views.category,
        name='category'
    ),
]
