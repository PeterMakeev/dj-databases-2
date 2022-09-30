from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article, Tag


def articles_list(request):
    template = 'articles/news.html'
    articles = Article.objects.all()
    context = {'object_list': articles}

    return render(request, template, context)
