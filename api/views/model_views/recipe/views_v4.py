from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from recipes.models import Recipe
from api.views.model_views.serializer import RecipeSerializer
from api.paginator import DefaultPaginationOffset
from api.permissions import IsOwner


class ViewSetRecipes(ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    pagination_class = DefaultPaginationOffset
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.request.method in ["PATCH", "PUT", "DELETE"]:
            return [IsOwner(),]

        return super().get_permissions()

    def partial_update(self, request: Request, *args, **kwargs):
        pk = kwargs.get('pk')
        recipe = Recipe.objects.get(pk=pk)
        serializar = RecipeSerializer(
            instance=recipe,
            data=request.data,
            partial=True,
            context={
                'request': request
            }
        )
        serializar.is_valid(raise_exception=True)
        serializar.save()
        return Response(serializar.data)
