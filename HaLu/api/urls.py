# coding:utf-8

from django.conf.urls import url
from api import views
#from Haru import settings

urlpatterns =[
    #作品一覧
    url(r'^get_image/(?P<pk>\d+)/$', views.get_image, name='get_image_by_pk'),
    url(r'^get_image/(?P<pk>\d+)/(?P<light>\w+)/$', views.get_image, name='get_image_by_pk_on'),
    url(r'^get_image/(?P<pk>\d+)/(?P<light>\w+)/$', views.get_image, name='get_image_by_pk_off'),
]