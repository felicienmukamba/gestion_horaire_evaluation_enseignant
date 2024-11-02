from django.db import models
from users.models import Enseignant, Etudiant
from django.core.validators import MaxValueValidator, MinValueValidator

class Evaluation(models.Model):
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    note = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)])
    commentaire = models.TextField()
    date = models.DateField(auto_now_add=True)
    anonymat = models.BooleanField(default=True)

    def __str__(self):
        return f'Évaluation de {self.enseignant} par {self.etudiant}'

    class Meta:
        verbose_name = 'Évaluation'
        verbose_name_plural = 'Évaluations'
        ordering = ['date']