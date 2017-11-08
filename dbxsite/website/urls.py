from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<article_id>[0-9]+)/$', views.article_page, name='article_page'),
    url(r'^edit/(?P<article_id>[0-9]+)/$', views.article_edit_page, name='article_edit_page'),
    url(r'^edit/action$', views.edit_action, name='edit_action'),
    url(r'^list/$', views.article_list_page, name='article_list_page'),
    url(r'^draft/$', views.draft_list_page, name='draft_list_page'),
    url(r'^column/$', views.column_page, name='column_page')
]
