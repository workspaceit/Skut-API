from rest_framework import serializers
from scooter_categories.models import ScooterCategory


class ScooterCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ScooterCategory
        fields = ('id', 'name', 'description', 'created_at')
