from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.db.models import Count
# from django.core.paginator import Paginator

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Article, Comment, ArticleView
from .serializers import (
    ArticleListSerializer, ArticleSerializer, 
    CommentSerializer
)

@api_view(['GET', 'POST'])
def article_list_or_create(request):

    def article_list():
        articles = Article.objects.annotate(
            comment_count=Count('comments', distinct=True),
            like_count=Count('user_like', distinct=True),
            view_count=Count('article_views', distinct=True)
        ).order_by('-pk')
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    
    def create_article():
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'GET':
        return article_list()
    elif request.method == 'POST':
        return create_article()


# community articles paginator
# @api_view(['GET'])
# def article_paginator(request):
#     articles = Article.objects.annotate(
#             comment_count=Count('comments', distinct=True),
#             like_count=Count('user_like', distinct=True),
#             view_count=Count('article_views', distinct=True)
#         ).order_by('-pk')
#     paginator = Paginator(articles, 10)

#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)

#     serializer = ArticleListSerializer(page_obj, many=True)

#     return Response(serializer.data)



@api_view(['GET', 'PUT', 'DELETE'])
def article_detail_or_update_or_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)


    def article_detail():
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def update_article():
        if request.user == article.user:
            serializer = ArticleSerializer(instance=article, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)

    def delete_article():
        if request.user == article.user:
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        return article_detail()
    elif request.method == 'PUT':
        if request.user == article.user:
            return update_article()
    elif request.method == 'DELETE':
        if request.user == article.user:
            return delete_article()


@api_view(['POST'])
def like_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    user = request.user
    if article.user_like.filter(pk=user.pk).exists():
        article.user_like.remove(user)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    else:
        article.user_like.add(user)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)


@api_view(['POST'])
def create_comment(request, article_pk):
    user = request.user
    article = get_object_or_404(Article, pk=article_pk)
    
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article, user=user)
        comments = article.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def comment_update_or_delete(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    def update_comment():
        if request.user == comment.user:
            serializer = CommentSerializer(instance=comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                comments = article.comments.all()
                serializer = CommentSerializer(comments, many=True)
                return Response(serializer.data)

    def delete_comment():
        if request.user == comment.user:
            comment.delete()
            comments = article.comments.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)
    
    if request.method == 'PUT':
        return update_comment()
    elif request.method == 'DELETE':
        return delete_comment()


@api_view(['POST'])
def record_view(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if not ArticleView.objects.filter(
        article=article,
        user=request.user):

        view = ArticleView(article=article,
                        ip=request.META['REMOTE_ADDR'],
                        user=request.user)
        view.save()
    
    view_count = ArticleView.objects.filter(article=article).count()
    
    context = {
        'viewCount': view_count
    }

    return JsonResponse(context)
