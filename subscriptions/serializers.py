from rest_framework import serializers
from django.contrib.humanize.templatetags.humanize import naturaltime
from .models import Subscription

class SubscriptionSerializer(serializers.ModelSerializer):
    subscriber_username = serializers.ReadOnlyField(source='subscriber.username')
    subscribee_username = serializers.ReadOnlyField(source='subscribee.username')
    time_since_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = Subscription
        fields = ['id', 'subscriber_username', 'subscribee_username', 'time_since_subscribed']

    def get_time_since_subscribed(self, obj):
        return naturaltime(obj.date_subscribed)
