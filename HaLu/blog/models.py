from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):

    class Meta:
        
        verbose_name = "タグ"
        verbose_name_plural ="タグ"

    name = models.CharField("名称", max_length=255)
 
    def __str__(self):
        return self.name
 
    def get_contents(self):
        queryset = Content.objects.filter(tag=self).filter(is_publish=True)


class Category(models.Model):

    class Meta:
        abstract = True
    
    name = models.CharField('名称', max_length=255)


    def __str__(self):
        return self.name

class RoughCategory(Category):

    class Meta:

        verbose_name = "大カテゴリ"
        verbose_name_plural ="大カテゴリ"

    name = models.CharField('名称', max_length=255)

    def __str__(self):
        return self.name

class SmallCategory(Category):

    class Meta:

        verbose_name = "小カテゴリ"
        verbose_name_plural ="小カテゴリ"

    parent = models.ForeignKey(RoughCategory, verbose_name="大カテゴリ")
    name = models.CharField('名称', max_length=255)

    def __str__(self):
        return self.name

class Content(models.Model):

    class Meta:

        verbose_name = "本文"
        verbose_name_plural ="本文"

    title = models.CharField(u"題名", max_length=100)
    content = models.TextField(u"本文")
    create_date = models.DateTimeField(u"投稿日", auto_now_add=True)
    update_date = models.DateTimeField(u"更新日", auto_now=True)
    writer = models.ForeignKey(User, verbose_name="投稿者",null=True,blank=True)
    category = models.ForeignKey(SmallCategory, verbose_name="カテゴリ",null=True,blank=True)
    tag = models.ManyToManyField(Tag, blank=True, verbose_name="タグ")
    thumbnail = models.ImageField("サムネイル", upload_to='thumnail/', blank=True)
    is_publish = models.BooleanField("公開OK", default=True)
    is_html_source = models.BooleanField("HTMLで記述した", default=False)
    is_rst_source = models.BooleanField("reStructuredTextで記述した", default=False)
 
    def __str__(self):
        return self.title

    