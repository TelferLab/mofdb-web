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
from db.models import ReactionCatalystCC
from db.models import ReactionCatalystLigand
from db.models import ReactionCatalystMof
from db.models import ReactionReactant
from db.models import ReactionProduct
from db.models import VisualizationCC
from db.models import VisualizationLigand
from db.models import VisualizationMof
from db.models import VisualizationReaction
import django_tables2 as tables
from db.serializers import (ReactionCatalystCCSerializer,
                            ReactionCatalystLigandSerializer,
                            ReactionCatalystMofSerializer,
                            ReactionReactantSerializer,
                            ReactionProductSerializer)

# Register your models here.

# admin.site.register(ChemicalCompound)
# admin.site.register(Reaction)
# admin.site.register(Ligand)
# admin.site.register(Mof)
admin.site.register(DataType)
admin.site.register(Category)
admin.site.register(FunctionalGroup)
# admin.site.register(MofLigand)
# admin.site.register(ReactionData)
# admin.site.register(ReactionCatalystCC)
# admin.site.register(ReactionCatalystLigand)
# admin.site.register(ReactionCatalystMof)
# admin.site.register(ReactionReactant)
# admin.site.register(ReactionProduct)
# admin.site.register(VisualizationCC)
# admin.site.register(VisualizationLigand)
# admin.site.register(VisualizationMof)
# admin.site.register(VisualizationReaction)


# Reaction {{{
class VisualizationReactionInline(admin.TabularInline):
    model = VisualizationReaction
    extra = 1


class ReactionDataInline(admin.TabularInline):
    model = ReactionData
    extra = 1


class ReactionCatalystCCInline(admin.TabularInline):
    model = Reaction.catalysts_cc.through
    extra = 1


class ReactionCatalystLigandInline(admin.TabularInline):
    model = Reaction.catalysts_ligand.through
    extra = 1


class ReactionCatalystMofInline(admin.TabularInline):
    model = Reaction.catalysts_mof.through
    extra = 1


class ReactionReactantInline(admin.TabularInline):
    model = Reaction.reactants.through
    extra = 1


class ReactionProductInline(admin.TabularInline):
    model = Reaction.products.through
    extra = 1

# Tables {{{
class GenericComponentTable(tables.Table):
    component_type = tables.Column()
    component_name = tables.Column()
    component_id = tables.LinkColumn()
    component_id = tables.Column()
    functional_group_name = tables.Column()
    chirality = tables.Column()
    rate_constant = tables.Column()
    conversion = tables.Column()
    ee = tables.Column()
    de = tables.Column()
    yield_field = tables.Column()
    amount = tables.Column()
#}}}

@admin.register(Reaction)
class ReactionAdmin(admin.ModelAdmin):
    inlines = (
        VisualizationReactionInline,
        ReactionDataInline,
        ReactionCatalystCCInline,
        ReactionCatalystLigandInline,
        ReactionCatalystMofInline,
        ReactionReactantInline,
        ReactionProductInline,
    )
    list_display = ('name', 'all_catalysts_ligand')

    def all_components_table(self, obj):
        """ return a table with all the components """
        # return "\n".join([a.name for a in obj.catalysts_ligand.exper()])
        return str(obj)

    change_form_template = 'db/admin/reaction/change_form.html'

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        # Queries
        q_cc = ReactionCatalystCC.objects.filter(reaction_id=object_id)
        q_ligand = ReactionCatalystLigand.objects.filter(reaction_id=object_id)
        q_mof = ReactionCatalystMof.objects.filter(reaction_id=object_id)
        q_reactant = ReactionReactant.objects.filter(reaction_id=object_id)
        q_product = ReactionProduct.objects.filter(reaction_id=object_id)
        # Serialize (they are [OrderedDict[(),], OrderedDict ])
        s_cc = ReactionCatalystCCSerializer(q_cc, many=True)
        s_ligand = ReactionCatalystLigandSerializer(q_ligand, many=True)
        s_mof = ReactionCatalystMofSerializer(q_mof, many=True)
        s_reactant = ReactionReactantSerializer(q_reactant, many=True)
        s_product = ReactionProductSerializer(q_product, many=True)

        data = s_cc.data + s_ligand.data + s_mof.data + s_reactant.data + s_product.data

        # Create table from serialized data
        # Ligand Table:
        # table = ReactionCatalystLigandTable(q_ligand)
        # extra_context['table'] = table
        # Generic Table:
        table = GenericComponentTable(data)
        extra_context['table'] = table
        return super().change_view(
            request, object_id, form_url, extra_context=extra_context,
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
