from .views_v1 import * # noqa
from .views_v2 import RecipesApiView, DetailRecipesApiView # noqa
from .views_v3 import GenericRecipesApiView, GenericDetailRecipesApiView # noqa
from .views_v4 import ViewSetRecipes # noqa


__all__ = [
    "RecipesApiView",
    "DetailRecipesApiView",
    "GenericRecipesApiView",
    "GenericDetailRecipesApiView",
    "ViewSetRecipes"
]
