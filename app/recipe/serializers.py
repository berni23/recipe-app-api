from rest_framework import serializers

from core.models import Ingredient, Tag, Recipe


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tag objects"""

    class Meta:
        model = Tag
        fields = ('id', 'name')

        # prevent user from modifying the primary key
        read_only_fields = ('id',)


class IngredientSerializer(serializers.ModelSerializer):
    """ Serializer for ingredient objects"""

    class Meta:
        model = Ingredient
        fields = ('id', 'name')
        read_only_fields = ('id',)


class RecipeSerializer(serializers.ModelSerializer):
    """ Serializer for recipe object """

    # primary key related field
    ingredients = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Ingredient.objects.all()
    )

    tags = serializers.PrimaryKeyRelatedField(

        many=True,
        queryset=Tag.objects.all()
    )

    class Meta:

        model = Recipe
        fields = ('id', 'title', 'ingredients', 'tags',
                  'time_minutes', 'price', 'link')

        read_only_fields = ('id',)
