# blog_app_admin/serializers.py

from .models import Post, Comment
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'published_date']

class CommentSerializer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'text', 'created_date']
