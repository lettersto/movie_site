from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Movie, Review, Actor, Genre, Director

User = get_user_model()

class ReviewSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ('pk', 'user', 'content', 'movie', 'vote_rate', 'created_at', 'updated_at')
        read_only_fields = ('movie', )

class MovieSerializer(serializers.ModelSerializer):

    class ActorName(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('name',)

    class DirectorName(serializers.ModelSerializer):
        class Meta:
            model = Director
            fields = ('name',)
    
    class GenreName(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('name',)

    def votesAverage(self, obj):
        length = obj.reviews.count()
        if length != 0:
            total = 0
            for review in obj.reviews.all():
                total += review.vote_rate
            result = round(total/length, 2)
        else:
            result = 0
        return result

    vote_average = serializers.SerializerMethodField('votesAverage')
    reviews = ReviewSerializer(many=True, read_only=True)
    review_count = serializers.IntegerField(
        source='reviews.count', read_only=True
    )
    actor = ActorName(many=True, read_only=True)
    director = DirectorName(many=True, read_only=True)
    genres = GenreName(many=True, read_only=True)
    # vote_average = serializers.FloatField()

    class Meta:
        model = Movie
        fields = '__all__'


class MovieListSerializer(serializers.ModelSerializer):

    def votesAverage(self, obj):
        length = obj.reviews.count()
        if length != 0:
            total = 0
            for review in obj.reviews.all():
                total += review.vote_rate
            result = round(total/length, 2)
        else:
            result = 0
        return result

    vote_average = serializers.SerializerMethodField('votesAverage')

    class Meta:
        model = Movie
        fields = '__all__'