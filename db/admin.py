from django.contrib import admin

from db.models import Category
from db.models import ChemicalCompound
from db.models import DataType
from db.models import FunctionalGroup
from db.models import Ligand
from db.models import Mof
from db.models import MofLigand
from db.models import Reaction
from db.models import ReactionData
from db.models import CatalystData
from db.models import ReactionCatalystCC
from db.models import ReactionCatalystLigand
from db.models import ReactionCatalystMof
from db.models import ReactionReactant
from db.models import ReactionProduct
from db.models import VisualizationCC
from db.models import VisualizationLigand
from db.models import VisualizationMof
from db.models import VisualizationReaction


# Register your models here.

admin.site.register(Category)
admin.site.register(ChemicalCompound)
admin.site.register(DataType)
admin.site.register(FunctionalGroup)
admin.site.register(Ligand)
admin.site.register(Mof)
admin.site.register(MofLigand)
admin.site.register(Reaction)
admin.site.register(ReactionData)
admin.site.register(CatalystData)
admin.site.register(ReactionCatalystCC)
admin.site.register(ReactionCatalystLigand)
admin.site.register(ReactionCatalystMof)
admin.site.register(ReactionReactant)
admin.site.register(ReactionProduct)
admin.site.register(VisualizationCC)
admin.site.register(VisualizationLigand)
admin.site.register(VisualizationMof)
admin.site.register(VisualizationReaction)
