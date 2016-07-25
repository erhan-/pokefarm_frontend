"""pokefront URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.contrib import admin
from frontend.views import PokeList, Sync, Filldata, ReleasePoke, EvolvePoke, Overview, SendConfig
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Overview.as_view()),
    url(r'list/(?:(?P<account_id>\d+)/)?$', PokeList.as_view(), name='list'),
    url(r'sync/(?:(?P<account_id>\d+)/)?$', Sync.as_view(), name='sync'),
    url(r'release/(?:(?P<account_id>\d+)/(?:(?P<poke_id>\d+)/))?$', ReleasePoke.as_view(), name='release'),
    url(r'evolve/(?:(?P<account_id>\d+)/(?:(?P<poke_id>\d+)/))?$', EvolvePoke.as_view(), name='evolve'),
    url(r'fill/$', Filldata.as_view(), name='fill'),
    url(r'get_config/$', SendConfig.as_view(), name='send_config'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
