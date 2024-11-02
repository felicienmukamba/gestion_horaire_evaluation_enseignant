from django.db import models
from django_softdelete.models import SoftDeleteModel

# Create your models here.


class AnneeAcademique(SoftDeleteModel):
    designation = models.CharField(max_length=50)

    class Meta:
        ordering = ("-id",)

    def __str__(self):
        return self.designation
