from rest_framework import serializers
from .models import WomenModel,Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'
class WomenSerializer(serializers.ModelSerializer):
    cat=CategorySerializer()
    class Meta:
        model= WomenModel
        exclude=['time_update']

