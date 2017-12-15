from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class IndexView(TemplateView):

    template_name = 'story/index.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['chapter'] = "1st"
        ctx['items'] = 'item'
        return ctx

class First(TemplateView):

    template_name = 'story/index.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['chapter'] = "1st"
        ctx['items'] = 'item'
        return ctx

class Second(TemplateView):

    template_name = 'story/index.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['chapter'] = "2nd"
        ctx['items'] = 'item'
        return ctx

class MainView(TemplateView):

    template_name = "html/index.html"

    def get_context_data(self,**kwargs):

        return None