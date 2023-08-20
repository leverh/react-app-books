from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    cover_image_url = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'isbn_number', 'summary', 'cover_image', 'created_by', 'created_at', 'updated_at']

    def get_cover_image_url(self, obj):
        if obj.cover_image:
            return obj.cover_image.url
        return None
