from django.shortcuts import render
from django.shortcuts import resolve_url
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import Context, loader
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView

# Create your views here.

class HaLu(TemplateView):
    """カレンダーを表示するビュー."""

    template_name = 'about/Artist.html'

    def get_context_data(self, *args, **kwargs):
        """HaLu"""
        
        context = {}
        context['Artist'] = 'HaLu'
        context['nickname'] = 'F の創人'
        context['act1'] = '2013年から各地イベントに参加。'
        context['act2'] = 'F の創人'
        context['comments'] = """自作ファンタジー世界の「World of F ～Fの世界～」で使用されているアイテムや幻想的な風景を、
                                様々な素材を用いて表現しています。
                                自然と歴史が好き。"""
        context['since'] = '2013'
        context['twitter'] = 'https://twitter.com/Hyu_HaLu?ref_src=twsrc%5Etfw'

        return context

class Ken(TemplateView):
    """カレンダーを表示するビュー."""

    template_name = 'about/Artist.html'

    def get_context_data(self, *args, **kwargs):
        """HaLu"""
        
        context = {}
        context['Artist'] = 'Ken'
        context['nickname'] = 'F の案内人'
        context['comments'] = 'あいうえおお'
        context['since'] = '2017'
        context['twitter'] = 'https://twitter.com/brv_HK?ref_src=twsrc%5Etfw'

        return context

class WorldOfFView(TemplateView):

    template_name = 'about/World-of-F.html'

    def get_context_date(self, *args, **kwargs):

        context = {}

        return context

