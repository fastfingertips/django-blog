from typing import Any, cast

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
    View,
)

from user.models import User

from .forms import ArticleForm
from .models import Article, Comment


class IndexView(TemplateView):
    template_name: str = 'index.html'


class AboutView(TemplateView):
    template_name: str = 'about.html'


class ArticleListView(ListView):
    model = Article
    template_name: str = 'articles.html'
    context_object_name: str = 'articles'
    ordering: list[str] = ['-created_at']

    def get_queryset(self) -> Any:
        return Article.objects.filter(visibility=True).order_by('-created_at')


class ArticleDetailView(DetailView):
    model = Article
    template_name: str = 'article/article_detail.html'
    context_object_name: str = 'article'
    pk_url_kwarg: str = 'id'
    object: Article

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        return context

    def get(self, request: Any, *args: Any, **kwargs: Any) -> HttpResponse:
        self.object = self.get_object()
        if not self.object.visibility:
            user = cast(User, request.user)
            if not user.is_authenticated or user != self.object.author:
                messages.error(request, 'Article is not visible')
                return redirect('article_urls:articles')
        return super().get(request, *args, **kwargs)


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name: str = 'article/article_add.html'
    success_url = reverse_lazy('index')
    login_url: str = 'login'

    def form_valid(self, form: ArticleForm) -> HttpResponse:
        user = cast(User, self.request.user)
        form.instance.author = user
        messages.success(self.request, 'Article has been added')
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name: str = 'article/article_update.html'
    pk_url_kwarg: str = 'id'
    login_url: str = 'login'
    object: Article

    def test_func(self) -> bool:
        article = cast(Article, self.get_object())
        user = cast(User, self.request.user)
        return user == article.author

    def get_success_url(self) -> str:
        article_id = getattr(self.object, 'id', self.object.pk)
        return reverse('article_urls:article_detail', kwargs={'id': article_id})

    def form_valid(self, form: ArticleForm) -> HttpResponse:
        messages.success(self.request, 'Article has been updated')
        return super().form_valid(form)


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    pk_url_kwarg: str = 'id'
    success_url = reverse_lazy('index')
    login_url: str = 'login'

    def test_func(self) -> bool:
        article = cast(Article, self.get_object())
        user = cast(User, self.request.user)
        return user == article.author

    def delete(self, request: Any, *args: Any, **kwargs: Any) -> Any:
        messages.success(self.request, 'Article has been deleted')
        return super().delete(request, *args, **kwargs)

    def get(self, request: Any, *args: Any, **kwargs: Any) -> Any:
        return self.delete(request, *args, **kwargs)


class ArticleVisibilityToggleView(LoginRequiredMixin, UserPassesTestMixin, View):
    login_url: str = 'login'

    def test_func(self) -> bool:
        article = get_object_or_404(Article, id=self.kwargs['id'])
        user = cast(User, self.request.user)
        return user == article.author

    def get(self, request: Any, *args: Any, **kwargs: Any) -> HttpResponse:
        article = get_object_or_404(Article, id=self.kwargs['id'])
        article.visibility = not article.visibility
        article.save()
        messages.success(request, f'Article visibility has been changed to {article.visibility}')
        return redirect(request.META.get('HTTP_REFERER', 'index'))


class CommentCreateView(LoginRequiredMixin, View):
    login_url: str = 'login'

    def post(self, request: Any, id: int) -> HttpResponse:
        article = get_object_or_404(Article, id=id)
        content = request.POST.get('comment_content')
        if content:
            user = cast(User, request.user)
            Comment.objects.create(article=article, comment_author=user, comment_content=content)
            messages.success(request, 'Comment has been added')
        return redirect('article_urls:article_detail', id=id)
