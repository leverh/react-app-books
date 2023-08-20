from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn_number = models.CharField(max_length=13, unique=True)
    summary = models.TextField(null=True, blank=True)
    cover_image = models.ImageField(upload_to='book_covers/', null=True, blank=True)
    
    def __str__(self):
        return self.title
