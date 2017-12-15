from django.contrib import admin
from cms.models import Art
from cms.models import Category
from cms.models import Chapter
from cms.models import ArtImage

admin.site.register(Art)
admin.site.register(Category)
admin.site.register(Chapter)
admin.site.register(ArtImage)

# Register your models here.
