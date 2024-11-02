from django.contrib import admin

from section.models import Departement, Section, Secretaire_section

# Register your models here.
admin.site.register(Section)
admin.site.register(Secretaire_section)
admin.site.register(Departement)
