# coding:utf-8

from django.conf.urls import url
from blog import views
#from Haru import settings

urlpatterns =[
    #作品一覧
    #url(r'^(?P<art_id>\d+)/$', views.art_mod, name='art_mod'),  # 修正
    url(r'^', views.BlogListView.as_view() , name="blog_top"),
    #url(r'^img/(?P<path>.*)$','django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
]