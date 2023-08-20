from django.conf import settings
from django.db import models
from books.models import Book

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.PositiveIntegerField()

    def __str__(self):
        return f"Review of {self.book.title} by {self.user.username}"
