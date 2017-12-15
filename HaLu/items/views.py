from django.shortcuts import render
from django.shortcuts import resolve_url
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import Context, loader
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView

# Create your views here.
class Item(TemplateView):
    """アイテム"""

    template_name = 'item/list.html'

    def get_context_data(self, *args, **kwargs):
        """HaLu"""
        
        context = {}
        

        return context