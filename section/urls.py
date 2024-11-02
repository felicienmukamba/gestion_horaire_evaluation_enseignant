from django.urls import path, include
from . import views
from django.conf.urls.static import static 
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [

    # section urls
    path("section/", views.section_list, name="section-list"),
    path("section-add/", views.section_save, name="section-add"),
    path("section-delete/<int:id>/", views.section_delete, name="section-delete"),
    path("section-edit/<int:id>/", views.section_edit, name="section-edit"),

    # secretaire_section urls
    path("secretaire_section/", views.secretaire_section_list, name="secretaire_section-list"),
    path("secretaire_section-add/", views.secretaire_section_save, name="secretaire_section-add"),
    path("secretaire_section-delete/<int:id>/", views.secretaire_section_edit, name="secretaire_section-delete"),
    path("secretaire_section-edit/<int:id>/", views.secretaire_section_delete, name="secretaire_section-edit"),

    # departement urls
    path("departement/", views.departement_list, name="departement-list"),
    path("departement-add/", views.departement_save, name="departement-add"),
    path("departement-delete/<int:id>/", views.departement_delete, name="departement-delete"),
    path("departement-edit/<int:id>/", views.departement_edit, name="departement-edit"),
]
