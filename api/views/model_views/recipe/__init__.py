from .views_v1 import recipe_api_view, detail_recipes_api_view # noqa
from .views_v2 import RecipesApiView, DetailRecipesApiView # noqa
from .views_v3 import GenericRecipesApiView, GenericDetailRecipesApiView # noqa
from .views_v4 import ViewSetRecipes # noqa


__all__ = [
    "recipe_api_view",
    "detail_recipes_api_view",
    "RecipesApiView",
    "DetailRecipesApiView",
    "GenericRecipesApiView",
    "GenericDetailRecipesApiView",
    "ViewSetRecipes"
]
