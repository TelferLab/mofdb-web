from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.reaction, name='reaction'),
        url(r'^gentelella/', views.gentelella, name='gentelella'),
        url(r'^gent_reaction/', views.gent_reaction, name='gent_reaction'),
]

from django.conf import settings
from django.views.static import serve
if settings.DEBUG:
    urlpatterns += [
        url(r'^databasefiles/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
