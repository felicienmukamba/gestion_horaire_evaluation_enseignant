from django.db import models
from django_softdelete.models import SoftDeleteModel
from anneeAcademiques.models import AnneeAcademique
from section.models import Departement
from promotions.models import Promotion
from salles.models import Salle
from anneeAcademiques.models import AnneeAcademique
from users.models import Enseignant

# Create your models here.
class Cours(SoftDeleteModel):
    designation = models.CharField(max_length=50)

    class Meta:
        ordering = ("designation",)

    def __str__(self):
        return self.designation


class Attribuer(SoftDeleteModel):
    nbreHeure = models.IntegerField()
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    anneeAcademique = models.ForeignKey(AnneeAcademique, on_delete=models.CASCADE)
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE)
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)

    class Meta:
        ordering = ("-id",)


class Dispenser(SoftDeleteModel):
    vacation = models.CharField(
        max_length=50, choices=[("Jour", "Jour"), ("Soir", "Soir")]
    )
    prester = models.BooleanField(default=False)
    date = models.DateField()
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    anneeAcademique = models.ForeignKey(AnneeAcademique, on_delete=models.CASCADE)
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE)
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE)

    class Meta:
        ordering = ("-date",)
