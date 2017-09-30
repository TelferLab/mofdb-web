from rest_framework import serializers
from db.models import (Reaction,
                       ReactionCatalystCC,
                       ReactionCatalystLigand,
                       ReactionCatalystMof,
                       ReactionProduct,
                       ReactionReactant)


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

