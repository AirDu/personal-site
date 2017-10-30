from django.contrib import admin
from .models import Article, Tag, Category, Editor


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'tag', 'category', 'editor', 'publish_time', 'modify_time', 'access_count')

    def tag(self, obj):
        return ', '.join([i[1] for i in obj.tags.values_list()])

    def category(self, obj):
        return obj.categories


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class EditorAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Editor, EditorAdmin)

