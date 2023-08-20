from rest_framework import serializers
from .models import Favorite
from django.contrib.humanize.templatetags.humanize import naturaltime

class FavoriteSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    book_title = serializers.ReadOnlyField(source='book.title')
    time_since_added = serializers.SerializerMethodField()

    class Meta:
        model = Favorite
        fields = ['id', 'username', 'book_title', 'date_added', 'time_since_added']

    def get_time_since_added(self, obj):
        return naturaltime(obj.date_added)
