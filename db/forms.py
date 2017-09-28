from django.forms import ModelForm
from db.models import Reaction

class ReactionForm(ModelForm):
    class Meta:
        model = Reaction
        fields = '__all__'
