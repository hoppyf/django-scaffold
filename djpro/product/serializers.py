from rest_framework import serializers

from common.serializer import MySerializer
from product.models import Book


class BookSerializer(MySerializer):
    class Meta:
        model = Book


class BookUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200, required=True, allow_blank=True)
    price = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
