"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from article import views as article_views
from django.conf import settings
from django.conf.urls.static import static
from user import views as user_views

urlpatterns = [
    # admin
    path('admin/', admin.site.urls, name='admin'),
    path('settings/', user_views.user_settings, name='settings'),

    # paths
    path('', article_views.index, name='index'),
    path('about/', article_views.about, name='about'),

    path('register/', user_views.register, name='register'),
    path('login/', user_views.user_login, name='login'),

    # search
    path('search/', user_views.search, name='search'),
    path('search/<str:query>', user_views.search, name='search'),

    # includes
    path('articles/',include('article.urls')),
    path('user/', include('user.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)