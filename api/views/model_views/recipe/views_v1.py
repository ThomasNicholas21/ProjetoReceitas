from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from recipes.models import Recipe
from api.views.model_views.serializer import RecipeSerializer


@api_view(["GET", "POST"])
def recipe_api_view(request):
    if request.method == "GET":
        recipes = Recipe.objects.all().order_by("id")
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = RecipeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    else:
        return Response(
            {
                "Error": "Method not allowed"
            },
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )


@api_view(["GET", "PATCH", "PUT", "DELETE"])
def detail_recipes_api_view(request, pk):
    if request.method == "GET":
        recipe = Recipe.objects.get(pk=pk)
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)

    elif request.method == "PATCH":
        serializer = RecipeSerializer(
            instance=Recipe.objects.get(pk=pk),
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = RecipeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    elif request.method == "DELETE":
        recipe = Recipe.objects.get(pk=pk)
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    else:
        return Response(
            {
                "Error": "Method not allowed"
            },
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )
