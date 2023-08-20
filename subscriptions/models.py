from django.db import models
from django.conf import settings

class Subscription(models.Model):
    subscriber = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='subscriptions', on_delete=models.CASCADE)
    subscribee = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='subscribers', on_delete=models.CASCADE)
    date_subscribed = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['subscriber', 'subscribee']

    def __str__(self):
        return f"{self.subscriber.username} subscribed to {self.subscribee.username}"
