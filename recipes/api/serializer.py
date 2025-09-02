from rest_framework import serializers

from recipes.models import Recipe, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "name"
        ]


class RecipeSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(
        many=False
    )

    class Meta:
        model = Recipe
        fields = [
            "id", "title", "description", "preparation_time",
            "preparation_time_unit", "servings", "servings_unit",
            "preparation_steps", "preparation_steps_is_html", "created_at",
            "updated_at", "is_published", "cover", "author", "category"
        ]

    def validate(self, attrs):
        if self.instance is not None and attrs.get('servings') is None:
            attrs['servings'] = self.instance.servings

        if self.instance is not None and attrs.get('preparation_time') is None:
            attrs['preparation_time'] = self.instance.preparation_time

        title = attrs.get('title')
        description = attrs.get('description')
        if title == description:
            raise serializers.ValidationError(
                {
                    "error": "Título e descrição não podem ser iguais"
                }
            )

        return super().validate(attrs)

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError(
                {
                    "error": "Título deve conter no mínimo 5 caracteres"
                }
            )

        return value
