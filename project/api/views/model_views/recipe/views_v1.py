from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import status

from recipes.models import Recipe
from api.views.model_views.serializer import RecipeSerializer
from api.paginator import DefaultPaginationOffset
from api.permissions import IsOwner


@permission_classes([IsAuthenticatedOrReadOnly,])
@api_view(["GET", "POST"])
def recipe_api_view(request):
    paginator = DefaultPaginationOffset()
    paginator.page_size = 10
    if request.method == "GET":
        recipes = Recipe.objects.all().order_by("id")
        result = paginator.paginate_queryset(recipes, request)
        serializer = RecipeSerializer(result, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = RecipeSerializer(
            data=request.data,
        )
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
@permission_classes([IsAuthenticatedOrReadOnly])
def detail_recipes_api_view(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)

    if request.method in ["PATCH", "PUT", "DELETE"]:
        permission = IsOwner()
        if not permission.has_object_permission(request, None, recipe):
            raise PermissionDenied((
                "Você não tem permissão para "
                "editar ou deletar esta receita."
                )
            )

    if request.method == "GET":
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)

    elif request.method in ["PUT", "PATCH"]:
        is_partial = request.method == 'PATCH'
        serializer = RecipeSerializer(
            instance=recipe,
            data=request.data,
            partial=is_partial,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    elif request.method == "DELETE":
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
