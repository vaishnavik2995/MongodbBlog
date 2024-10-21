from django.urls import path, include
from . import views
from .views import *
from rest_framework.routers import DefaultRouter
from django.contrib import admin


router = DefaultRouter()
router.register('category', CategoryView, basename='category')
router.register('user', CustomUserView , basename='user')
router.register('post', PostView, basename='post')
router.register('comment', CommentView, basename='comment')



urlpatterns = [
    path('', include(router.urls))
]
