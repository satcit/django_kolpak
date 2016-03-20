from django.conf.urls import url

from . import views

app_name = 'mainapp'
urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^articles/(?P<article_id>[0-9]+)/$', views.get_article, name="get_article"),
    url(r'^articles/$', views.get_articles, name="get_articles"),
    url(r'^articles/create/$', views.create_article, name="create_article"),
    url(r'^articles/(?P<article_id>[0-9]+)/edit/$', views.edit_article, name="edit_article"),
    url(r'^articles/(?P<article_id>[0-9]+)/comments/create$', views.create_article_comment, name="create_article_comment"),
    url(r'^articles/(?P<article_id>[0-9]+)/upload/', views.upload_article_file, name="upload_article_file"),

    url(r'^persons/(?P<person_id>[0-9]+)/$', views.get_person, name="get_person"),
    url(r'^persons/$', views.get_persons, name="get_persons"),
    url(r'^persons/create/$', views.create_person, name="create_person"),
    url(r'^persons/(?P<person_id>[0-9]+)/edit/$', views.edit_person, name="edit_person"),
    url(r'^persons/(?P<person_id>[0-9]+)/comments/create$', views.create_person_comment, name="create_person_comment"),

    url(r'^tasks/$', views.get_tasks, name='get_tasks'),
]
