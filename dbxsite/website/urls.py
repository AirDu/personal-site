from django.conf.urls import url
import views

urlpatterns = [
    url(r'^(?P<article_id>[0-9]+)/$', views.article_page, name='article_page'),
    url(r'^edit/(?P<article_id>[0-9]+)/$', views.article_edit_page, name='article_edit_page')
]
