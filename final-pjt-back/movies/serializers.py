from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Movie
from .models import Review

User = get_user_model()

class ReviewSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ('pk', 'user', 'content', 'movie', 'vote_rate',)
        read_only_fields = ('movie', )

class MovieSerializer(serializers.ModelSerializer):

    review_set = ReviewSerializer(many=True, read_only=True)
    review_count = serializers.IntegerField(
        source='review_set.count', read_only=True
    )
    # vote_average = serializers.FloatField()

    class Meta:
        model = Movie
        fields = '__all__'


class MovieListSerializer(serializers.ModelSerializer):

    review_set = ReviewSerializer(many=True, read_only=True)
    review_count = serializers.IntegerField(
        source='review_set.count', read_only=True
    )
    # vote_average = serializers.FloatField()

    class Meta:
        model = Movie
        fields = '__all__'
