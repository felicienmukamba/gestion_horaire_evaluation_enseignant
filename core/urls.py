from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from core.views import DashbordView, home


urlpatterns = [
    path("admin/", admin.site.urls),
    path("dashbord/", DashbordView.as_view(), name="dashbord"),
    path("", home, name="home"),
    path("", include("cours.urls")),
    path("", include("promotions.urls")),
    path("", include("horaire.urls")),
    path("", include("section.urls")),
    path("", include("salles.urls")),
    path("", include("anneeAcademiques.urls")),
    path("", include("users.urls")),
    path("", include("evaluation.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
