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
from db.models import (Attachment,
                       AttachmentChemicalCompound,
                       AttachmentLigand,
                       AttachmentMof,
                       AttachmentReaction)
from db.models import (StructureChemicalCompound,
                       StructureLigand,
                       StructureReaction)
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
class AttachmentReactionInline(admin.TabularInline):
    model = AttachmentReaction
    extra = 1
    verbose_name = "Attachment"
    verbose_name_plural = "Attachments"

class StructureReactionInline(admin.TabularInline):
    model = StructureReaction
    extra = 1
    verbose_name = "Reaction Structure"
    verbose_name_plural = "Reaction Structures"


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
    raw_id_fields = ('component', )
    autocomplete_lookup_fields = {
        'fk': ['component', ]
    }


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
        StructureReactionInline,
        ReactionReactantInline,
        ReactionProductInline,
        ReactionCatalystCCInline,
        ReactionCatalystLigandInline,
        ReactionCatalystMofInline,
        ReactionDataInline,
        AttachmentReactionInline,
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

# ChemicalCompound {{{
class AttachmentChemicalCompoundInline(admin.TabularInline):
    model = AttachmentChemicalCompound
    extra = 1
    verbose_name = "Attachment"
    verbose_name_plural = "Attachments"

class StructureChemicalCompoundInline(admin.TabularInline):
    model = StructureChemicalCompound
    extra = 1
    verbose_name = "CC Structure"
    verbose_name_plural = "CC Structures"


@admin.register(ChemicalCompound)
class ChemicalCompoundAdmin(AutocompleteEditLinkAdminMixin, admin.ModelAdmin):
    search_fields = ('name',
                     'nick',
                     'formula',
                     )
    list_display = ('name',
                    'nick',
                    'formula',
                    )
    inlines = (
        StructureChemicalCompoundInline,
        AttachmentChemicalCompoundInline,
    )
# }}}


# Ligand {{{
class AttachmentLigandInline(admin.TabularInline):
    model = AttachmentLigand
    extra = 1
    verbose_name = "Attachment"
    verbose_name_plural = "Attachments"

class StructureLigandInline(admin.TabularInline):
    model = StructureLigand
    extra = 0
    verbose_name = "Ligand Structure"
    verbose_name_plural = "Ligand Structures"


@admin.register(BaseLigand)
class BaseLigandAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)

@admin.register(Ligand)
class LigandAdmin(AutocompleteEditLinkAdminMixin, admin.ModelAdmin):
    search_fields = ('name',
                     'nick',
                     'formula',
                     'base_ligand__name',
                     )
    list_display = ('name',
                    'nick',
                    'formula',
                    'category_name',
                    'functional_group',
                    'base_ligand_name',
                    )
    inlines = (
        StructureLigandInline,
        AttachmentLigandInline,
    )

    # Autocomplete: requires grappelli:
    # http://django-grappelli.readthedocs.io/en/latest/customization.html
    raw_id_fields = ('category', 'functional_group', 'base_ligand',)
    autocomplete_lookup_fields = {
        'fk': ['category', 'functional_group', 'base_ligand'],
    }
# }}}


# Mof {{{
class AttachmentMofInline(admin.TabularInline):
    model = AttachmentMof
    extra = 1
    verbose_name = "Attachment"
    verbose_name_plural = "Attachments"

class MofLigandInline(admin.TabularInline):
    model = Mof.ligands.through
    extra = 1
    raw_id_fields = ('ligand',)
    autocomplete_lookup_fields = {
        'fk': ['ligand']
    }


@admin.register(Mof)
class MofAdmin(AutocompleteEditLinkAdminMixin, admin.ModelAdmin):
    search_fields = ('name',
                     'nick',
                     'formula',
                     'ligands__name',
                     )
    list_display = ('name',
                    'nick',
                    'formula',
                    'topology',
                    'all_ligands',
                    )
    inlines = (
        MofLigandInline,
        AttachmentMofInline,
    )
# }}}
