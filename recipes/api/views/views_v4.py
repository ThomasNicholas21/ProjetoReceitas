from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from recipes.models import Recipe
from recipes.api.serializer import RecipeSerializer


class ViewSetRecipes(ModelViewSet):
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
