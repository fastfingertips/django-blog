from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404
from article.models import Article, Comment

from .forms import RegisterForm, LoginForm

User = get_user_model()

# Create your views here.

# not auth
def register(request):
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
    messages.success(request, f'Hoşgeldin {new_user.username}')
    
    # Redirect to index page
    return redirect('index')
  context = {'form': form,}
  return render(request, 'user/register.html', context)

def user_login(request):
  form = LoginForm(request.POST or None)
  context = {'form': form,}
 
  if form.is_valid():
    username = form.cleaned_data.get('username')
    password = form.cleaned_data.get('password')

    user = authenticate(username=username, password=password)


    if user is None: # If user is not authenticated
      messages.error(request, 'Kullanıcı adı veya parola hatalı!')
      return render(request, 'user/login.html', context) 
    
    # Login user
    login(request, user)
    messages.success(request, f'Hoşgeldin {user.username}')
    return redirect('index') # Redirect to index page

  # If form is not valid
  return render(request, 'user/login.html', context)

def user_profile(request, id=None, username=None):
  if id:
    user = get_object_or_404(User, id=id)
  elif username == 'me':
    if not request.user.is_authenticated:
      messages.error(request, 'Bu sayfayı görüntülemek için giriş yapmalısınız.')
      return redirect('login')
    user = request.user
  else:
    user = get_object_or_404(User, username=username)

  return render(request, 'user/profile.html', {'user': user})

def user_articles(request, username):
  user = get_object_or_404(User, username=username)
  articles = Article.objects.filter(author=user)
  context = {'articles': articles, 'user': user}
  return render(request, 'user/user_articles.html', context)

def search(request, query=None):
  if query is None: # not in search/<str:query>
    query = request.GET.get('q') # get search/?q=query

  if not query:
    messages.error(request, 'Arama sorgusu boş girildi.')
    return redirect(request.META.get('HTTP_REFERER', 'index'))

  users = User.objects.filter(username__icontains=query)
  titles = Article.objects.filter(title__icontains=query)
  contents = Article.objects.filter(content__icontains=query)
  comments = Comment.objects.filter(comment_content__icontains=query)

  context = {
    'query': query,
    'users': users,
    'titles': titles,
    'contents': contents,
    'comments': comments 
  }

  return render(request, 'search.html', context)

# auth

@login_required(login_url='login')
def user_logout(request):
  logout(request)
  messages.success(request, 'Başarıyla çıkış yaptınız.')
  return redirect('index')

@login_required(login_url='login')
def dashboard(request):
    logned_user = request.user
    user_is_superuser = logned_user.is_superuser

    articles = Article.objects.filter(author=logned_user)
    comments = Comment.objects.filter(comment_author=logned_user)

    context = {
      'user': logned_user,
      'user_is_superuser': user_is_superuser,
      'articles': articles,
      'comments': comments
    }

    return render(request, 'dashboard.html', context)

@login_required(login_url='login')
def user_settings(request):
  return render(request, 'user/user_settings.html')