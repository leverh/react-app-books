from rest_framework import generics
from .models import Comment
from .serializers import CommentSerializer
from reviews.models import Review

class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = CommentSerializer
