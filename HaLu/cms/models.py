# coding:utf-8

from django.db import models
from HaLu.settings import MEDIA_ROOT

import uuid
import os

# Create your models here.


class Category(models.Model):
    class Meta:
        verbose_name = 'カテゴリ'
        verbose_name_plural = 'カテゴリ'
    """
    HaLu の作品のカテゴリ（ネックレス…など）
    """
    category = models.CharField(u'カテゴリ', max_length=15)

    def __str__(self):
        return self.category


class Chapter(models.Model):
    """
    HaLu の小説の章
    """
    class Meta:
        verbose_name = '章'
        verbose_name_plural = '章'

    chapter = models.CharField(u'章', max_length=15)

    def __str__(self):
        return self.chapter


class Art(models.Model):
    """
    HaLu の作品
    """

    class Meta:
        verbose_name = 'art'
        verbose_name_plural = 'art'

    name = models.CharField(u'作品名', max_length=30)
    detail = models.TextField(u'詳細', max_length=300, blank=True, null=True)
    category = models.ForeignKey(Category)
    chapter = models.ForeignKey(Chapter)
    date = models.DateField(u'日付')
    minne_url = models.URLField(u'ミンネのURL', blank=True, null=True)
    is_sold = models.BooleanField(u'売れたか', default=False)
    price = models.IntegerField(u'値段', default=1000)
    price_sold = models.IntegerField(u'実際売った値段', default=1000)
    comment = models.TextField(
        u'作者のコメント', max_length=300, blank=True, null=True)

    def __str__(self):
        return "No. " + str(self.pk) + " " + self.name + "_" + self.date.strftime(u'%Y/%m/%d')+" 製作"


class ArtImage(models.Model):
    """
    Haru の作品の画像
    """

    class Meta:
        verbose_name = '画像'
        verbose_name_plural = '画像'

    def get_image_path(self, filename):
        """カスタマイズした画像パスを取得する.

        :param self: インスタンス (models.Model)
        :param filename: 元ファイル名
        :return: カスタマイズしたファイル名を含む画像パス
        """

        prefix = 'img/upload/'
        name = str(uuid.uuid4()).replace('-', '')
        extension = os.path.splitext(filename)[-1]
        return prefix + name + extension

    displayName = models.CharField(u'画像名', max_length=30)
    artImage = models.ImageField(u'作品の画像', upload_to=get_image_path)
    art = models.ForeignKey(Art, models.SET_NULL, blank=True,
                            null=True, verbose_name="作品", related_name="art")
    is_in_dark = models.BooleanField(u'暗闇', default=True)

    def __str__(self):
        return self.displayName

    def delete_previous_file(function):
        """不要となる古いファイルを削除する為のデコレータ実装.

        :param function: メイン関数
        :return: wrapper
        """
        def wrapper(*args, **kwargs):
            """Wrapper 関数.

            :param args: 任意の引数
            :param kwargs: 任意のキーワード引数
            :return: メイン関数実行結果
            """
            self = args[0]

            # 保存前のファイル名を取得
            result = ArtImage.objects.filter(pk=self.pk)
            previous = result[0] if len(result) else None
            super(ArtImage, self).save()

            # 関数実行
            result = function(*args, **kwargs)

            # 保存前のファイルがあったら削除
            if previous:
                os.remove(MEDIA_ROOT + "\\" +
                          previous.artImage.name.replace("/", "\\"))
            return result
        return wrapper

    @delete_previous_file
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super(ArtImage, self).save()

    @delete_previous_file
    def delete(self, using=None, keep_parents=False):
        super(ArtImage, self).delete()
