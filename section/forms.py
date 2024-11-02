from django import forms
from .models import Section, Secretaire_section, Departement

class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = '__all__'

class Secretaire_sectionForm(forms.ModelForm):
    class Meta:
        model = Secretaire_section
        fields = '__all__'
        
class DepartementForm(forms.ModelForm):
    class Meta:
        model = Departement
        fields = '__all__'