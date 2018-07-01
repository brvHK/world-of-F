# coding:utf-8

from django.conf.urls import url
from about import views
from django.views.generic.base import TemplateView

urlpatterns =[
    #作品一覧
    # url(r'^Artist/HaLu', views.HaLu.as_view(), name='HaLu'),
    url(r'^Artist/HaLu', TemplateView.as_view(template_name = 'about/HaLu.html')),
    url(r'^Artist/HK', TemplateView.as_view(template_name = 'about/Ken.html'), name='Ken'),
    url(r'^Artist/(?P<Artist>)', views.HaLu.as_view(), name='HaLu'),
    url(r'^this-site', views.WorldOfFView.as_view(), name='this-site')
    #url(r'^', views.index, name="index"),
    #url(r'^img/(?P<path>.*)$','django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
]
