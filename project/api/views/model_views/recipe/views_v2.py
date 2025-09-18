from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status

from recipes.models import Recipe
from project.api.views.model_views.serializer import RecipeSerializer
from project.api.paginator import DefaultPaginationOffset
from project.api.permissions import IsOwner


class RecipesApiView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        paginator = DefaultPaginationOffset()
        recipes = Recipe.objects.all().order_by("id")
        result = paginator.paginate_queryset(recipes, request)
        serializer = RecipeSerializer(result, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RecipeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class DetailRecipesApiView(APIView):
    def get_permissions(self):
        if self.request.method in ["PATCH", "PUT", "DELETE"]:
            return [IsOwner(),]

        return super().get_permissions()

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
