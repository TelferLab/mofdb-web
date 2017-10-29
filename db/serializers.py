from rest_framework import serializers
from db.models import (Mof, MofLigand)
from db.models import (Reaction,
                       ReactionCatalystCC,
                       ReactionCatalystLigand,
                       ReactionCatalystMof,
                       ReactionProduct,
                       ReactionReactant)

######## MOF ######
class MofLigandSerializer(serializers.ModelSerializer):
    mof_name = serializers.ReadOnlyField()
    ligand_name = serializers.ReadOnlyField()
    ligand_nick = serializers.ReadOnlyField()
    ligand_functional_group = serializers.ReadOnlyField()
    ligand_url = serializers.HyperlinkedIdentityField(view_name='ligand.views.details', format='html')

    class Meta:
        model = MofLigand
        fields = '__all__'

class MofSerializer(serializers.ModelSerializer):
    ligands = MofLigandSerializer(source="mofligand_set", many=True, read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='mof.views.details', format='html')
    url_ligands_table = serializers.HyperlinkedIdentityField(view_name='mof.views.ligandstable', format='html')

    class Meta:
        model = Mof
        fields = '__all__'

######## REACTION ######

class ReactionCatalystCCSerializer(serializers.ModelSerializer):
    reaction_name = serializers.ReadOnlyField()
    component_name = serializers.ReadOnlyField()
    component_functional_group = serializers.ReadOnlyField()
    component_type = serializers.ReadOnlyField()
    component_nick = serializers.ReadOnlyField()
    component_url = serializers.HyperlinkedIdentityField(view_name='chemicalcompound.views.details', format='html')

    class Meta:
        model = ReactionCatalystCC
        fields = '__all__'

class ReactionCatalystLigandSerializer(serializers.ModelSerializer):
    reaction_name = serializers.ReadOnlyField()
    component_name = serializers.ReadOnlyField()
    component_functional_group = serializers.ReadOnlyField()
    component_type = serializers.ReadOnlyField()
    component_nick = serializers.ReadOnlyField()
    component_url = serializers.HyperlinkedIdentityField(view_name='ligand.views.details', format='html')

    class Meta:
        model = ReactionCatalystLigand
        fields = '__all__'

class ReactionCatalystMofSerializer(serializers.ModelSerializer):
    reaction_name = serializers.ReadOnlyField()
    component_name = serializers.ReadOnlyField()
    component_type = serializers.ReadOnlyField()
    component_nick = serializers.ReadOnlyField()
    component_url = serializers.HyperlinkedIdentityField(view_name='mof.views.details', format='html')

    class Meta:
        model = ReactionCatalystMof
        fields = '__all__'

class ReactionProductSerializer(serializers.ModelSerializer):
    reaction_name = serializers.ReadOnlyField()
    component_name = serializers.ReadOnlyField()
    component_functional_group = serializers.ReadOnlyField()
    component_type = serializers.ReadOnlyField()
    component_nick = serializers.ReadOnlyField()
    component_url = serializers.HyperlinkedIdentityField(view_name='chemicalcompound.views.details', format='html')

    class Meta:
        model = ReactionProduct
        fields = '__all__'

class ReactionReactantSerializer(serializers.ModelSerializer):
    reaction_name = serializers.ReadOnlyField()
    component_name = serializers.ReadOnlyField()
    component_functional_group = serializers.ReadOnlyField()
    component_type = serializers.ReadOnlyField()
    component_nick = serializers.ReadOnlyField()
    component_url = serializers.HyperlinkedIdentityField(view_name='chemicalcompound.views.details', format='html')

    class Meta:
        model = ReactionReactant
        fields = '__all__'


class ReactionSerializer(serializers.ModelSerializer):
    catalysts_cc = ReactionCatalystCCSerializer(source="reactioncatalystcc_set", many=True, read_only=True)
    catalysts_ligand = ReactionCatalystLigandSerializer(source="reactioncatalystligand_set", many=True, read_only=True)
    catalysts_mof = ReactionCatalystMofSerializer(source="reactioncatalystmof_set", many=True, read_only=True)
    reactants = ReactionReactantSerializer(source="reactants_set", many=True, read_only=True)
    products = ReactionProductSerializer(source="products_set", many=True, read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='reaction.views.details', format='html')
    url_catalysts_table = serializers.HyperlinkedIdentityField(view_name='reaction.views.catalyststable', format='html')
    url_products_table = serializers.HyperlinkedIdentityField(view_name='reaction.views.productstable', format='html')
    url_reactants_table = serializers.HyperlinkedIdentityField(view_name='reaction.views.reactantstable', format='html')

    class Meta:
        model = Reaction
        # fields = ('name', 'catalyst_ligands')
        fields = '__all__'

