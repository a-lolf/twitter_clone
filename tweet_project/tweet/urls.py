from django.urls import path
from . import views

urlpatterns = [
    path('', views.some_view, name='some_view'),
    path('tweet_list/', views.tweet_list, name='tweet_list'),
    path('tweet_create/', views.tweet_create, name='tweet_create'),
    path('<int:tweet_id>/tweet_edit/', views.tweet_edit, name='tweet_edit'),
    path('<int:tweet_id>/tweet_delete/', views.tweet_delete, name='tweet_delete'),
    path('register/', views.register, name='register'),
]