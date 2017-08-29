# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-29 05:55
from __future__ import unicode_literals

import db.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import enumfields.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseLigand',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('base_name', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'BaseLigand',
            },
        ),
        migrations.CreateModel(
            name='CatalystData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('functional_group_id', models.IntegerField(blank=True, null=True)),
                ('chirality', enumfields.fields.EnumField(blank=True, enum=db.models.Chirality, max_length=5, null=True)),
                ('rate_constant', models.FloatField(blank=True, null=True)),
                ('conversion', models.FloatField(blank=True, null=True)),
                ('ee_field', models.FloatField(blank=True, null=True)),
                ('de_field', models.FloatField(blank=True, null=True)),
                ('yield_field', models.FloatField(blank=True, db_column='yield', null=True)),
                ('amount', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'CatalystData',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'db_table': 'Category',
            },
        ),
        migrations.CreateModel(
            name='ChemicalCompound',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('nick', models.CharField(blank=True, max_length=45, null=True)),
                ('formula', models.CharField(blank=True, max_length=45, null=True)),
                ('synthesis', models.TextField(blank=True, null=True)),
                ('analysis', models.TextField(blank=True, null=True)),
                ('mass', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0.0)])),
            ],
            options={
                'db_table': 'ChemicalCompound',
            },
        ),
        migrations.CreateModel(
            name='DataType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'DataType',
            },
        ),
        migrations.CreateModel(
            name='FunctionalGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'FunctionalGroup',
            },
        ),
        migrations.CreateModel(
            name='Ligand',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('nick', models.CharField(blank=True, max_length=45, null=True)),
                ('formula', models.CharField(blank=True, max_length=45, null=True)),
                ('synthesis', models.TextField(blank=True, null=True)),
                ('analysis', models.TextField(blank=True, null=True)),
                ('mass', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('connections', models.PositiveIntegerField(blank=True, null=True)),
                ('chirality', enumfields.fields.EnumField(blank=True, enum=db.models.Chirality, max_length=5, null=True)),
            ],
            options={
                'db_table': 'Ligand',
            },
        ),
        migrations.CreateModel(
            name='Mof',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('nick', models.CharField(blank=True, max_length=45, null=True)),
                ('formula', models.CharField(blank=True, max_length=45, null=True)),
                ('synthesis', models.TextField(blank=True, null=True)),
                ('analysis', models.TextField(blank=True, null=True)),
                ('mass', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('topology', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Mof',
            },
        ),
        migrations.CreateModel(
            name='MofLigand',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Mof_Ligand',
            },
        ),
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Reaction',
            },
        ),
        migrations.CreateModel(
            name='ReactionCatalystCC',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Reaction_Catalyst_CC',
            },
        ),
        migrations.CreateModel(
            name='ReactionCatalystLigand',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('notes', models.TextField(blank=True, null=True)),
                ('catalyst_data_id', models.ForeignKey(db_column='catalyst_data', on_delete=django.db.models.deletion.DO_NOTHING, related_name='data_ligand', to='db.CatalystData')),
            ],
            options={
                'db_table': 'Reaction_Catalyst_Ligand',
            },
        ),
        migrations.CreateModel(
            name='ReactionCatalystMof',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('notes', models.TextField(blank=True, null=True)),
                ('catalyst_data_id', models.ForeignKey(db_column='catalyst_data', on_delete=django.db.models.deletion.DO_NOTHING, related_name='data_mof', to='db.CatalystData')),
            ],
            options={
                'db_table': 'Reaction_Catalyst_Mof',
            },
        ),
        migrations.CreateModel(
            name='ReactionData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data_file', models.FileField(upload_to='')),
                ('data_type', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='db.DataType')),
            ],
            options={
                'db_table': 'ReactionData',
            },
        ),
        migrations.CreateModel(
            name='ReactionProduct',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Reaction_Product',
            },
        ),
        migrations.CreateModel(
            name='ReactionReactant',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Reaction_Reactant',
            },
        ),
        migrations.CreateModel(
            name='VisualizationCC',
            fields=[
                ('id_chemical_compound', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='db.ChemicalCompound')),
                ('chemdraw', models.FileField(upload_to='')),
            ],
            options={
                'db_table': 'VisualizationCC',
            },
        ),
        migrations.CreateModel(
            name='VisualizationLigand',
            fields=[
                ('id_ligand', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='db.Ligand')),
                ('chemdraw', models.FileField(upload_to='')),
            ],
            options={
                'db_table': 'VisualizationLigand',
            },
        ),
        migrations.CreateModel(
            name='VisualizationMof',
            fields=[
                ('id_mof', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='db.Mof')),
                ('cif', models.FileField(db_column='CIF', upload_to='')),
            ],
            options={
                'db_table': 'VisualizationMof',
            },
        ),
        migrations.CreateModel(
            name='VisualizationReaction',
            fields=[
                ('id_reaction', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='db.Reaction')),
                ('chemdraw', models.FileField(upload_to='')),
            ],
            options={
                'db_table': 'VisualizationReaction',
            },
        ),
        migrations.AddField(
            model_name='reactionreactant',
            name='reactant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='db.ChemicalCompound'),
        ),
        migrations.AddField(
            model_name='reactionreactant',
            name='reaction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='db.Reaction'),
        ),
        migrations.AddField(
            model_name='reactionproduct',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='db.ChemicalCompound'),
        ),
        migrations.AddField(
            model_name='reactionproduct',
            name='reaction_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='db.Reaction'),
        ),
        migrations.AddField(
            model_name='reactiondata',
            name='reaction_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='db.Reaction'),
        ),
        migrations.AddField(
            model_name='reactioncatalystmof',
            name='catalyst_mof_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='db.Mof'),
        ),
        migrations.AddField(
            model_name='reactioncatalystmof',
            name='reaction_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='db.Reaction'),
        ),
        migrations.AddField(
            model_name='reactioncatalystligand',
            name='catalyst_ligand_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='db.Ligand'),
        ),
        migrations.AddField(
            model_name='reactioncatalystligand',
            name='reaction_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='db.Reaction'),
        ),
        migrations.AddField(
            model_name='reactioncatalystcc',
            name='catalyst_cc_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='db.ChemicalCompound'),
        ),
        migrations.AddField(
            model_name='reactioncatalystcc',
            name='catalyst_data_id',
            field=models.ForeignKey(db_column='catalyst_data', on_delete=django.db.models.deletion.DO_NOTHING, related_name='data_cc', to='db.CatalystData'),
        ),
        migrations.AddField(
            model_name='reactioncatalystcc',
            name='reaction_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='db.Reaction'),
        ),
        migrations.AddField(
            model_name='reaction',
            name='catalysts_cc',
            field=models.ManyToManyField(blank=True, related_name='catalysts_cc', through='db.ReactionCatalystCC', to='db.ChemicalCompound'),
        ),
        migrations.AddField(
            model_name='reaction',
            name='catalysts_ligand',
            field=models.ManyToManyField(blank=True, related_name='catalysts_ligands', through='db.ReactionCatalystLigand', to='db.Ligand'),
        ),
        migrations.AddField(
            model_name='reaction',
            name='catalysts_mof',
            field=models.ManyToManyField(blank=True, related_name='catalysts_mofs', through='db.ReactionCatalystMof', to='db.Mof'),
        ),
        migrations.AddField(
            model_name='reaction',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='products', through='db.ReactionProduct', to='db.ChemicalCompound'),
        ),
        migrations.AddField(
            model_name='reaction',
            name='reactants',
            field=models.ManyToManyField(blank=True, related_name='reactants', through='db.ReactionReactant', to='db.ChemicalCompound'),
        ),
        migrations.AddField(
            model_name='mofligand',
            name='ligand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='db.Ligand'),
        ),
        migrations.AddField(
            model_name='mofligand',
            name='mof',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='db.Mof'),
        ),
        migrations.AddField(
            model_name='mof',
            name='ligands',
            field=models.ManyToManyField(through='db.MofLigand', to='db.Ligand'),
        ),
        migrations.AddField(
            model_name='ligand',
            name='base_ligand',
            field=models.ForeignKey(blank=True, db_column='base_ligand', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='db.BaseLigand'),
        ),
        migrations.AddField(
            model_name='ligand',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='db.Category'),
        ),
        migrations.AddField(
            model_name='ligand',
            name='functional_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='db.FunctionalGroup'),
        ),
        migrations.AddField(
            model_name='baseligand',
            name='base_ligand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='db.Ligand'),
        ),
    ]
