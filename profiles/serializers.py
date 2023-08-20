from rest_framework import serializers
from django.contrib.humanize.templatetags.humanize import naturaltime
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='owner.username')
    time_since_created = serializers.SerializerMethodField()
    time_since_updated = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['id', 'username', 'created_at', 'time_since_created', 'updated_at', 'time_since_updated', 'name', 'content', 'image']

    def get_time_since_created(self, obj):
        return naturaltime(obj.created_at)

    def get_time_since_updated(self, obj):
        return naturaltime(obj.updated_at)
