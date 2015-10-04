from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.do_login, name='login'),
    url(r'^logout/$', views.do_logout, name='logout'),
    url(r'^quests/(?P<pk>[0-9]+)/$', views.quest, name='quest'),
    url(r'^quest/create/$', views.quest_create, name='quest_create'),
    url(r'^hint/(?P<pk>[0-9a-z]+)/$', views.hint, name='hint'),
    url(r'^quests/(?P<quest_pk>[0-9]+)/hint/create$', views.hint_create, name='hint_create'),
]