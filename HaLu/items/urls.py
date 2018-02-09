# coding:utf-8

from django.conf.urls import url
from items import views
#from Haru import settings

urlpatterns =[
    #作品一覧
    url(r'^$', views.Item.as_view(), name='index'),
    url(r'detail/(?P<pk>[0-9]+)/$', views.ItemDetailView.as_view(), name='detail'),
]