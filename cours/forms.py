from django import forms

from anneeAcademiques.models import AnneeAcademique
from section.models import Departement
from promotions.models import Promotion
from salles.models import Salle
from users.models import Enseignant
from .models import Cours, Attribuer, Dispenser


class CoursForm(forms.ModelForm):
    class Meta:
        model = Cours
        fields = '__all__'


class AttribuerForm(forms.ModelForm):
    class Meta:
        model = Attribuer
        fields = '__all__'
        fields = ["nbreHeure", "cours", "anneeAcademique", "promotion", "departement", "enseignant",]
    
    def __init__(self, *args, **kwargs):
        super(AttribuerForm, self).__init__(*args, **kwargs)
        # Disable editing of login field (assuming it should be unique and not changeable)
        self.fields["nbreHeure"].widget.attrs.update({"class": "form-control", "placeholder": "nbreHeure"})
        self.fields['cours'].queryset = Cours.objects.all() # Filter active teachers
        self.fields['anneeAcademique'].queryset = AnneeAcademique.objects.all() # Filter active teachers
        self.fields['promotion'].queryset = Promotion.objects.all() # Filter active teachers
        self.fields['departement'].queryset = Departement.objects.all()
        self.fields['enseignant'].queryset = Enseignant.objects.all()


class DispenserForm(forms.ModelForm):
    class Meta:
        model = Dispenser
        fields = ["vacation", "prester", "date", "cours", "anneeAcademique", "promotion", "departement", "salle",]

    def __init__(self, *args, **kwargs):
        super(DispenserForm, self).__init__(*args, **kwargs)
        # Disable editing of login field (assuming it should be unique and not changeable)
        self.fields["vacation"].widget.attrs.update({"class": "form-control", "placeholder": "vacation"})
        self.fields["prester"].widget = forms.CheckboxInput(attrs={"class": "form-control", "id": "date", "type": "date"})
        self.fields['date'].queryset = forms.DateInput(attrs={"class": "form-control", "id": "date", "type": "date"}) # Filter active teachers
        self.fields['cours'].queryset = Cours.objects.all() # Filter active teachers
        self.fields['anneeAcademique'].queryset = AnneeAcademique.objects.all() # Filter active teachers
        self.fields['promotion'].queryset = Promotion.objects.all() # Filter active teachers
        self.fields['departement'].queryset = Departement.objects.all()
        self.fields['salle'].queryset = Salle.objects.all()