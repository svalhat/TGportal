from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = ['id','firstname','lastname','age','address','copyrightby']
        fields = '__all__'