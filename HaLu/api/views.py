from datetime import date
import sys
import json

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from django.db.models import Sum
from cms.models import ArtImage
from cms.models import Art

# Create your views here.


def get_image(request, pk=None, light=None):
    status = None

    art = Art.objects.get(pk=pk)

    artimages = ArtImage.objects.filter(art=art)
    print(light)

    if light == 'off' or light is None:
        # query_paramが指定されている場合の処理
        artimages = artimages.filter(is_in_dark=True)
    else:
        artimages = artimages.filter(is_in_dark=False)

    config = create_artimage_dict(artimages)
    json_str = json.dumps(config, ensure_ascii=False, indent=2)
    return _respose_json(request=request, json_str=json_str, status=status)


def get_images(request, pk=None, light=None):
    status = None

    art = Art.objects.get(pk=pk)

    artimages = ArtImage.objects.filter(art=art)
    print(light)

    if light == 'off' or light is None:
        # query_paramが指定されている場合の処理
        artimages = artimages.filter(is_in_dark=True)
    else:
        artimages = artimages.filter(is_in_dark=False)

    config = create_artimage_dict(artimages)
    json_str = json.dumps(config, ensure_ascii=False, indent=2)
    return _respose_json(request=request, json_str=json_str, status=status)


def _respose_json(request, json_str, status):
    callback = request.GET.get('callback')
    if not callback:
        callback = request.POST.get('callback')
    if callback:
        json_str = "%s(%s)" % (callback, json_str)
        response = HttpResponse(
            json_str, content_type='application/javascript; charset=UTF-8', status=status)
    else:
        response = HttpResponse(
            json_str, content_type='application/javascript; charset=UTF-8', status=status)

    return response


def create_artimage_dict(artImages):

    config = {}
    for artImage in artImages:
        config["id"] = str(artImage.id)
        config["image"] = artImage.artImage.name

    return config
