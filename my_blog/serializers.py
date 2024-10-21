from rest_framework import serializers
from .models import CustomUser, Category, Post, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    auther = CustomUserSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    post = PostSerializer(many=True, read_only=True)
    auther = CustomUserSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
