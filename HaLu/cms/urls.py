# coding:utf-8

from django.conf.urls import url
from cms import views
#from Haru import settings

urlpatterns =[
    #作品一覧
    url(r'^Arts/$', views.arts_list, name='arts_list'),
    url(r'^Arts/add/$', views.art_mod, name='art_add'),  # 登録
    url(r'^Arts/mod/(?P<art_id>\d+)/$', views.art_mod, name='art_mod'),  # 修正
    url(r'^Arts/del/(?P<art_id>\d+)/$', views.art_del, name='art_del'),   # 削除

    #url(r'^', views.index, name="index"),
    #url(r'^img/(?P<path>.*)$','django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
]