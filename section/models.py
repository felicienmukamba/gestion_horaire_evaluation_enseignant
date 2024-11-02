from django.db import models
from django_softdelete.models import SoftDeleteModel
from users.models import Enseignant

class Section(SoftDeleteModel):
    designation = models.CharField(max_length=50)
    
    class Meta:
        ordering=('designation',)
    
    def __str__(self):
        return self.designation
    

class Secretaire_section(SoftDeleteModel):
    actif = models.BooleanField(default=True)
    enseignant=models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    
    class Meta:
            ordering=('section',)
    
    def __str__(self):
        return self.enseignant.nom



class Departement(SoftDeleteModel):
    designation = models.CharField(max_length=50)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    class Meta:
        ordering = ("designation",)

    def __str__(self):
        return self.designation
