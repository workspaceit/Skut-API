from rest_framework import serializers
from scooter_models.models import ScooterModel
from scooter_categories.scooter_category_serializer import ScooterCategorySerializer


class ScooterModelSerializer(serializers.ModelSerializer):
    category = ScooterCategorySerializer(read_only=True)
    category_id = serializers.CharField(write_only=True)

    class Meta:
        model = ScooterModel
        fields = ('id', 'name', 'description', 'category', 'category_id', 'created_at')
