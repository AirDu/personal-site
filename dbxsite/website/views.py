# coding=utf-8
import json

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Article, Tag, Category, Editor


def index(request):
    hot_articles = Article.objects.all().filter(status=1).order_by('-access_count')[:6]
    latest_articles = Article.objects.all().filter(status=1).order_by('publish_time')[:6]
    return render(request, 'website/index.html', {'hot_articles': hot_articles, 'latest_articles': latest_articles})


def article_list_page(request):
    tag_id = request.GET.get('tag', '')
    if tag_id:
        articles = Article.objects.filter(tags__id=tag_id, status=1)
    else:
        articles = Article.objects.filter(status=1)
    tags = Tag.objects.filter(status=1)
    categories = Category.objects.filter(status=1)
    return render(request, 'website/article_list_page.html', {'articles': articles, 'tags': tags,
                                                              'categories': categories, 'article_stats': 1})


@login_required
def draft_list_page(request):
    articles = Article.objects.all().filter(status=0)
    tags = Tag.objects.all().filter(articles__status=0)
    categories = Category.objects.all().filter(articles__status=0)
    return render(request, 'website/article_list_page.html', {'articles': articles, 'tags': tags,
                                                              'categories': categories, 'article_stats': 0})


def article_page(request, article_id):
    article = Article.objects.get(pk=article_id)
    article.access_count += 1
    article.save()
    return render(request, 'website/article_page.html', {'article': article})


def column_page(request):
    return render(request, 'website/column_page.html')


@login_required
def article_edit_page(request, article_id):
    editor = request.GET.get('editor', '')
    tags = list(Tag.objects.values('id', 'name'))
    tags = json.dumps(tags)
    article_tags = []
    if article_id == '0':
        try:
            editor = Editor.objects.get(name=editor)
        except Exception as e:
            editor = Editor.objects.get(name='Summernote')
        return render(request, 'website/article_edit_page.html', {'article_id': 0, 'editor': editor, 'tags': tags,
                                                                  'article_tags': article_tags})
    article = get_object_or_404(Article, pk=article_id)
    if article.tags:
        article_tags = list(article.tags.values('id', 'name'))
        article_tags = json.dumps(article_tags)
    try:
        editor = Editor.objects.get(name=editor)
    except Exception as e:
        editor = article.editor
    return render(request, 'website/article_edit_page.html', {'article': article, 'article_id': article.id,
                                                              'editor': editor, 'tags': tags,
                                                              'article_tags': article_tags})


@login_required
def edit_action(request):
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    article_id = request.POST.get('article_id', '0')
    editor = request.POST.get('editor', 'Summernote')
    tags = request.POST.get('tags', '')
    submit_stat = request.POST.get('submit_stat', '0')

    if article_id == '0':
        article = Article.objects.create(title=title, content=content)
    else:
        article = Article.objects.get(pk=article_id)
    editor = Editor.objects.get(name=editor)
    if tags:
        tags = Tag.objects.filter(pk__in=tags.split(','))
        article.tags = tags
    else:
        article.tags.clear()
    article.title = title
    article.content = content
    article.editor = editor
    article.status = submit_stat
    article.save()
    return HttpResponseRedirect(reverse('article:article_page', args=[article.id]))

