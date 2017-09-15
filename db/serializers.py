from rest_framework import serializers
from db.models import (ReactionCatalystCC,
                       ReactionCatalystLigand,
                       ReactionCatalystMof,
                       ReactionProduct,
                       ReactionReactant)

class ReactionCatalystCCSerializer(serializers.ModelSerializer):
    reaction_name = serializers.ReadOnlyField()
    component_name = serializers.ReadOnlyField()
    functional_group_name = serializers.ReadOnlyField()
    component_type = serializers.ReadOnlyField()

    class Meta:
        model = ReactionCatalystCC
        fields = '__all__'

class ReactionCatalystLigandSerializer(serializers.ModelSerializer):
    reaction_name = serializers.ReadOnlyField()
    component_name = serializers.ReadOnlyField()
    functional_group_name = serializers.ReadOnlyField()
    component_type = serializers.ReadOnlyField()

    class Meta:
        model = ReactionCatalystLigand
        fields = '__all__'

class ReactionCatalystMofSerializer(serializers.ModelSerializer):
    reaction_name = serializers.ReadOnlyField()
    component_name = serializers.ReadOnlyField()
    functional_group_name = serializers.ReadOnlyField()
    component_type = serializers.ReadOnlyField()

    class Meta:
        model = ReactionCatalystMof
        fields = '__all__'

class ReactionProductSerializer(serializers.ModelSerializer):
    reaction_name = serializers.ReadOnlyField()
    component_name = serializers.ReadOnlyField()
    functional_group_name = serializers.ReadOnlyField()
    component_type = serializers.ReadOnlyField()

    class Meta:
        model = ReactionProduct
        fields = '__all__'

class ReactionReactantSerializer(serializers.ModelSerializer):
    reaction_name = serializers.ReadOnlyField()
    component_name = serializers.ReadOnlyField()
    functional_group_name = serializers.ReadOnlyField()
    component_type = serializers.ReadOnlyField()

    class Meta:
        model = ReactionReactant
        fields = '__all__'
