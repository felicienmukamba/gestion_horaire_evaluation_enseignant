from django.urls import path
from . import views

urlpatterns = [

    # Cours urls
    path("cours/", views.cours_list, name="cours-list"),
    path("cours-add/", views.cours_save, name="cours-add"),
    path("cours-delete/<int:id>/", views.cours_delete, name="cours-delete"),
    path("cours-edit/<int:id>/", views.cours_edit, name="cours-edit"),

    # Attribuer cours urls
    path("attribuer-cours/", views.attribuer_cours_list, name="attribuer-cours-list"),
    path("attribuer-cours-add/", views.attribuer_cours_save, name="attribuer-cours-add"),
    path("attribuer-cours-delete/<int:id>/", views.attribuer_cours_edit, name="attribuer-cours-delete"),
    path("attribuer-cours-edit/<int:id>/", views.attribuer_cours_delete, name="attribuer-cours-edit"),

    # Dispenser cours urls
    path("dispenser-cours/", views.dispenser_cours_list, name="dispenser-cours-list"),
    path("dispenser-cours-add/", views.dispenser_cours_save, name="dispenser-cours-add"),
    path("dispenser-cours-delete/<int:id>/", views.dispenser_cours_delete, name="dispenser-cours-delete"),
    path("dispenser-cours-edit/<int:id>/", views.dispenser_cours_edit, name="dispenser-cours-edit"),
]