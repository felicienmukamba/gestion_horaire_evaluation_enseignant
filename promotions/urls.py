from django.urls import path, include
from . import views
from django.conf.urls.static import static 
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [

    # promotion urls
    path("promotion/", views.promotion_list, name="promotion-list"),
    path("promotion-add/", views.promotion_save, name="promotion-add"),
    path("promotion-delete/<int:id>/", views.promotion_delete, name="promotion-delete"),
    path("promotion-edit/<int:id>/", views.promotion_edit, name="promotion-edit"),
]