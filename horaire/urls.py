from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import *


urlpatterns = [
    path("horaires", Horaire.as_view(), name="horaire-list"),
    path("horaires/now", HoraireWeek.as_view()),
]

