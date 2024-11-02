from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from anneeAcademiques.models import AnneeAcademique
from .forms import AnneeAcademiqueForm

# AnneeAcademiqueForm views.
def annee_academique_save(request):
    if request.method == 'POST':
        form = AnneeAcademiqueForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True,  'message': 'Ajout de du AnneeAcademiqueForm reussie!'}) 
    else:
        form = AnneeAcademiqueForm()
    return JsonResponse({'success': False,  'message': 'POST only supported!'}, 400) 

def annee_academique_delete(request, id):
    try:
        AnneeAcademiqueForm_on_database = AnneeAcademique.objects.get(pk=id) 
        AnneeAcademiqueForm_on_database.delete() 
        return JsonResponse({'success': True,  'message': 'AnneeAcademiqueForm supprimé avec succès!'}) 
    except AnneeAcademiqueForm.DoesNotExist:
        return JsonResponse({'success': False, 'message': "AnneeAcademiqueForm non supprimé."}, status=404)

def annee_academique_edit(request,id ):
    AnneeAcademiqueForm_to_edit = get_object_or_404(AnneeAcademique, pk=id)
    print(request.POST)
    if request.method == 'POST':
        designation = request.POST.get('designation') 
        AnneeAcademiqueForm_to_edit.designation = designation
        AnneeAcademiqueForm_to_edit.save()
        return JsonResponse({'success': True, 'message': "AnneeAcademiqueForm modifiée avec succès."})
    else:
        return JsonResponse({'success': False, 'message': "Une erreur est survenue. Veuillez corriger les champs du formulaire."})

def annee_academique_list(request):
    context = {
        'anneeacademique': AnneeAcademique.objects.all(),
    }

    return render(request, 'annee-academique/list.html', context)
