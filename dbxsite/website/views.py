# coding=utf-8
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Article


def index(request):
    articles = Article.objects.all()
    return render(request, 'website/index.html', {'articles': articles})


def article_page(request, article_id):
    article = Article.objects.get(pk=article_id)
    return render(request, 'website/article_page.html', {'article': article})


def article_edit_page(request, article_id):
    if article_id == '0':
        return render(request, 'website/article_edit_page.html')
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'website/article_edit_page.html', {'article': article})
