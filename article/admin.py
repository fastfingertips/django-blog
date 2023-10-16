from django.contrib import admin

from .models import Article, Comment

# Register your models here.
admin.site.register(Comment)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
  # show these fields in the admin panel
  list_display = ['title', 'author', 'created_at'] 

  # make these fields clickable
  list_display_links = ['title', 'created_at']

  # search by these fields
  search_fields = ['title', 'content'] 

  # filter by these fields
  list_filter = ['created_at']

  class Meta:
    model = Article

