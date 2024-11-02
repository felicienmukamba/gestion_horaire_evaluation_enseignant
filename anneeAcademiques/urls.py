from django.urls import path, include
from . import views
from django.conf.urls.static import static 
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [

    # annee-academique urls
    path("annee-academique/", views.annee_academique_list, name="annee-academique-list"),
    path("annee-academique-add/", views.annee_academique_save, name="annee-academique-add"),
    path("annee-academique-delete/<int:id>/", views.annee_academique_delete, name="annee-academique-delete"),
    path("annee-academique-edit/<int:id>/", views.annee_academique_edit, name="annee-academique-edit"),
]
