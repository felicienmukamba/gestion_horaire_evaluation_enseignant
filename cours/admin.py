from django.contrib import admin
from .models import Cours, Dispenser,Attribuer
# Register your models here.
admin.site.register(Dispenser)
admin.site.register(Attribuer)
admin.site.register(Cours)