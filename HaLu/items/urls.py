# coding:utf-8

from django.conf.urls import url
from items import views
#from Haru import settings

urlpatterns =[
    #作品一覧
    url(r'^', views.Item.as_view(), name='index'),
    url(r'^PhantomCastle', views.Item.as_view(), name='PhantomCastle'),
]