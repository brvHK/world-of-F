# coding:utf-8

from django.conf.urls import url
from items import views
#from Haru import settings

urlpatterns =[
    #作品一覧
    url(r'^PhantomCastle', views.Item.as_view(), name='PhantomCastle'),
    #url(r'^', views.index, name="index"),
    #url(r'^img/(?P<path>.*)$','django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
]