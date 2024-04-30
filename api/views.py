from django.shortcuts import render
from .models import BlogPost
from rest_framework import generics
from .serializers import BlogPostSerializer

# Create your views here.


class BlogPostListCreate(generics.ListCreateAPIView):

    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
