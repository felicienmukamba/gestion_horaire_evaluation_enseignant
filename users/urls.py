from django.urls import path, include

from users import user_views
urlpatterns = [

    # Users urls
    path("user/auth/login/", user_views.login, name="user-auth-login"),
    path("user/auth/logout/", user_views.logout, name="user-auth-logout"),
    # path("user/auth/register/", views.create_user, name="user-auth-register"),

    # disponibilite urls
    path("user/disponibilite-add/", user_views.DisponibiliteCreateView.as_view(), name="disponibilite-add"),
    path("user/disponibilite/", user_views.DisponibiliteListView.as_view(), name="disponibilite-list"),
    path("user/disponibilite-edit/<int:pk>/", user_views.DisponibiliteUpdateView.as_view(), name="disponibilite-edit"),


    # disponibilite urls
    path("user/etudiant-add/", user_views.EtudiantCreateView.as_view(), name="etudiant-add"),
    path("user/etudiant/", user_views.EtudiantListView.as_view(), name="etudiant-list"),
    path("user/etudiant-edit/<int:pk>/", user_views.EtudiantUpdateView.as_view(), name="etudiant-edit"),

    
    # disponibilite urls
    path("user/enseignant-add/", user_views.EnseignantCreateView.as_view(), name="enseignant-add"),
    path("user/enseignant/", user_views.EnseignantListView.as_view(), name="enseignant-list"),
    path("user/enseignant-edit/<int:pk>/", user_views.EnseignantUpdateView.as_view(), name="enseignant-edit"),
]