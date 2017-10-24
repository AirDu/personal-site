from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'tags', 'category', 'editor', 'publish_time', 'modify_time', 'access_count')


admin.site.register(Article, ArticleAdmin)
