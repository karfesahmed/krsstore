from rest_framework import serializers
from .models import Category, Product, Image, Color,Size

# Serializer for Image
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image']

# Serializer for Color
class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id', 'title', 'image']


# Serializer for Size
class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id', 'title', 'price']

# Serializer for Category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

# Serializer for Product
class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    color = ColorSerializer(many=True, read_only=True)
    size = SizeSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    is_on_sale = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'price', 'sale_price',
            'is_on_sale', 'category', 'images', 'color','size'
        ]

    def get_is_on_sale(self, obj):
        return obj.is_on_sale()
