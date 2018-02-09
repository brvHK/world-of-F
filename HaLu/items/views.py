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

from cms.models import Art
from cms.models import ArtImage
from cms.models import Category
from cms.models import Chapter

# Create your views here.


class Item(ListView):
    """アイテム"""

    template_name = 'item/list.html'
    #content_object_name = 'arts'
    paginate_by = 20
    model = Art

    def get_context_data(self, **kwargs):
        q_categorys = self.request.GET.getlist('category')
        q_chapters = self.request.GET.getlist('chapter')
        page = self.kwargs.get('page')
        paginator = Paginator(self.object_list, self.paginate_by)
        try:
            self.object_list = paginator.page(page)
        except PageNotAnInteger:
            self.object_list = paginator.page(1)
        except EmptyPage:
            self.object_list = paginator.page(paginator.num_pages)

        context = super().get_context_data(**kwargs)
        categorys = Category.objects.all()
        artImages = ArtImage.objects.all()
        chapters = Chapter.objects.all()
        context["categorys"] = categorys
        context["q_categorys"] = q_categorys
        context["q_chapters"] = q_chapters
        context["artImages"] = artImages
        context["chapters"] = chapters
        # print(context)

        return context

    """
    def get_context_data(self, *args, **kwargs):
        arts_list = Art.objects.all().order_by('date')
        if self.kwargs.get("filter-category"):
            # 絞り込み検索処理
            category = Category.objects.get(
                pk=self.kwargs.get("filter-category"))
            arts_list.objects.get(category=category)
        paginator = Paginator(arts_list, self.paginate_by)

        page = self.kwargs.get('page')
        try:
            arts = paginator.page(page)
        except PageNotAnInteger:
            arts = paginator.page(1)
        except EmptyPage:
            arts = paginator.page(paginator.num_pages)


        categorys = Category.objects.all()
        artImages = ArtImage.objects.all()
        chapters = Chapter.objects.all()
        #self.queryset = arts

        context = {}
        context["categorys"] = categorys
        context["artImages"] = artImages
        context["chapters"] = chapters
        print(context)

        return context
"""

    def get_queryset(self):
        # デフォルトは全件取得

        results = Art.objects.all().order_by('date')
        q_categorys = self.request.GET.getlist('category')
        q_chapters = self.request.GET.getlist('chapter')
        q = None

        if len(q_categorys) != 0:
            print(u"len > 0")
            for q_category in q_categorys:
                cate = Category.objects.get(pk=q_category)
                q = Q(category=cate) if q is None else q | Q(category=cate)

        if q is not None:
            results = results.filter(q)

        q = None
        if len(q_chapters) != 0:
            for q_chapter in q_chapters:
                chap = Chapter.objects.get(pk=q_chapter)
                q = Q(chapter=chap) if q is None else q | Q(chapter=chap)

        if q is not None:
            print(str(q))
            results = results.filter(q)

        return results


class ItemDetailView(DetailView):
    """アイテム"""

    model = Art
