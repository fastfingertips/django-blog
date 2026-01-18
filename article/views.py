from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    TemplateView, 
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView,
    View
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Article, Comment
from .forms import ArticleForm

class IndexView(TemplateView):
    template_name = 'index.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class ArticleListView(ListView):
    model = Article
    template_name = 'articles.html'
    context_object_name = 'articles'
    ordering = ['-created_at']

    def get_queryset(self):
        return Article.objects.filter(visibility=True).order_by('-created_at')

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article/article_detail.html'
    context_object_name = 'article'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not self.object.visibility:
            if not request.user.is_authenticated or request.user != self.object.author:
                messages.error(request, 'Article is not visible')
                return redirect('article_urls:articles')
        return super().get(request, *args, **kwargs)

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article/article_add.html'
    success_url = reverse_lazy('index')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Article has been added')
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article/article_update.html'
    pk_url_kwarg = 'id'
    login_url = 'login'

    def test_func(self):
        article = self.get_object()
        return self.request.user == article.author

    def get_success_url(self):
        return reverse('article_urls:article_detail', kwargs={'id': self.object.id})

    def form_valid(self, form):
        messages.success(self.request, 'Article has been updated')
        return super().form_valid(form)

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('index')
    login_url = 'login'

    def test_func(self):
        article = self.get_object()
        return self.request.user == article.author

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Article has been deleted')
        return super().delete(request, *args, **kwargs)

    # We allow GET to delete if you want, but standard DeleteView expects POST.
    # The original FBV allowed direct navigation to delete URL.
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

class ArticleVisibilityToggleView(LoginRequiredMixin, UserPassesTestMixin, View):
    login_url = 'login'

    def test_func(self):
        article = get_object_or_404(Article, id=self.kwargs['id'])
        return self.request.user == article.author

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=self.kwargs['id'])
        article.visibility = not article.visibility
        article.save()
        messages.success(request, f'Article visibility has been changed to {article.visibility}')
        return redirect(request.META.get('HTTP_REFERER', 'index'))

class CommentCreateView(LoginRequiredMixin, View):
    login_url = 'login'

    def post(self, request, id):
        article = get_object_or_404(Article, id=id)
        content = request.POST.get('comment_content')
        if content:
            Comment.objects.create(
                article=article,
                comment_author=request.user,
                comment_content=content
            )
            messages.success(request, 'Comment has been added')
        return redirect('article_urls:article_detail', id=id)