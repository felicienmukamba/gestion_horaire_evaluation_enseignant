from django import forms
from django.contrib.auth import get_user_model

from users.models import Disponibilite, Enseignant, Etudiant

User = get_user_model()


class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['login', 'fonction']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if not password1 or not password2:
            raise forms.ValidationError('Please provide both password fields.')
        if password1 != password2:
            raise forms.ValidationError('Passwords do not match.')
        return password2

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['fonction']  # Update only the fonction field

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        # Disable editing of login field (assuming it should be unique and not changeable)
        self.fields['login'].disabled = True
        self.fields["intitule"].widget.attrs.update(
            {"class": "form-control", "placeholder": "intitule"})
        self.fields["semestre"].widget.attrs.update(
            {"class": "form-select", "id": "semestre"})
        self.fields["categorie"].widget.attrs.update(
            {"class": "form-control", "placeholder": "categorie"})


class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ['matricule', 'nom', 'postnom', 'prenom',
                  'sexe', 'telephone', 'departement', 'promotion', "login", "password"]

    def __init__(self, *args, **kwargs):
        super(EtudiantForm, self).__init__(*args, **kwargs)
        # Disable editing of login field (assuming it should be unique and not changeable)
        self.fields["matricule"].widget.attrs.update(
            {"class": "form-control", "placeholder": "matricule"})
        self.fields["nom"].widget.attrs.update(
            {"class": "form-control", "id": "nom"})
        self.fields["postnom"].widget.attrs.update(
            {"class": "form-control", "placeholder": "postnom"})
        self.fields["prenom"].widget.attrs.update(
            {"class": "form-control", "placeholder": "prenom"})
        self.fields["sexe"].widget.attrs.update(
            {"class": "form-control", "placeholder": "sexe"})
        self.fields["telephone"].widget.attrs.update(
            {"class": "form-control", "placeholder": "telephone"})
        self.fields["departement"].widget.attrs.update(
            {"class": "form-control", "placeholder": "departement"})
        self.fields["promotion"].widget.attrs.update(
            {"class": "form-control", "placeholder": "promotion"})
        self.fields["login"].widget.attrs.update(
            {"class": "form-control", "placeholder": "login"})
        self.fields["password"].widget = forms.PasswordInput(attrs=
            {"class": "form-control", "placeholder": "password"})

    def clean_telephone(self):
        telephone = self.cleaned_data['telephone']
        # Check for uniqueness (consider using a unique validator)
        if Etudiant.objects.filter(telephone=telephone).exists():
            raise forms.ValidationError('This phone number is already in use.')
        return telephone


class EnseignantForm(forms.ModelForm):
    class Meta:
        model = Enseignant
        fields = ['titreAcademique', 'nom', 'postnom', 'prenom', 'sexe', "login", "password"]

    def __init__(self, *args, **kwargs):
        super(EnseignantForm, self).__init__(*args, **kwargs)
        # Disable editing of login field (assuming it should be unique and not changeable)
        self.fields["titreAcademique"].widget.attrs.update(
            {"class": "form-control", "placeholder": "titreAcademique"})
        self.fields["nom"].widget.attrs.update(
            {"class": "form-control", "id": "nom", "placeholder": "nom"})
        self.fields["postnom"].widget.attrs.update(
            {"class": "form-control", "placeholder": "postnom"})
        self.fields["prenom"].widget.attrs.update(
            {"class": "form-control", "placeholder": "prenom"})
        self.fields["sexe"].widget.attrs.update(
            {"class": "form-control", "placeholder": "sexe"})
        self.fields["login"].widget.attrs.update(
            {"class": "form-control", "placeholder": "login"})
        self.fields["password"].widget = forms.PasswordInput(attrs=
            {"class": "form-control", "placeholder": "password"})


class DisponibiliteForm(forms.ModelForm):
    class Meta:
        model = Disponibilite
        fields = ['vacation', 'date', "enseignant"]

    def __init__(self, *args, **kwargs):
        super(DisponibiliteForm, self).__init__(*args, **kwargs)
        # Disable editing of login field (assuming it should be unique and not changeable)
        self.fields["vacation"].widget.attrs.update(
            {"class": "form-control", "placeholder": "vacation"})
        self.fields["date"].widget = forms.DateInput(
            attrs={"class": "form-control", "id": "date", "type": "date"})
        self.fields['enseignant'].queryset = Enseignant.objects.filter(
            is_active=True)  # Filter active teachers
        self.fields['enseignant'].widget.attrs.update(
            {"class": "form-select", "id": "date"})  # Filter active teachers