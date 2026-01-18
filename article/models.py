from ckeditor.fields import RichTextField
from django.conf import settings
from django.db import models
from django.db.models.functions import Now

# Create your models here.


class Article(models.Model):
    objects: models.Manager  # Type hint for IDE
    comments: models.Manager  # Type hint for related manager

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Author')
    title = models.CharField(max_length=50, verbose_name='Article Title')
    content = RichTextField()
    created_at = models.DateTimeField(db_default=Now(), verbose_name='Created At')
    article_image = models.FileField(blank=True, null=True, verbose_name='Article Image')
    visibility = models.BooleanField(verbose_name='Article Visibility', default=True)

    def __str__(self) -> str:
        return f'{self.author} - {self.title}'


class Comment(models.Model):
    objects: models.Manager  # Type hint for IDE

    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Article', related_name='comments')
    comment_author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Comment Author'
    )
    comment_content = models.CharField(max_length=200, verbose_name='Comment Content')
    comment_date = models.DateTimeField(db_default=Now(), verbose_name='Comment Date')

    def __str__(self) -> str:
        return f'{self.comment_author} - {self.comment_content}'
