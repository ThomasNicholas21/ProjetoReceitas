from django.urls import path
from .views import ViewSetRecipes


urlpatterns = [
    # Api View Sets
    path(
        'recipes/',
        ViewSetRecipes.as_view(
            {
                "get": "list",
                "post": "create"
            }
        ),
        name="recipe-api-v2-list"
    ),
    path(
        'recipe/<int:pk>/',
        ViewSetRecipes.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy"
            }
        ),
        name="recipe-api-v2-detail"
    ),
]
