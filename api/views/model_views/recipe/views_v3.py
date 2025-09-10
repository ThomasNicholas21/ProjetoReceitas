from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from recipes.models import Recipe
from api.views.model_views.serializer import RecipeSerializer
from api.paginator import DefaultPaginationOffset
from api.permissions import IsOwner


class GenericRecipesApiView(ListCreateAPIView):
    queryset = Recipe.objects.all().order_by("id")
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = DefaultPaginationOffset


class GenericDetailRecipesApiView(RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get_permissions(self):
        if self.request.method in ["PATCH", "PUT", "DELETE"]:
            return [IsOwner(),]

        return super().get_permissions()

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
