from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_list, name="movie_list"),
    path('<int:movie_pk>/', views.movie_detail, name="movie_detail"),
    path('<int:movie_pk>/reviews/', views.create_review, name="create_review"),
    path('<int:movie_pk>/reviews/<int:review_pk>/', views.review_update_or_delete, name="review_update_or_delete"),
    # path('<str:movie_name>/', views.),  # search
    # path('<int:person_pk>/', views.),
    # path('recommend/weathcer_rec/', views.),
    # path('recommend/random_rec/', views.),
    # path('ranking/like/', views.),
    # path('ranking/new/', views.),
    # path('ranking/community/', views.),
]
