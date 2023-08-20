from rest_framework import serializers
from .models import Comment
from django.contrib.humanize.templatetags.humanize import naturaltime

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    book_title = serializers.ReadOnlyField(source='review.book.title')
    time_since_posted = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'review', 'username', 'book_title', 'comment_text', 'time_since_posted']

    def get_time_since_posted(self, obj):
        return naturaltime(obj.created_at)
