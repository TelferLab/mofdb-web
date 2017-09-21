# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-21 01:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.RenameField(
            model_name='baseligand',
            old_name='base_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='baseligand',
            name='base_ligand',
        ),
        migrations.AlterField(
            model_name='ligand',
            name='base_ligand',
            field=models.ForeignKey(blank=True, db_column='base_ligand', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ligand', to='db.BaseLigand'),
        ),
        migrations.AlterField(
            model_name='ligand',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ligand', to='db.Category'),
        ),
        migrations.AlterField(
            model_name='ligand',
            name='functional_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ligand', to='db.FunctionalGroup'),
        ),
    ]
