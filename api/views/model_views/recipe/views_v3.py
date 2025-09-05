from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.response import Response

from recipes.models import Recipe
from api.views.model_views.serializer import RecipeSerializer


class GenericRecipesApiView(ListCreateAPIView):
    queryset = Recipe.objects.all().order_by("id")
    serializer_class = RecipeSerializer


class GenericDetailRecipesApiView(RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def patch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        recipe = Recipe.objects.get(pk=pk)
        serializar = RecipeSerializer(
            instance=recipe,
            data=request.data,
            partial=True
        )
        serializar.is_valid(raise_exception=True)
        serializar.save()
        return Response(serializar.data)
