from rest_framework import serializers
from django.contrib.humanize.templatetags.humanize import naturaltime
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    book_title = serializers.ReadOnlyField(source='book.title')
    reviewer = serializers.ReadOnlyField(source='user.username')
    time_since_reviewed = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ['id', 'book_title', 'reviewer', 'review_text', 'rating', 'time_since_reviewed']

    def get_time_since_reviewed(self, obj):
        return naturaltime(obj.created_at)
