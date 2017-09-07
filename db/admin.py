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
from db.models import ExperimentalData
from db.models import ReactionComponent
from db.models import VisualizationCC
from db.models import VisualizationLigand
from db.models import VisualizationMof
from db.models import VisualizationReaction


# Register your models here.

admin.site.register(DataType)
admin.site.register(Category)
admin.site.register(FunctionalGroup)
admin.site.register(ExperimentalData)


# Reaction {{{
class VisualizationReactionInline(admin.TabularInline):
    model = VisualizationReaction
    extra = 1


class ReactionDataInline(admin.TabularInline):
    model = ReactionData
    extra = 1


class ReactionComponentCCInline(admin.TabularInline):
    model = Reaction.catalysts_cc.through
    extra = 1


class ReactionComponentLigandInline(admin.TabularInline):
    model = Reaction.catalysts_ligand.through
    extra = 1


class ReactionComponentMofInline(admin.TabularInline):
    model = Reaction.catalysts_mof.through
    extra = 1


class ReactionComponentReactantInline(admin.TabularInline):
    model = Reaction.reactants.through
    extra = 1


class ReactionComponentProductInline(admin.TabularInline):
    model = Reaction.products.through
    extra = 1


@admin.register(Reaction)
class ReactionAdmin(admin.ModelAdmin):
    inlines = (
        VisualizationReactionInline,
        ReactionDataInline,
        ReactionComponentCCInline,
        ReactionComponentLigandInline,
        ReactionComponentMofInline,
        ReactionComponentReactantInline,
        ReactionComponentProductInline,
    )

# }}}


# ChemicalCompound {{{
class VisualizationCCInline(admin.TabularInline):
    model = VisualizationCC
    extra = 1


@admin.register(ChemicalCompound)
class ChemicalCompoundAdmin(admin.ModelAdmin):
    inlines = (
        VisualizationCCInline,
    )
# }}}


# Ligand {{{
class VisualizationLigandInline(admin.TabularInline):
    model = VisualizationLigand
    extra = 1


@admin.register(Ligand)
class LigandAdmin(admin.ModelAdmin):
    inlines = (
        VisualizationLigandInline,
    )
# }}}


# Mof {{{
class MofLigandInline(admin.TabularInline):
    model = Mof.ligands.through
    extra = 1


class VisualizationMofInline(admin.TabularInline):
    model = VisualizationMof
    extra = 1


@admin.register(Mof)
class MofAdmin(admin.ModelAdmin):
    inlines = (
        VisualizationMofInline,
        MofLigandInline,
    )
# }}}
