from rest_framework import serializers
from django.contrib.auth import get_user_model
from community.models import Article
from movies.models import Movie, Review
# from movies.serializers import ReviewSerializer

class ProfileSerializer(serializers.ModelSerializer):

    class ArticleSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Article
            fields = '__all__'

    class ReviewSerializer(serializers.ModelSerializer):

        class MovieSerializer(serializers.ModelSerializer):

            class Meta:
                model = Movie
                fields = ('pk', 'title', 'poster_url',)
        
        movie = MovieSerializer(read_only=True)

        
        class Meta:
            model = Review
            fields = ('movie','vote_rate',)
            read_only_fields = ('movie', 'vote_rate',)

    like_articles = ArticleSerializer(many=True)
    articles = ArticleSerializer(many=True)
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'email', 'like_articles', 'articles', 'reviews',)
