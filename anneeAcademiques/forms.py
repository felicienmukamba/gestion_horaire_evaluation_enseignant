from django import forms
from .models import AnneeAcademique

class AnneeAcademiqueForm(forms.ModelForm):
    class Meta:
        model = AnneeAcademique
        fields = '__all__'