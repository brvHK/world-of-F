# coding:utf-8

from django.conf.urls import url
from about import views
#from Haru import settings

urlpatterns =[
    #作品一覧
    url(r'^Artist/HaLu', views.HaLu.as_view(), name='HaLu'),
    url(r'^Artist/HK', views.Ken.as_view(), name='Ken'),
    url(r'^Artist/(?P<Artist>)', views.HaLu.as_view(), name='HaLu'),
    #url(r'^', views.index, name="index"),
    #url(r'^img/(?P<path>.*)$','django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
]