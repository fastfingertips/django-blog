  """
  article = get_object_or_404(Article, id=id)
  """

  """
  or use filter and add .first() to get the first object

  article = Article.objects.filter(id=id)
  if not article:
    return HttpResponse(f'Article not found with id {id}')
  """