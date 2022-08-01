from django.shortcuts import render
from django.urls import is_valid_path
from posts.models import Post
from posts.serializers import PostSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins
from rest_framework import generics

# Get all Posts 
# Create all posts 
class PostList(generics.ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer



  


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer


