from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render
from django.shortcuts import resolve_url
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import Context, loader
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from blog.models import Content
from cms.models import ArtImage
from cms.models import Category
from cms.models import Chapter

# Create your views here.


class BlogListView(ListView):
    """アイテム"""

    template_name = 'blog/blog_list.html'
    #content_object_name = 'arts'
    paginate_by = 20
    model = Content

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context


    def get_queryset(self):
        return Content.objects.filter(is_publish=True)