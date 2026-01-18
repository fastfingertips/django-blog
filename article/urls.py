from django.urls import path
from . import views

app_name = 'article_urls'

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='articles'),
    path('article/comment/<int:id>/', views.CommentCreateView.as_view(), name='comment'),
    path('article/add/', views.ArticleCreateView.as_view(), name='article_add'),
    path('article/<int:id>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('article/<int:id>/visibility/', views.ArticleVisibilityToggleView.as_view(), name='article_visibility'),
    path('article/<int:id>/delete/', views.ArticleDeleteView.as_view(), name='article_delete'), 
    path('article/<int:id>/update/', views.ArticleUpdateView.as_view(), name='article_update'),
]