from django.contrib import admin
from .models import Disponibilite, User, Etudiant, Enseignant

# Register your models here.
admin.site.register(User)
admin.site.register(Etudiant)
admin.site.register(Enseignant)
admin.site.register(Disponibilite)
