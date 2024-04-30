from django.shortcuts import render
from .models import BlogPost
from rest_framework import generics, status
from .serializers import BlogPostSerializer
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.views import APIView

# Create your views here.
class BlogPostList(APIView):
    def get(self,request,format=None):

        title = request.query_params.get("title")
        if title:
            blog_posts = BlogPost.objects.filter(title__contains=title)
        else:
            blog_posts = BlogPost.objects.all()

        serializer = BlogPostSerializer(blog_posts,many=True)


        return Response(serializer.data,status=status.HTTP_200_OK)


class BlogPostListCreate(generics.ListCreateAPIView):

    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    def delete(self,request,*args,**kwargs):
        # BlogPost.objects.filter(id=5).delete()
        BlogPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # def update(self):
    #
    #     return True
    #
    # def get(self):
    #
    #     return True


class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = "pk"



