from django.conf.urls import include, url
from . import views
from db.views import ReactionListView, ReactionDetailView
from db.views import ChemicalCompoundListView, ChemicalCompoundDetailView
from db.views import LigandListView, LigandDetailView
from db.views import MofListView, MofDetailView

urlpatterns = [
    url(r'^search/', include('haystack.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^index', views.index, name='index'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^reactions/([\w-]+)/$', ReactionListView.as_view(), name='reaction.views.list'),
    url(r'^reaction/(?P<pk>[0-9]+)/$', ReactionDetailView.as_view(), name='reaction.views.details'),
    url(r'^chemicalcompounds/([\w-]+)/$', ChemicalCompoundListView.as_view(), name='chemicalcompound.views.list'),
    url(r'^chemicalcompound/(?P<pk>[0-9]+)/$', ChemicalCompoundDetailView.as_view(), name='chemicalcompound.views.details'),
    url(r'^ligands/([\w-]+)/$', LigandListView.as_view(), name='ligand.views.list'),
    url(r'^ligand/(?P<pk>[0-9]+)/$', LigandDetailView.as_view(), name='ligand.views.details'),
    url(r'^mofs/([\w-]+)/$', MofListView.as_view(), name='mof.views.list'),
    url(r'^mof/(?P<pk>[0-9]+)/$', MofDetailView.as_view(), name='mof.views.details'),
### TABLES ####
# Reaction #
    url(r'^reaction-catalysts-table/(?P<pk>[0-9]+)/$', views.reaction_catalysts_JSON, name='reaction.views.catalyststable'),
    url(r'^reaction-reactants-table/(?P<pk>[0-9]+)/$', views.reaction_reactants_JSON, name='reaction.views.reactantstable'),
    url(r'^reaction-products-table/(?P<pk>[0-9]+)/$', views.reaction_products_JSON, name='reaction.views.productstable'),
    url(r'^reactions-table/([\w-]+)/$', views.ReactionListViewJSON.as_view(), name='reaction.views.table'),
# Mof #
    url(r'^mof-ligands-table/(?P<pk>[0-9]+)/$', views.mof_ligands_JSON, name='mof.views.ligandstable'),
    url(r'^mofs-table/([\w-]+)/$', views.MofListViewJSON.as_view(), name='mof.views.table'),
# Ligand #
    url(r'^ligands-table/([\w-]+)/$', views.LigandListViewJSON.as_view(), name='ligand.views.table'),
# ChemicalCompound #
    url(r'^chemicalcompounds-table/([\w-]+)/$', views.ChemicalCompoundListViewJSON.as_view(), name='chemicalcompound.views.table'),
]

from django.conf import settings
from django.views.static import serve
if settings.DEBUG:
    urlpatterns += [
        url(r'^databasefiles/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
