from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from recipes.models import Recipe
from api.views.model_views.serializer import RecipeSerializer


class RecipesApiView(APIView):
    def get(self, request):
        recipes = Recipe.objects.all().order_by("id")
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RecipeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class DetailRecipesApiView(APIView):
    def get(self, request, pk):
        recipe = Recipe.objects.get(pk=pk)
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)

    def patch(self, request, pk):
        serializer = RecipeSerializer(
            instance=Recipe.objects.get(pk=pk),
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def put(self, request, pk):
        serializer = RecipeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        recipe = Recipe.objects.get(pk=pk)
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
