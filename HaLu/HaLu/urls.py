""" world-of-f URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import TemplateView
from cms import views

urlpatterns = [
    #static(STORY_MAIN_URL, document_root=STORY_MAIN_ROOT),
    url(r'^abcde/admin/', admin.site.urls),
    url(r'^about/', include('about.urls', namespace='about')),
    url(r'^api/', include('api.urls', namespace='api')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^cms/', include('cms.urls', namespace='cms')),
    url(r'^item/', include('items.urls', namespace='item')),
    url(r'^story/', include('story.urls', namespace='story')),
    #url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^information',views.InformationView.as_view()),
    url(r'^$', views.IndexView.as_view()),
]
