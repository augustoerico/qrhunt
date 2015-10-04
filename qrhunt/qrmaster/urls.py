from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.do_login, name='login'),
    url(r'^logout/$', views.do_logout, name='logout'),
    url(r'^quests/(?P<pk>[0-9]+)/$', views.quest, name='quest'),
    url(r'^quest/create/$', views.quest_create, name='quest_create'),
    url(r'^quests/(?P<pk>[0-9]+)/delete/$', views.quest_delete, name='quest_delete'),
    url(r'^quests/(?P<pk>[0-9]+)/edit/$', views.quest_edit, name='quest_edit'),
    url(r'^hints/(?P<pk>[0-9a-z]+)/$', views.hint, name='hint'),
    url(r'^hints/(?P<pk>[0-9a-z]+)/delete/$', views.hint_delete, name='hint_delete'),
    url(r'^hints/(?P<pk>[0-9a-z]+)/edit/$', views.hint_edit, name='hint_edit'),
    url(r'^quests/(?P<quest_pk>[0-9]+)/hint/create$', views.hint_create, name='hint_create'),
    url(r'^account/create/$', views.account_create, name='account_create'),
]