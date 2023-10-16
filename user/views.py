from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from article.models import Article, Comment

from .forms import RegisterForm, LoginForm

# Create your views here.

# not auth
def register(request):
  form = RegisterForm(request.POST or None)
  if form.is_valid():
    username = form.cleaned_data.get('username')
    password = form.cleaned_data.get('password')

    # Create user
    newUser = User(username=username)
    newUser.set_password(password)
    newUser.save()

    # Login user
    login(request, newUser)
    messages.success(request, f'Hoşgeldin {newUser.username}')

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

    # Authenticate user
    """
    authenticate: checks the username and password and returns a user 
    object if they are correct or None if they are not.
    """
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
  referer = request.META.get('HTTP_REFERER')
  # request_path = request.path
  user_exists = True

  if id is not None:
    try:
      user = User.objects.get(id=id)
    except User.DoesNotExist: user_exists = False
  elif username is not None:
    if username == 'me': # logged in user profile
      if not request.user.is_authenticated:
        messages.error(request, 'Bu sayfayı görüntülemek için giriş yapmalısınız.')
        return redirect('login')
      user = request.user
    else:
      try:
        user = User.objects.get(username=username)
      except User.DoesNotExist: user_exists = False
    
  if not user_exists:
    messages.error(request, 'Kullanıcı bulunamadı.')
    if referer is not None:
      return redirect(referer)
    return redirect('index')

  context = {'user': user}
  return render(request, 'user/profile.html', context)

def user_articles(request, username):
  try:
    user = User.objects.get(username=username)
  except User.DoesNotExist:
    messages.error(request, 'Kullanıcı bulunamadı.')
    return redirect('index')

  articles = Article.objects.filter(author=user)
  context = {'articles': articles, 'user': user}
  return render(request, 'user/user_articles.html', context)

def search(request, query=None):
  if query is None: # not in search/<str:query>
    query = request.GET.get('q') # get search/?q=query

    """
    # search/?q=query -> search/query
    if query is not None: 
      return redirect(request.path + query)
    """

  if query is None or len(query) == 0:

    messages.error(request, 'Arama sorgusu boş girildi.')
    referer = request.META.get('HTTP_REFERER')

    if referer is not None:
      return redirect(referer)

    return render(request, 'search.html', {'query': query})

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