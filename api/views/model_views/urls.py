from django.urls import path
from .recipe import (
    RecipesApiView,
    DetailRecipesApiView,
    GenericRecipesApiView,
    GenericDetailRecipesApiView,
    ViewSetRecipes
)


urlpatterns = [
    # APIView V2
    path(
        'v2/recipes/',
        RecipesApiView.as_view(),
        name="recipe-api-v2-list"
    ),
    path(
        'v2/recipes/<int:pk>/',
        DetailRecipesApiView.as_view(),
        name="recipe-api-v2-detail"
    ),
    # APIGenerics V3
    path(
        'v3/recipes/',
        GenericRecipesApiView.as_view(),
        name="recipe-api-v2-list"
    ),
    path(
        'v4/recipes/<int:pk>/',
        GenericDetailRecipesApiView.as_view(),
        name="recipe-api-v2-detail"
    ),
    # APIViewsSets V4
    path(
        'v4/recipes/',
        ViewSetRecipes.as_view(
            {
                "get": "list",
                "post": "create"
            }
        ),
        name="recipe-api-v2-list"
    ),
    path(
        'v4/recipes/<int:pk>/',
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
