from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Article(models.Model):
  author = models.ForeignKey(
    'auth.User',
    on_delete=models.CASCADE,
    verbose_name='Author'
    ) # if user is deleted, delete the article
  
  created_at = models.DateTimeField(
    auto_now_add=True, # when the article is created, set the date and time 
    verbose_name='Created At'
    )

  title = models.CharField(
    max_length=50,
    verbose_name='Title'
    ) # max length of 50 characters
  content = RichTextField(
    verbose_name='Content'
    ) # no max length

  article_image = models.FileField(
    blank=True,
    null=True,
    verbose_name='Article Image'
    )

  visibility = models.BooleanField(
    default=True,
    verbose_name='Article Visibility'
    )

  def __str__(self):
    return f'{self.author} - {self.title}'
  
  class Meta:
    ordering = ['-created_at'] # order by created_at descending
  
class Comment(models.Model):
  article = models.ForeignKey(
    Article,
    on_delete=models.CASCADE,
    verbose_name='Article',
    related_name='comments' # to access comments from article object
    )
  comment_author = models.CharField(
    'auth.User',
    max_length=50,
    )
  comment_content = models.CharField(
    max_length=200,
    verbose_name='Comment'
    )
  comment_date = models.DateTimeField(
    auto_now_add=True,
    verbose_name='Comment Date'
    )
  
  def __str__(self):
    return self.comment_content
  
  class Meta:
    ordering = ['-comment_date'] # order by created_at descending