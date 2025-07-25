from rest_framework import serializers
from .models import *

class OrderSerializer(serializers.ModelSerializer):
    tracking_id = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = [
            'id', 'product', 'wilaya', 'IDwilaya', 'Name', 'Phone',
            'order_type', 'confirmed', 'delivery_type', 'Address',
            'Size', 'Color', 'quantity', 'total','note', 'tracking_id'
        ]
    def get_tracking_id(self, obj):
        return obj.tracking_id()