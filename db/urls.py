from django.conf.urls import include, url
from . import views
from db.views import ReactionListView, ReactionDetailView
from db.views import ChemicalCompoundListView, ChemicalCompoundDetailView
from db.views import LigandListView, LigandDetailView
from db.views import MofListView, MofDetailView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index', views.index, name='index'),
    url(r'^reactions/([\w-]+)/$', ReactionListView.as_view(), name='reaction.views.list'),
    url(r'^reaction/(?P<pk>[0-9]+)/$', ReactionDetailView.as_view(), name='reaction.views.details'),
    url(r'^chemicalcompounds/([\w-]+)/$', ChemicalCompoundListView.as_view(), name='chemicalcompound.views.list'),
    url(r'^chemicalcompound/(?P<pk>[0-9]+)/$', ChemicalCompoundDetailView.as_view(), name='chemicalcompound.views.details'),
    url(r'^ligands/([\w-]+)/$', LigandListView.as_view(), name='ligand.views.list'),
    url(r'^ligand/(?P<pk>[0-9]+)/$', LigandDetailView.as_view(), name='ligand.views.details'),
    url(r'^mofs/([\w-]+)/$', MofListView.as_view(), name='mof.views.list'),
    url(r'^mof/(?P<pk>[0-9]+)/$', MofDetailView.as_view(), name='mof.views.details'),
]

from django.conf import settings
from django.views.static import serve
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^databasefiles/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
