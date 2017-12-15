# coding:utf-8

from django.conf.urls import url
from django.conf.urls import include
from story import views

urlpatterns =[
    #作品一覧
    url(r'^$', views.IndexView.as_view(), name='Index'),
    url(r'^prologue$', views.IndexView.as_view(), name='Index'),
    url(r'^prologue/1st', views.First.as_view(), name='First'),
    url(r'^prologue/2nd', views.Second.as_view(), name='Second'),
    url(r'^prologue/3rd', views.IndexView.as_view(), name='Third'),
    #url(r'^main/$', views.MainView.as_view(), name='Main'),
    #url(r'^main/$', include('contents.urls'), name='Main'),
]