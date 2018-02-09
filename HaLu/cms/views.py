from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse

from cms.models import Art
from cms.forms import ArtForm

# Create your views here.

def arts_list(request):
    """
    HaLu の作品の一覧
    """
    #return HttpResponse(u'作品一覧')
    arts = Art.objects.all().order_by('id')
    return render(request,
                  'cms/arts_list.html',
                  {'arts': arts}
    )

def art_add(request):
    """
    HaLu の作品の登録
    """
    return HttpResponse(u'作品の登録')


def art_mod(request, art_id=None):
    """
    HaLu の作品の修正
    """

    if art_id:
        art = get_object_or_404(Art, pk=art_id)
    else:
        art = Art()
    if request.method == 'POST':  
        form = ArtForm(request.POST, instance=art)
        if form.is_valid():
            art = form.save(commit=False)
            art.save()
            return redirect('cms:arts_list')
    else:
        form = ArtForm(instance=art)
    return render(request, 'cms/art_mod.html', dict(form=form, art_id=art_id))


    #return HttpResponse(u'作品の修正')

def art_del(request, art_id=None):
    """
    HaLu の作品の削除
    """

    art = get_object_or_404(Art, pk=art_id)
    art.delete()
    return redirect('cms:arts_list')

    #return HttpResponse(u'作品の削除')

def index(request):
    """
    index
    """
    return render(request, 'template/index.html')
