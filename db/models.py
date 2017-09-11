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

class Chirality(Enum):
    R = 'right'
    L = 'left'
    NONE = 'none'


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Category'
        verbose_name_plural = "Category"
        verbose_name_plural = "Categories"


class ChemicalCompound(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    nick = models.CharField(max_length=45, blank=True, null=True)
    formula = models.CharField(max_length=45, blank=True, null=True)
    synthesis = models.TextField(blank=True, null=True)
    analysis = models.TextField(blank=True, null=True)
    mass = models.FloatField(
        validators=[MinValueValidator(0.0)],
        blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ChemicalCompound'


class DataType(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.type

    class Meta:
        db_table = 'DataType'


class FunctionalGroup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'FunctionalGroup'


class BaseLigand(models.Model):
    id = models.AutoField(primary_key=True)
    base_name = models.CharField(max_length=200, blank=True, null=True)
    base_ligand = models.ForeignKey(
        'Ligand',
        on_delete=models.DO_NOTHING,
        blank=True, null=True)

    def __str__(self):
        return self.base_name

    class Meta:
        db_table = 'BaseLigand'


class Ligand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    nick = models.CharField(max_length=45, blank=True, null=True)
    formula = models.CharField(max_length=45, blank=True, null=True)
    synthesis = models.TextField(blank=True, null=True)
    analysis = models.TextField(blank=True, null=True)
    mass = models.FloatField(
        validators=[MinValueValidator(0.0)],
        blank=True, null=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.DO_NOTHING,
        blank=True, null=True)

    functional_group = models.ForeignKey(
        FunctionalGroup,
        on_delete=models.DO_NOTHING,
        blank=True, null=True)
    connections = models.PositiveIntegerField(blank=True, null=True)
    chirality = EnumField(Chirality, max_length=5, blank=True, null=True)
    base_ligand = models.ForeignKey(
        BaseLigand,
        on_delete=models.DO_NOTHING,
        db_column='base_ligand',
        blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Ligand'


class Mof(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    nick = models.CharField(max_length=45, blank=True, null=True)
    formula = models.CharField(max_length=45, blank=True, null=True)
    synthesis = models.TextField(blank=True, null=True)
    analysis = models.TextField(blank=True, null=True)
    mass = models.FloatField(
        validators=[MinValueValidator(0.0)],
        blank=True, null=True)
    topology = models.TextField(blank=True, null=True)
    ligands = models.ManyToManyField(
        Ligand,
        through='MofLigand',
        through_fields=('mof', 'ligand')
    )

    def __str__(self):
        return self.name

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
    name = models.CharField(max_length=200, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    catalysts_cc = models.ManyToManyField(
        ChemicalCompound,
        through='ReactionCatalystCC',
        through_fields=('reaction_id', 'catalyst_cc_id'),
        related_name='catalysts_cc',
        blank=True,
    )
    catalysts_ligand = models.ManyToManyField(
        Ligand,
        through='ReactionCatalystLigand',
        through_fields=('reaction_id', 'catalyst_ligand_id'),
        related_name='catalysts_ligands',
        blank=True,
    )
    catalysts_mof = models.ManyToManyField(
        Mof,
        through='ReactionCatalystMof',
        through_fields=('reaction_id', 'catalyst_mof_id'),
        related_name='catalysts_mofs',
        blank=True,
    )
    reactants = models.ManyToManyField(
        ChemicalCompound,
        through='ReactionReactant',
        through_fields=('reaction_id', 'reactant_id'),
        related_name='reactants',
        blank=True,
    )
    products = models.ManyToManyField(
        ChemicalCompound,
        through='ReactionProduct',
        through_fields=('reaction_id', 'product_id'),
        related_name='products',
        blank=True,
    )

    def __str__(self):
        return self.name

    # @property
    # def all_components(self):
    #     return ', '.join([reactionligand.experimental_data_id for reactionligand in self.catalysts_ligand.all()])


    class Meta:
        db_table = 'Reaction'


class ReactionData(models.Model):
    id = models.AutoField(primary_key=True)
    reaction_id = models.ForeignKey(
        Reaction,
        on_delete=models.CASCADE,
        blank=True, null=True)
    data_type = models.ForeignKey(
        DataType,
        on_delete=models.DO_NOTHING,
        blank=True)
    data_file = models.FileField()

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'ReactionData'


class ExperimentalData(models.Model):
    id = models.AutoField(primary_key=True)
    functional_group_id = models.ForeignKey(
        FunctionalGroup,
        on_delete=models.DO_NOTHING,
        blank=True, null=True)
    chirality = EnumField(Chirality, max_length=5, blank=True, null=True)
    rate_constant = models.FloatField(blank=True, null=True)
    conversion = models.FloatField(blank=True, null=True)
    ee = models.FloatField(blank=True, null=True)
    de = models.FloatField(blank=True, null=True)
    # yield renamed because it was a Python reserved word.
    yield_field = models.FloatField(db_column='yield', blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'ExperimentalData'


class ReactionCatalystCC(models.Model):
    id = models.AutoField(primary_key=True)
    reaction_id = models.ForeignKey(
        Reaction,
        on_delete=models.DO_NOTHING)
    catalyst_cc_id = models.ForeignKey(
        ChemicalCompound,
        on_delete=models.DO_NOTHING)
    experimental_data_id = models.ForeignKey(
        ExperimentalData,
        on_delete=models.DO_NOTHING,
        related_name='data_cc',
        db_column='ExperimentalData',
        blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'Reaction_Catalyst_CC'


class ReactionCatalystLigand(models.Model):
    id = models.AutoField(primary_key=True)
    reaction_id = models.ForeignKey(
        Reaction,
        on_delete=models.DO_NOTHING)
    catalyst_ligand_id = models.ForeignKey(
        Ligand,
        on_delete=models.DO_NOTHING)
    experimental_data_id = models.ForeignKey(
        ExperimentalData,
        on_delete=models.DO_NOTHING,
        related_name='data_ligand',
        db_column='ExperimentalData',
        blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'Reaction_Catalyst_Ligand'


class ReactionCatalystMof(models.Model):
    id = models.AutoField(primary_key=True)
    reaction_id = models.ForeignKey(
        Reaction,
        on_delete=models.DO_NOTHING)
    catalyst_mof_id = models.ForeignKey(
        Mof,
        on_delete=models.DO_NOTHING)
    experimental_data_id = models.ForeignKey(
        ExperimentalData,
        on_delete=models.DO_NOTHING,
        related_name='data_mof',
        db_column='ExperimentalData',
        blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'Reaction_Catalyst_Mof'


class ReactionProduct(models.Model):
    id = models.AutoField(primary_key=True)
    reaction_id = models.ForeignKey(
        Reaction,
        on_delete=models.DO_NOTHING)
    product_id = models.ForeignKey(
        ChemicalCompound,
        on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'Reaction_Product'


class ReactionReactant(models.Model):
    id = models.AutoField(primary_key=True)
    reaction = models.ForeignKey(
        Reaction,
        on_delete=models.DO_NOTHING)
    reactant = models.ForeignKey(
        ChemicalCompound,
        on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'Reaction_Reactant'


class VisualizationCC(models.Model):
    id_chemical_compound = models.OneToOneField(
        ChemicalCompound,
        on_delete=models.DO_NOTHING,
        primary_key=True)
    chemdraw = models.FileField()

    class Meta:
        db_table = 'VisualizationCC'


class VisualizationLigand(models.Model):
    id_ligand = models.OneToOneField(
        Ligand,
        on_delete=models.DO_NOTHING,
        primary_key=True)
    chemdraw = models.FileField()

    class Meta:
        db_table = 'VisualizationLigand'


class VisualizationMof(models.Model):
    id_mof = models.OneToOneField(
        Mof,
        on_delete=models.DO_NOTHING,
        primary_key=True)
    cif = models.FileField(db_column='CIF')  # Field name made lowercase.

    class Meta:
        db_table = 'VisualizationMof'


class VisualizationReaction(models.Model):
    id_reaction = models.OneToOneField(
        Reaction,
        on_delete=models.DO_NOTHING,
        primary_key=True)
    chemdraw = models.FileField()

    class Meta:
        db_table = 'VisualizationReaction'

# class DjangoMigrations(models.Model):
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()
#
#     class Meta:
#         db_table = 'django_migrations'
