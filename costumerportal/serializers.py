from rest_framework import serializers
from .models import Category, Product, Image, Other

# Serializer for Image
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image']

# Serializer for Other
class OtherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Other
        fields = ['id', 'title', 'price', 'image']

# Serializer for Category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

# Serializer for Product
class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    others = OtherSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    is_on_sale = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'price', 'sale_price',
            'is_on_sale', 'category', 'images', 'others'
        ]

    def get_is_on_sale(self, obj):
        return obj.is_on_sale()
