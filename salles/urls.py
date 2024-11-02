from django.urls import path, include
from . import views
from django.conf.urls.static import static 
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [

    # salle urls
    path("salle/", views.salle_list, name="salle-list"),
    path("salle-add/", views.salle_save, name="salle-add"),
    path("salle-delete/<int:id>/", views.salle_delete, name="salle-delete"),
    path("salle-edit/<int:id>/", views.salle_edit, name="salle-edit"),
]