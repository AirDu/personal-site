# coding=utf-8
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Article


def index(request):
    hot_articles = Article.objects.all().order_by('-access_count')[:10]
    latest_articles = Article.objects.all().order_by('publish_time')[:10]
    return render(request, 'website/index.html', {'hot_articles': hot_articles, 'latest_articles': latest_articles})


def article_list_page(request):
    articles = Article.objects.all()
    return render(request, 'website/article_list_page.html', {'articles': articles})


def article_page(request, article_id):
    article = Article.objects.get(pk=article_id)
    article.access_count += 1
    article.save()
    return render(request, 'website/article_page.html', {'article': article})


def article_edit_page(request, article_id):
    if article_id == '0':
        return render(request, 'website/article_edit_page.html')
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'website/article_edit_page.html', {'article': article})


def edit_action(request):
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    article_id = request.POST.get('article_id', '0')

    if article_id == '0':
        article = Article.objects.create(title=title, content=content)
    else:
        article = Article.objects.get(pk=article_id)
        article.title = title
        article.content = content
        article.save()
    return HttpResponseRedirect(reverse('article:article_page', args=[article.id]))
