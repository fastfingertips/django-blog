from django.shortcuts import (
  render,
  redirect,
  get_object_or_404
)
from django.contrib import messages

from .models import Article, Comment
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
  return render(request, 'index.html')

def about(request):
  return render(request, 'about.html')

def articles(request):
  # descending: -created_at, ascending: created_at
  articles = Article.objects.all().order_by('-created_at')

  visible_articles = articles.filter(visibility=True).all()

  context = {
    'articles': visible_articles
  }
  return render(request, 'articles.html', context)

def detail(request, id):
  referer = request.META.get('HTTP_REFERER') # get the previous page url

  try:
    # try to get the article with the given id
    article = Article.objects.get(id=id)
  except Article.DoesNotExist:
    # if not found, show an error message and redirect
    messages.error(request, f'Article not found with id {id}')
    return redirect(referer or 'index')
  
  if not article.visibility:
    if not request.user.is_authenticated or request.user != article.author:
      messages.error(request, 'Article is not visible')
      return redirect(referer or 'index')

  context = {
    'article': article,
    'comments': article.comments.all() # related_name
    }

  return render(request, 'article/article_detail.html', context)

@login_required(login_url='login')
def add(request):
  form = ArticleForm(
    request.POST or None,
    request.FILES or None
    )

  if form.is_valid():
    # commit=False means don't save to database yet
    article = form.save(commit=False)
    # set the author to the current user
    article.author = request.user
    article.save()
    messages.success(request, 'Article has been added')
    return redirect('index')

  return render(request, 'article/article_add.html', {'form': form})

@login_required(login_url='login')
def delete(request, id):
  article = get_object_or_404(Article, id=id)
  article.delete()
  messages.success(
    request,
    'Article has been deleted')

  referer = request.META.get('HTTP_REFERER')
  return redirect(referer or 'index')

@login_required(login_url='login')
def update(request, id):
  article = get_object_or_404(Article, id=id)

  form = ArticleForm(
    request.POST or None,
    request.FILES or None,
    instance=article
  )
  
  if form.is_valid():
    # commit=False means don't save to database yet
    article = form.save(commit=False)
    article.author = request.user
    article.save()
    messages.success(request, 'Article has been updated')
    return redirect('article_urls:article_detail', id=id)
  
  return render(request, 'article/article_update.html', {'form': form})

@login_required(login_url='login')
def article_visibility(request, id):
  article = get_object_or_404(Article, id=id)
  article.visibility = not article.visibility
  article.save()
  messages.success(
    request,
    f'Article visibility has been changed to {article.visibility}'
  )

  referer = request.META.get('HTTP_REFERER')
  return redirect(referer or 'index')

def comment(request, id):
  article = get_object_or_404(Article, id=id)

  if request.method == 'POST':
    content = request.POST.get('comment_content')

    new_comment = Comment(
      article=article,
      comment_author=request.user,
      comment_content=content
    )
    new_comment.save()
    messages.success(request, 'Comment has been added')
  return redirect('article_urls:article_detail', id=id)