from django.urls import path
from .views import (
    RecipesApiView,
    DetailRecipesApiView
)


urlpatterns = [
    # Api views
    path(
        'recipes/',
        RecipesApiView.as_view(),
        name="recipe-api-v2-list"
    ),
    path(
        'recipe/<int:pk>/',
        DetailRecipesApiView.as_view(),
        name="recipe-api-v2-detail"
    )
]
