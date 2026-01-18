from typing import Any, cast

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from article.models import Article, Comment

from .forms import LoginForm, RegisterForm
from .models import User

# Create your views here.


# not auth
def register(request: Any) -> HttpResponse:
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        # Create user
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()

        # Login user
        login(request, new_user)
        messages.success(request, f'Welcome {new_user.username}')

        # Redirect to index page
        return redirect('index')
    context = {'form': form}
    return render(request, 'user/register.html', context)


def user_login(request: Any) -> HttpResponse:
    form = LoginForm(request.POST or None)
    context = {'form': form}

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)

        if user is None:  # If user is not authenticated
            messages.error(request, 'Invalid username or password!')
            return render(request, 'user/login.html', context)

        # Login user
        login(request, user)
        messages.success(request, f'Welcome {user.username}')
        return redirect('index')  # Redirect to index page

    # If form is not valid
    return render(request, 'user/login.html', context)


def user_profile(request: Any, id: int | None = None, username: str | None = None) -> HttpResponse:
    user: User | None = None
    if id:
        user = get_object_or_404(User, id=id)
    elif username == 'me':
        temp_user = cast(User, request.user)
        if not temp_user.is_authenticated:
            messages.error(request, 'You must log in to view this page.')
            return redirect('login')
        user = temp_user
    else:
        user = get_object_or_404(User, username=username)

    articles = Article.objects.filter(author=user)
    return render(request, 'user/profile.html', {'user': user, 'articles': articles})


def user_articles(request: Any, username: str) -> HttpResponse:
    user = get_object_or_404(User, username=username)
    articles = Article.objects.filter(author=user)
    context = {'articles': articles, 'user': user}
    return render(request, 'user/user_articles.html', context)


def search(request: Any, query: str | None = None) -> HttpResponse:
    if query is None:  # not in search/<str:query>
        search_query = request.GET.get('q')  # get search/?q=query
    else:
        search_query = query

    if not search_query or not isinstance(search_query, str):
        messages.error(request, 'Search query cannot be empty.')
        return redirect(request.META.get('HTTP_REFERER', 'index'))

    users = User.objects.filter(username__icontains=search_query)
    titles = Article.objects.filter(title__icontains=search_query)
    contents = Article.objects.filter(content__icontains=search_query)
    comments = Comment.objects.filter(comment_content__icontains=search_query)

    context = {
        'query': search_query,
        'users': users,
        'titles': titles,
        'contents': contents,
        'comments': comments,
    }

    return render(request, 'search.html', context)


# auth


@login_required(login_url='login')
def user_logout(request: Any) -> HttpResponse:
    logout(request)
    messages.success(request, 'Successfully logged out.')
    return redirect('index')


@login_required(login_url='login')
def dashboard(request: Any) -> HttpResponse:
    logged_user = cast(User, request.user)
    user_is_superuser = logged_user.is_superuser

    articles = Article.objects.filter(author=logged_user)
    comments = Comment.objects.filter(comment_author=logged_user)

    context = {
        'user': logged_user,
        'user_is_superuser': user_is_superuser,
        'articles': articles,
        'comments': comments,
    }

    return render(request, 'dashboard.html', context)


@login_required(login_url='login')
def user_settings(request: Any) -> HttpResponse:
    return render(request, 'user/user_settings.html')
