from django.db import models
from django.utils import timezone
from django_softdelete.models import SoftDeleteModel
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)
from promotions.models import Promotion

class UserAccountManager(BaseUserManager):
    def create_user(
        self,
        login,  
        fonction,
        password=None,
    ):
        if fonction is None:
            fonction = "Internaute"

        login = login
        user = self.model(login=login, password=password, fonction=fonction)

        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, login, password, fonction="Admin"):
        user = self.create_user(
            login=login,
            password=password,
            fonction=fonction,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    login = models.CharField(max_length=50, unique=True)
    fonction = models.CharField(
        max_length=50,
        choices=[
            ("Internaute", "Internaute"),
            ("Etudiant", "Etudiant"),
            ("Enseignant", "Enseignant"),
            ("Secretaire_section", "Secretaire_section"),
            ("Admin", "Admin"),
        ],
        default="Internaute",
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = "login"
    REQUIRED_FIELDS = ["fonction"]

    class Meta:
        ordering = ("-login",)

    def __str__(self):
        return self.login


class Etudiant(User):
    matricule = models.CharField(max_length=10)
    nom = models.CharField(max_length=50)
    postnom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50, blank=True)
    sexe = models.CharField(
        max_length=50, choices=[("M", "Masculin"), ("F", "Feminin")]
    )
    telephone = models.CharField(max_length=15, unique=True)
    departement=models.ForeignKey("section.Departement", on_delete=models.CASCADE)
    promotion=models.ForeignKey(Promotion, on_delete=models.CASCADE)


class Enseignant(User):
    titreAcademique = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    postnom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50, blank=True)
    sexe = models.CharField(
        max_length=50, choices=[("M", "Masculin"), ("F", "Feminin")]
    )


class Disponibilite(models.Model):
    vacation = models.CharField(
        max_length=50, choices=[("Jour", "Jour"), ("Soir", "Soir")]
    )
    enseignant=models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    date = models.DateField()

    class Meta:
        ordering = ("-date",)