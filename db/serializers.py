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
    component_chirality = serializers.ReadOnlyField()

    class Meta:
        model = ReactionCatalystCC
        fields = '__all__'

class ReactionCatalystLigandSerializer(serializers.ModelSerializer):
    reaction_name = serializers.ReadOnlyField()
    component_name = serializers.ReadOnlyField()
    # component_name = serializers.HyperlinkedIdentityField(view_name='ligand.views.detail', format='html')
    component_functional_group = serializers.ReadOnlyField()
    component_type = serializers.ReadOnlyField()
    component_nick = serializers.ReadOnlyField()
    component_chirality = serializers.ReadOnlyField()

    class Meta:
        model = ReactionCatalystLigand
        fields = '__all__'

class ReactionCatalystMofSerializer(serializers.ModelSerializer):
    reaction_name = serializers.ReadOnlyField()
    component_name = serializers.ReadOnlyField()
    component_type = serializers.ReadOnlyField()
    component_nick = serializers.ReadOnlyField()

    class Meta:
        model = ReactionCatalystMof
        fields = '__all__'

class ReactionProductSerializer(serializers.ModelSerializer):
    reaction_name = serializers.ReadOnlyField()
    component_name = serializers.ReadOnlyField()
    component_functional_group = serializers.ReadOnlyField()
    component_type = serializers.ReadOnlyField()
    component_nick = serializers.ReadOnlyField()
    component_chirality = serializers.ReadOnlyField()

    class Meta:
        model = ReactionProduct
        fields = '__all__'

class ReactionReactantSerializer(serializers.ModelSerializer):
    reaction_name = serializers.ReadOnlyField()
    component_name = serializers.ReadOnlyField()
    component_functional_group = serializers.ReadOnlyField()
    component_type = serializers.ReadOnlyField()
    component_nick = serializers.ReadOnlyField()
    component_chirality = serializers.ReadOnlyField()

    class Meta:
        model = ReactionReactant
        fields = '__all__'


class ReactionSerializer(serializers.ModelSerializer):
    catalyst_cc = ReactionCatalystCCSerializer(read_only=True, many=True)

    class Meta:
        model = Reaction
        fields = ['name', 'catalyst_cc']
        # fields = '__all__'

