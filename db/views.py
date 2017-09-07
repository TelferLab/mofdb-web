from django.shortcuts import render
from db.models import Reaction
from db.models import ChemicalCompound
from db.models import Ligand
from db.models import Mof
from db.models import ExperimentalData

import django_tables2 as tables

class ExperimentalDataTable(tables.Table):
    class Meta:
        model = ExperimentalData

# Create your views here.

def reaction(request):
    reactions = Reaction.objects.all().order_by('name')
    return render(request, "db/reaction.html", {'reactions': reactions})

def gent_reaction(request):
    reactions = Reaction.objects.all().order_by('name')
    experimental_data_table = ExperimentalDataTable(ExperimentalData.objects.all())
    chemical_compounds = ChemicalCompound.objects.all().order_by('name')
    ligands = Ligand.objects.all().order_by('name')
    mofs = Mof.objects.all().order_by('name')
    return render(request, "db/greaction.html", {
        'reactions': reactions,
        'chemical_compounds': chemical_compounds,
        'ligands': ligands,
        'mofs': mofs,
        'experimental_data_table': experimental_data_table,
    })

def gentelella(request):
    return render(request, "gentelella/index.html", {})
