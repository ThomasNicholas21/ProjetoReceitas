from django.urls import path
from .views import (
    GenericRecipesApiView,
    GenericDetailRecipesApiView
)


urlpatterns = [
    # Api generic views
    path(
        'recipes/',
        GenericRecipesApiView.as_view(),
        name="recipe-api-v2-list"
    ),
    path(
        'recipe/<int:pk>/',
        GenericDetailRecipesApiView.as_view(),
        name="recipe-api-v2-detail"
    ),
]
