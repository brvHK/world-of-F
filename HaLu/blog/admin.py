from django.contrib import admin
from blog.models import Content
from blog.models import RoughCategory
from blog.models import SmallCategory
from blog.models import Tag

# Register your models here.

admin.site.register(Content)
admin.site.register(RoughCategory)
admin.site.register(SmallCategory)
admin.site.register(Tag)