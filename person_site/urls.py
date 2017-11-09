from django.conf.urls import url

from person_site import views

urlpatterns = [
    # Домашняя страница
    url(r'^$', views.index, name='index'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^articles/$', views.articles, name='articles'),
    url(r'^articles/new_article/$', views.new_article, name='new_article'),
    url(r'^article/(?P<article_id>\d+)/$', views.article, name='article'),
]