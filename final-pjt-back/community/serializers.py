from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Article, Comment


User = get_user_model()

class CommentSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('pk', 'user', 'content', 'article',)
        read_only_fields = ('article', )

class ArticleSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')


    comments = CommentSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    user_like = UserSerializer(read_only=True, many=True)
    article_views = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Article
        fields = (
            'pk', 'user', 'title', 
            'content', 'comments', 'user_like', 
            'created_at', 'updated_at', 'article_views'
        )


class ArticleListSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)
    comment_count = serializers.IntegerField()
    like_count = serializers.IntegerField()
    view_count = serializers.IntegerField()

    class Meta:
        model = Article
        fields = (
            'pk', 'user', 'title', 
            'comment_count', 'like_count', 'created_at',
            'view_count'
        )
