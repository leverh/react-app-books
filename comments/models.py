from django.db import models
from django.conf import settings
from reviews.models import Review

class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment_text = models.TextField()

    def __str__(self):
        return f"Comment by {self.user.username} on {self.review.book.title}"
