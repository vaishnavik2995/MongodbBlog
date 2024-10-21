from django.shortcuts import render
from django.http import HttpResponse
from .serializers import CategorySerializer, CustomUserSerializer, PostSerializer, CommentSerializer
from rest_framework import viewsets
from .models import Category, CustomUser, Post, Comment
from rest_framework.response import Response


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CustomUserView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
