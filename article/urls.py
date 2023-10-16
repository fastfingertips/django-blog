from django.contrib import admin
from django.urls import path
from . import views as article_views

app_name = 'article_urls'

urlpatterns = [
  path('', article_views.articles, name='articles'),
  path('article/comment/<int:id>/', article_views.comment, name='comment'),
  path('article/add/', article_views.add, name='article_add'),
  path('article/<int:id>/', article_views.detail, name='article_detail'),
  path('article/<int:id>/visibility/', article_views.article_visibility, name='article_visibility'),
  path('article/<int:id>/delete/', article_views.delete, name='article_delete'), 
  path('article/<int:id>/update/', article_views.update, name='article_update'),
]