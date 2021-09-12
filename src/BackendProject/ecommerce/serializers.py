from rest_framework import serializers
from . models import Products
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

class ProductSerializer(serializers.ModelSerializer):
    """Serializers Class allows data to be converted to JSON datatypes"""
    class Meta:
        model = Products
        fields= ('name', 'price', 'start_date') 
        extra_kwargs = {
            'name': {
                'validators': [
                    UniqueValidator(
                        queryset=Products.objects.all()
                    )
                ]
            }
        }