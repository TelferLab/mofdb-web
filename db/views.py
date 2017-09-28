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
# Create your views here.

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
        print(data_products)
        context['data_reactants'] = JSONRenderer().render(data_reactants)
        context['data_products'] = JSONRenderer().render(data_products)
        context['data_catalysts'] = JSONRenderer().render(data_catalysts)
        return context
