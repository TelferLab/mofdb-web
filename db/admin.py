from django.contrib import admin

from db.models import LigandCategory
from db.models import ReactionCategory
from db.models import ChemicalCompound
from db.models import DataType
from db.models import FunctionalGroup
from db.models import BaseLigand
from db.models import Ligand
from db.models import Mof
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
from db.serializers import (ReactionCatalystCCSerializer,
                            ReactionCatalystLigandSerializer,
                            ReactionCatalystMofSerializer,
                            ReactionReactantSerializer,
                            ReactionProductSerializer)
# from db.tables import (CatalystsTable,
#                        ReactantsTable,
#                        ProductsTable)
# Might be reduntant in the future, check:
# https://github.com/sehmaschine/django-grappelli/issues/618
from grappelli_autocomplete_fk_edit_link import AutocompleteEditLinkAdminMixin

# Register your models here.
@admin.register(DataType)
class DataTypeAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)

@admin.register(LigandCategory)
class LigandCategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)

@admin.register(ReactionCategory)
class ReactionCategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)

@admin.register(FunctionalGroup)
class FunctionalGroupAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)

# Reaction {{{
class VisualizationReactionInline(admin.TabularInline):
    model = VisualizationReaction
    extra = 1
    verbose_name = "Visualization"
    verbose_name_plural = "Visualizations"


class ReactionDataInline(admin.TabularInline):
    model = ReactionData
    extra = 1
    verbose_name = "Reaction Data"
    verbose_name_plural = "Reaction Datas"


class ReactionCatalystCCInline(admin.TabularInline):
    model = Reaction.catalysts_cc.through
    extra = 1
    verbose_name = "Catalyst: Chemical Compound"
    verbose_name_plural = "Catalysts: Chemical Compounds"


class ReactionCatalystLigandInline(admin.TabularInline):
    model = Reaction.catalysts_ligand.through
    extra = 1
    verbose_name = "Catalyst: Ligand"
    verbose_name_plural = "Catalyst: Ligands"
    verbose_name_plural = "Catalysts: Ligands"
    raw_id_fields = ('component', )
    autocomplete_lookup_fields = {
        'fk': ['component', ]
    }


class ReactionCatalystMofInline(admin.TabularInline):
    model = Reaction.catalysts_mof.through
    extra = 1
    verbose_name = "Catalyst: Mof"
    verbose_name_plural = "Catalysts: Mofs"
    raw_id_fields = ('component',)
    autocomplete_lookup_fields = {
        'fk': ['component', ]
    }


class ReactionReactantInline(admin.TabularInline):
    model = Reaction.reactants.through
    extra = 1
    verbose_name = "Reactant"
    verbose_name_plural = "Reactants"
    raw_id_fields = ('component',)
    autocomplete_lookup_fields = {
        'fk': ['component']
    }


class ReactionProductInline(admin.TabularInline):
    model = Reaction.products.through
    extra = 1
    verbose_name = "Product"
    verbose_name_plural = "Products"
    raw_id_fields = ('component',)
    autocomplete_lookup_fields = {
        'fk': ['component']
    }


@admin.register(Reaction)
class ReactionAdmin(AutocompleteEditLinkAdminMixin, admin.ModelAdmin):
    # For order: if you want to mix fields, and inlines,
    # have to modify template (change_form):
    # https://stackoverflow.com/questions/1206991/django-admin-change-order-of-fields-including-inline-fields
    search_fields = ('name',
                     'catalysts_cc__name',
                     'catalysts_ligand__name',
                     'catalysts_mof__name',
                     'reactants__name',
                     'products__name',
                     )
    inlines = (
        VisualizationReactionInline,
        ReactionReactantInline,
        ReactionProductInline,
        ReactionCatalystCCInline,
        ReactionCatalystLigandInline,
        ReactionCatalystMofInline,
        ReactionDataInline,
    )
    list_display = ('name', 'all_catalysts_ligand')

    class Media:
        css = {
            "all": ("admin/css/reaction/reaction.css",)
        }
        # js = ("")

    def all_components_table(self, obj):
        """ return a table with all the components """
        # return "\n".join([a.name for a in obj.catalysts_ligand.exper()])
        return str(obj)

    change_form_template = 'db/admin/reaction/change_form.html'

    # Change view to add table information
    # def change_view(self, request, object_id, form_url='', extra_context=None):
    #     extra_context = extra_context or {}
    #     # Queries
    #     q_cc = ReactionCatalystCC.objects.filter(reaction=object_id)
    #     q_ligand = ReactionCatalystLigand.objects.filter(reaction=object_id)
    #     q_mof = ReactionCatalystMof.objects.filter(reaction=object_id)
    #     q_reactant = ReactionReactant.objects.filter(reaction=object_id)
    #     q_product = ReactionProduct.objects.filter(reaction=object_id)
    #     # Serialize (they are [OrderedDict[(),], OrderedDict ])
    #     s_cc = ReactionCatalystCCSerializer(q_cc, many=True, context={'request': request})
    #     s_ligand = ReactionCatalystLigandSerializer(q_ligand, many=True, context={'request': request})
    #     s_mof = ReactionCatalystMofSerializer(q_mof, many=True, context={'request': request})
    #     s_reactant = ReactionReactantSerializer(q_reactant, many=True, context={'request': request})
    #     s_product = ReactionProductSerializer(q_product, many=True, context={'request': request})
    #
    #     data_reactants = s_reactant.data
    #     data_products = s_product.data
    #     data_catalysts = s_cc.data + s_ligand.data + s_mof.data
    #
    #     # Create table from serialized data
    #     # Ligand Table:
    #     # table = ReactionCatalystLigandTable(q_ligand)
    #     # extra_context['table'] = table
    #     # Generic Table:
    #     table_catalysts = CatalystsTable(data_catalysts)
    #     extra_context['table_catalysts'] = table_catalysts
    #     table_reactants = ReactantsTable(data_reactants)
    #     extra_context['table_reactants'] = table_reactants
    #     table_products = ProductsTable(data_products)
    #     extra_context['table_products'] = table_products
    #     return super().change_view(
    #         request, object_id, form_url, extra_context=extra_context,
    #     )

# }}}


# ChemicalCompound {{{
class VisualizationCCInline(admin.TabularInline):
    model = VisualizationCC
    extra = 1


@admin.register(ChemicalCompound)
class ChemicalCompoundAdmin(admin.ModelAdmin):
    search_fields = ('name',
                     'nick',
                     'formula',
                     )
    list_display = ('name',
                    'nick',
                    'formula',
                    'synthesis',
                    'analysis',
                    'mass',
                    )
    inlines = (
        VisualizationCCInline,
    )
# }}}


# Ligand {{{
class VisualizationLigandInline(admin.TabularInline):
    model = VisualizationLigand
    extra = 1


@admin.register(BaseLigand)
class BaseLigandAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)
# class BaseLigandAdmin(admin.ModelAdmin):
#     def get_model_perms(self, request):
#         """
#         Return empty perms dict thus hiding the model from admin index, but allowing edit/add new from Ligand.
#         """
#         return {}

@admin.register(Ligand)
class LigandAdmin(admin.ModelAdmin):
    search_fields = ('name',
                     'nick',
                     'formula',
                     'base_ligand__name',
                     )
    list_display = ('name',
                    'nick',
                    'formula',
                    'synthesis',
                    'analysis',
                    'mass',
                    'category_name',
                    'functional_group',
                    'base_ligand_name',
                    )
    inlines = (
        VisualizationLigandInline,
    )

    # Autocomplete: requires grappelli:
    # http://django-grappelli.readthedocs.io/en/latest/customization.html
    raw_id_fields = ('category', 'functional_group', 'base_ligand',)
    autocomplete_lookup_fields = {
        'fk': ['category', 'functional_group', 'base_ligand'],
    }
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
    search_fields = ('name',
                     'nick',
                     'formula',
                     'ligands__name',
                     )
    list_display = ('name',
                    'nick',
                    'formula',
                    'synthesis',
                    'analysis',
                    'mass',
                    'topology',
                    'all_ligands',
                    )
    inlines = (
        VisualizationMofInline,
        MofLigandInline,
    )
# }}}
