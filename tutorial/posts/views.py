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
class PostList(generics.ListModelMixin,mixins.CreateModelMixin,mixins.GenericAPIView):
    queryset=Post.objects.all()
    serializerclass=PostSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)  


  


class PostDetail(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    queryset=Post.objects.all()
    serializerclass=PostSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

