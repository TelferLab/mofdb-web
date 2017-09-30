# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

from django.core.validators import MinValueValidator

from enumfields import EnumField
from enumfields import Enum  # Uses Ethan Furman's "enum34" backport
from django.urls import reverse  # for get_absolute_url
from django.contrib import admin

class Chirality(Enum):
    R = 'right'
    S = 'left'
    NONE = 'none'

class ComponentType(Enum):
    CC = 'CC'
    LIGAND = 'Ligand'
    MOF = 'Mof'
    REACTANT = 'Reactant'
    PRODUCT = 'Product'


class LigandCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ligandcategory.views.details', args=[str(self.id)])

    class Meta:
        verbose_name = "LigandCategory"
        verbose_name_plural = "LigandCategories"


class ReactionCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('reactioncategory.views.details', args=[str(self.id)])

    class Meta:
        verbose_name = "ReactionCategory"
        verbose_name_plural = "ReactionCategories"


class DataType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('datatype.views.details', args=[str(self.id)])

    class Meta:
        db_table = 'DataType'


class FunctionalGroup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('functionalgroup.views.details', args=[str(self.id)])

    class Meta:
        db_table = 'FunctionalGroup'


class ChemicalCompound(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True)
    nick = models.CharField(max_length=100, blank=True)
    formula = models.CharField(max_length=100, blank=True)
    synthesis = models.TextField(blank=True)
    analysis = models.TextField(blank=True)
    mass = models.FloatField(
        validators=[MinValueValidator(0.0)],
        blank=True, null=True)
    functional_group = models.ForeignKey(
        FunctionalGroup,
        on_delete=models.DO_NOTHING,
        related_name='chemicalcompound',
        blank=True, null=True)
    chirality = EnumField(Chirality, max_length=5, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('chemicalcompound.views.details', args=[str(self.id)])

    class Meta:
        db_table = 'ChemicalCompound'


class BaseLigand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('baseligand.views.details', args=[str(self.id)])

    class Meta:
        db_table = 'BaseLigand'


class Ligand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True)
    nick = models.CharField(max_length=100, blank=True)
    formula = models.CharField(max_length=100, blank=True)
    synthesis = models.TextField(blank=True)
    analysis = models.TextField(blank=True)
    mass = models.FloatField(
        validators=[MinValueValidator(0.0)],
        blank=True, null=True)

    category = models.ForeignKey(
        LigandCategory,
        on_delete=models.DO_NOTHING,
        related_name='ligands',
        blank=True, null=True)

    functional_group = models.ForeignKey(
        FunctionalGroup,
        on_delete=models.DO_NOTHING,
        related_name='ligands',
        blank=True, null=True)
    chirality = EnumField(Chirality, max_length=5, blank=True, null=True)
    connections = models.PositiveIntegerField(blank=True, null=True)
    base_ligand = models.ForeignKey(
        BaseLigand,
        on_delete=models.DO_NOTHING,
        db_column='base_ligand',
        related_name='ligands',
        blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ligand.views.details', args=[str(self.id)])

    @property
    def category_name(self):
        return self.category.__str__

    @property
    def functional_group_name(self):
        return self.functional_group.__str__

    @property
    def base_ligand_name(self):
        return self.base_ligand.__str__

    class Meta:
        db_table = 'Ligand'


class Mof(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True)
    nick = models.CharField(max_length=100, blank=True)
    formula = models.CharField(max_length=100, blank=True)
    synthesis = models.TextField(blank=True)
    analysis = models.TextField(blank=True)
    mass = models.FloatField(
        validators=[MinValueValidator(0.0)],
        blank=True, null=True)
    topology = models.CharField(max_length=10, blank=True)
    ligands = models.ManyToManyField(
        Ligand,
        through='MofLigand',
        through_fields=('mof', 'ligand'),
        related_name='mofs'
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('mof.views.details', args=[str(self.id)])

    @property
    def all_ligands(self):
        return ', '.join([a.name for a in self.ligands.all()])

    class Meta:
        db_table = 'Mof'


class MofLigand(models.Model):
    id = models.AutoField(primary_key=True)
    mof = models.ForeignKey(
        Mof,
        on_delete=models.DO_NOTHING)
    ligand = models.ForeignKey(
        Ligand,
        on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'Mof_Ligand'


class Reaction(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True)
    notes = models.TextField(blank=True)

    category = models.ForeignKey(
        ReactionCategory,
        on_delete=models.DO_NOTHING,
        related_name='reactions',
        blank=True, null=True)

    catalysts_cc = models.ManyToManyField(
        ChemicalCompound,
        through='ReactionCatalystCC',
        through_fields=('reaction', 'component'),
        related_name='reaction_catalysts',
        blank=True,
    )
    catalysts_ligand = models.ManyToManyField(
        Ligand,
        through='ReactionCatalystLigand',
        through_fields=('reaction', 'component'),
        related_name='reaction_catalysts',
        blank=True,
    )
    catalysts_mof = models.ManyToManyField(
        Mof,
        through='ReactionCatalystMof',
        through_fields=('reaction', 'component'),
        related_name='reaction_catalysts',
        blank=True,
    )
    reactants = models.ManyToManyField(
        ChemicalCompound,
        through='ReactionReactant',
        through_fields=('reaction', 'component'),
        related_name='reaction_reactants',
        blank=True,
    )
    products = models.ManyToManyField(
        ChemicalCompound,
        through='ReactionProduct',
        through_fields=('reaction', 'component'),
        related_name='reaction_products',
        blank=True,
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('reaction.views.details', args=[str(self.id)])

    @property
    def all_catalysts_cc(self):
        return ', '.join([a.name for a in self.catalysts_cc.all()])

    @property
    def all_catalysts_ligand(self):
        return ', '.join([a.name for a in self.catalysts_ligand.all()])

    @property
    def all_catalysts_mof(self):
        return ', '.join([a.name for a in self.catalysts_mof.all()])

    @property
    def all_reactants(self):
        return ', '.join([a.name for a in self.reactants.all()])

    @property
    def all_products(self):
        return ', '.join([a.name for a in self.products.all()])

    class Meta:
        db_table = 'Reaction'


class ReactionData(models.Model):
    id = models.AutoField(primary_key=True)
    reaction = models.ForeignKey(
        Reaction,
        on_delete=models.DO_NOTHING,
        blank=True, null=True)
    data_type = models.ForeignKey(
        DataType,
        on_delete=models.DO_NOTHING,
        blank=True)
    data_file = models.FileField(upload_to="reaction_data/")

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'ReactionData'


class ReactionCatalystCC(models.Model):
    id = models.AutoField(primary_key=True)
    reaction = models.ForeignKey(
        Reaction,
        on_delete=models.DO_NOTHING)
    component = models.ForeignKey(
        ChemicalCompound,
        on_delete=models.DO_NOTHING)
    rate_constant = models.FloatField(blank=True, null=True)
    conversion = models.FloatField(blank=True, null=True)
    ee = models.FloatField(blank=True, null=True)
    de = models.FloatField(blank=True, null=True)
    # yield renamed because it was a Python reserved word.
    yield_field = models.FloatField(db_column='yield', blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return str(self.id)

    @property
    def component_type(self):
        return ComponentType.CC.label

    @property
    def reaction_name(self):
        return self.reaction.name

    @property
    def reaction_category(self):
        return self.reaction.category

    @property
    def component_name(self):
        return self.component.name

    @property
    def component_nick(self):
        return self.component.nick

    @property
    def component_functional_group(self):
        return self.component.functional_group.name

    @property
    def component_chirality(self):
        return self.component.chirality

    @property
    def component_url(self):
        return self.component.get_absolute_url()

    class Meta:
        db_table = 'Reaction_Catalyst_CC'


class ReactionCatalystLigand(models.Model):
    id = models.AutoField(primary_key=True)
    reaction = models.ForeignKey(
        Reaction,
        on_delete=models.DO_NOTHING)
    component = models.ForeignKey(
        Ligand,
        on_delete=models.DO_NOTHING)
    rate_constant = models.FloatField(blank=True, null=True)
    conversion = models.FloatField(blank=True, null=True)
    ee = models.FloatField(blank=True, null=True)
    de = models.FloatField(blank=True, null=True)
    # yield renamed because it was a Python reserved word.
    yield_field = models.FloatField(db_column='yield', blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return str(self.id)

    @property
    def component_type(self):
        return ComponentType.LIGAND.label

    @property
    def reaction_name(self):
        return self.reaction.name

    @property
    def reaction_category(self):
        return self.reaction.category

    @property
    def component_name(self):
        return self.component.name

    @property
    def component_nick(self):
        return self.component.nick

    @property
    def component_functional_group(self):
        return self.component.functional_group.name

    @property
    def component_chirality(self):
        return self.component.chirality

    @property
    def component_url(self):
        return self.component.get_absolute_url()

    class Meta:
        db_table = 'Reaction_Catalyst_Ligand'


class ReactionCatalystMof(models.Model):
    id = models.AutoField(primary_key=True)
    reaction = models.ForeignKey(
        Reaction,
        on_delete=models.DO_NOTHING)
    component = models.ForeignKey(
        Mof,
        on_delete=models.DO_NOTHING)
    rate_constant = models.FloatField(blank=True, null=True)
    conversion = models.FloatField(blank=True, null=True)
    ee = models.FloatField(blank=True, null=True)
    de = models.FloatField(blank=True, null=True)
    # yield renamed because it was a Python reserved word.
    yield_field = models.FloatField(db_column='yield', blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return str(self.id)

    @property
    def component_type(self):
        return ComponentType.MOF.label

    @property
    def reaction_name(self):
        return self.reaction.name

    @property
    def reaction_category(self):
        return self.reaction.category

    @property
    def component_name(self):
        return self.component.name

    @property
    def component_nick(self):
        return self.component.nick

    @property
    def component_url(self):
        return self.component.get_absolute_url()

    class Meta:
        db_table = 'Reaction_Catalyst_Mof'


class ReactionProduct(models.Model):
    id = models.AutoField(primary_key=True)
    reaction = models.ForeignKey(
        Reaction,
        on_delete=models.DO_NOTHING)
    component = models.ForeignKey(
        ChemicalCompound,
        on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.id)

    @property
    def component_type(self):
        return ComponentType.PRODUCT.label

    @property
    def reaction_name(self):
        return self.reaction.name

    @property
    def reaction_category(self):
        return self.reaction.category.__str__

    @property
    def component_name(self):
        return self.component.name

    @property
    def component_nick(self):
        return self.component.nick

    @property
    def component_functional_group(self):
        return self.component.functional_group.name

    @property
    def component_chirality(self):
        return self.component.chirality

    @property
    def component_url(self):
        return self.component.get_absolute_url()

    class Meta:
        db_table = 'Reaction_Product'


class ReactionReactant(models.Model):
    id = models.AutoField(primary_key=True)
    reaction = models.ForeignKey(
        Reaction,
        on_delete=models.DO_NOTHING)
    component = models.ForeignKey(
        ChemicalCompound,
        on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.id)

    @property
    def component_type(self):
        return ComponentType.REACTANT.label

    @property
    def reaction_name(self):
        return self.reaction.name

    @property
    def reaction_category(self):
        return self.reaction.category.__str__

    @property
    def component_name(self):
        return self.component.name

    @property
    def component_nick(self):
        return self.component.nick

    @property
    def component_functional_group(self):
        return self.component.functional_group.name

    @property
    def component_chirality(self):
        return self.component.chirality

    @property
    def component_url(self):
        return self.component.get_absolute_url()

    class Meta:
        db_table = 'Reaction_Reactant'


class VisualizationCC(models.Model):
    id = models.AutoField(primary_key=True)
    chemical_compound = models.OneToOneField(
        ChemicalCompound,
        on_delete=models.DO_NOTHING,
        related_name="visualization")
    chemdraw = models.FileField(upload_to="visualization/cc/")

    class Meta:
        db_table = 'VisualizationCC'


class VisualizationLigand(models.Model):
    id = models.AutoField(primary_key=True)
    ligand = models.OneToOneField(
        Ligand,
        on_delete=models.DO_NOTHING,
        related_name="visualization")
    chemdraw = models.FileField(upload_to="visualization/ligand/")

    class Meta:
        db_table = 'VisualizationLigand'


class VisualizationMof(models.Model):
    id = models.AutoField(primary_key=True)
    mof = models.OneToOneField(
        Mof,
        on_delete=models.DO_NOTHING,
        related_name="visualization")
    cif = models.FileField(db_column='CIF',  # Field name made lowercase.
                           upload_to="visualization/mof/cif/")

    class Meta:
        db_table = 'VisualizationMof'


class VisualizationReaction(models.Model):
    id = models.AutoField(primary_key=True)
    reaction = models.OneToOneField(
        Reaction,
        on_delete=models.DO_NOTHING,
        related_name="visualization")
    chemdraw = models.FileField(upload_to="visualization/reaction/")

    class Meta:
        db_table = 'VisualizationReaction'

# class DjangoMigrations(models.Model):
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()
#
#     class Meta:
#         db_table = 'django_migrations'

# class ExperimentalData(models.Model):
#     id = models.AutoField(primary_key=True)
#     functional_group = models.ForeignKey(
#         FunctionalGroup,
#         on_delete=models.DO_NOTHING,
#         blank=True, null=True)
#     chirality = EnumField(Chirality, max_length=5, blank=True, null=True)
#     rate_constant = models.FloatField(blank=True, null=True)
#     conversion = models.FloatField(blank=True, null=True)
#     ee = models.FloatField(blank=True, null=True)
#     de = models.FloatField(blank=True, null=True)
#     # yield renamed because it was a Python reserved word.
#     yield_field = models.FloatField(db_column='yield', blank=True, null=True)
#     amount = models.FloatField(blank=True, null=True)
#
#     def __str__(self):
#         return str(self.id)
#
#     class Meta:
#         db_table = 'ExperimentalData'
