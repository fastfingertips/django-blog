from django.urls import path
from . import views as user_views

app_name = 'user_urls'

urlpatterns = [
  path('dashboard/', user_views.dashboard, name='dashboard'),

  path('logout/', user_views.user_logout, name='logout'),

  path('<int:id>/', user_views.user_profile, name='profile'),
  path('<str:username>/', user_views.user_profile, name='profile'),
  
  path('<str:username>/', user_views.user_profile, name='username_profile'),
  path('<str:username>/articles/', user_views.user_articles, name='articles'),
]