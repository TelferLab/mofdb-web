from django.shortcuts import render
from django.views.generic import FormView, ListView, DetailView
from db.models import Reaction
from db.models import ChemicalCompound
from db.models import Ligand
from db.models import Mof
from db.serializers import ReactionSerializer
from db.serializers import (ReactionCatalystCCSerializer,
                            ReactionCatalystLigandSerializer,
                            ReactionCatalystMofSerializer,
                            ReactionReactantSerializer,
                            ReactionProductSerializer)
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
import json
# Create your views here.

class ReactionListViewJSON(ListView):
    model = Reaction
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        # Serialize Reactions
        serializer = ReactionSerializer(queryset,
                                        many=True, context={'request': request})
        print(serializer)
        print(serializer.data)
        print(json.dumps(serializer.data))
        return HttpResponse(json.dumps(serializer.data), content_type='application/json')

def reaction_catalysts_JSON(request, pk):
    try:
        reaction = Reaction.objects.get(pk=pk)
    except Reaction.DoesNotExist:
        return HttpResponse(status=404)

    # Serialize Reaction catalysts and add them
    s_cc = ReactionCatalystCCSerializer(reaction.reactioncatalystcc_set.all(),
                                        many=True, context={'request': request})
    s_ligand = ReactionCatalystLigandSerializer(reaction.reactioncatalystligand_set.all(),
                                                many=True, context={'request': request})
    s_mof = ReactionCatalystMofSerializer(reaction.reactioncatalystmof_set.all(),
                                          many=True, context={'request': request})

    s_catalysts_data = s_cc.data + s_ligand.data + s_mof.data
    return HttpResponse(json.dumps(s_catalysts_data), content_type='application/json')

def reaction_reactants_JSON(request, pk):
    try:
        reaction = Reaction.objects.get(pk=pk)
    except Reaction.DoesNotExist:
        return HttpResponse(status=404)

    # Serialize Reaction catalysts and add them
    s_reactant = ReactionReactantSerializer(reaction.reactionreactant_set.all(),
                                            many=True, context={'request': request})
    return HttpResponse(json.dumps(s_reactant.data), content_type='application/json')

def reaction_products_JSON(request, pk):
    try:
        reaction = Reaction.objects.get(pk=pk)
    except Reaction.DoesNotExist:
        return HttpResponse(status=404)

    # Serialize Reaction catalysts and add them
    s_product = ReactionProductSerializer(reaction.reactionproduct_set.all(),
                                          many=True, context={'request': request})
    return HttpResponse(json.dumps(s_product.data), content_type='application/json')


def index(request):
    # Query main 4 components to create a dashboard
    reactions = Reaction.objects.all().order_by('name')
    chemical_compounds = ChemicalCompound.objects.all().order_by('name')
    ligands = Ligand.objects.all().order_by('name')
    mofs = Mof.objects.all().order_by('name')
    return render(request, "db/index.html", {
        'reactions': reactions,
        'chemical_compounds': chemical_compounds,
        'ligands': ligands,
        'mofs': mofs,
    })

class ChemicalCompoundListView(ListView):
    model = ChemicalCompound

class ChemicalCompoundDetailView(DetailView):
    model = ChemicalCompound

class LigandListView(ListView):
    model = Ligand

class LigandDetailView(DetailView):
    model = Ligand

class MofListView(ListView):
    model = Mof

class MofDetailView(DetailView):
    model = Mof

class ReactionListView(ListView):
    model = Reaction

class ReactionDetailView(DetailView):
    model = Reaction

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ReactionDetailView, self).get_context_data(**kwargs)
        # Serialize Reaction and add it (to display by js)
        s_cc = ReactionCatalystCCSerializer(self.object.reactioncatalystcc_set.all(), many=True, context={'request': self.request})
        s_ligand = ReactionCatalystLigandSerializer(self.object.reactioncatalystligand_set.all(), many=True, context={'request': self.request})
        s_mof = ReactionCatalystMofSerializer(self.object.reactioncatalystmof_set.all(), many=True, context={'request': self.request})
        s_reactant = ReactionReactantSerializer(self.object.reactionreactant_set.all(), many=True, context={'request': self.request})
        s_product = ReactionProductSerializer(self.object.reactionproduct_set.all(), many=True, context={'request': self.request})

        data_reactants = s_reactant.data
        data_products = s_product.data
        data_catalysts = s_cc.data + s_ligand.data + s_mof.data
        context['data_reactants'] = JSONRenderer().render(data_reactants)
        context['data_products'] = JSONRenderer().render(data_products)
        context['data_catalysts'] = JSONRenderer().render(data_catalysts)
        return context
