# coding:utf-8

from django.forms import ModelForm
from cms.models import Art


class ArtForm(ModelForm):
    """作品のフォーム"""

    class Meta:
        model = Art
        fields = ('name', 'detail', 'category', 'chapter', 'date',)