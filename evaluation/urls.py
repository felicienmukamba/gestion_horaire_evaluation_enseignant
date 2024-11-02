from django.urls import path
from .views import soumettre_evaluation, evaluation_detail, evaluation_list, delete_evaluation

urlpatterns = [
    path('soumettre_evaluation/<int:enseignant_id>/', soumettre_evaluation, name='soumettre_evaluation'),
    path('evaluation/<int:evaluation_id>/', evaluation_detail, name='evaluation_detail'),
    path('evaluations/', evaluation_list, name='evaluation_list'),
    path('evaluation-delete/<int:evaluation_id>/', delete_evaluation, name='evaluation_delete'),
]
