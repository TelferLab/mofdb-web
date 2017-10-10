from haystack import indexes
from db.models import Reaction
from db.models import Mof
from db.models import Ligand
from db.models import ChemicalCompound


class MofIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    date_creation = indexes.DateTimeField(model_attr='date_creation')
    date_last_modified = indexes.DateTimeField(model_attr='date_last_modified')

    def get_model(self):
        return Mof


class LigandIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    date_creation = indexes.DateTimeField(model_attr='date_creation')
    date_last_modified = indexes.DateTimeField(model_attr='date_last_modified')

    def get_model(self):
        return Ligand


class ChemicalCompoundIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    date_creation = indexes.DateTimeField(model_attr='date_creation')
    date_last_modified = indexes.DateTimeField(model_attr='date_last_modified')

    def get_model(self):
        return ChemicalCompound


class ReactionIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    date_creation = indexes.DateTimeField(model_attr='date_creation')
    date_last_modified = indexes.DateTimeField(model_attr='date_last_modified')

    def get_model(self):
        return Reaction
