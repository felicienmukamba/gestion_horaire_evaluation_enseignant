from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from salles.models import Salle
from .forms import SalleForm

# salle views.

def salle_list(request):
    context = {
        'salles': Salle.objects.all(),
    }

    return render(request, 'salles/list.html', context)

def salle_save(request):
    if request.method == 'POST':
        form = SalleForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True,  'message': 'Ajout de du salle reussie!'}) 
    else:
        form = SalleForm()
    return JsonResponse({'success': False,  'message': 'POST only supported!'}, 400) 

def salle_delete(request, id):
    try:
        salle_on_database = Salle.objects.get(pk=id) 
        salle_on_database.delete() 
        return JsonResponse({'success': True,  'message': 'salle supprimé avec succès!'}) 
    except Salle.DoesNotExist:
        return JsonResponse({'success': False, 'message': "salle non supprimé."}, status=404)

def salle_edit(request,id ):
    salle_to_edit = get_object_or_404(Salle, pk=id)
    print(request.POST)
    if request.method == 'POST':
        designation = request.POST.get('designation') 
        salle_to_edit.designation = designation
        salle_to_edit.save()
        return JsonResponse({'success': True, 'message': "salle modifiée avec succès."})
    else:
        return JsonResponse({'success': False, 'message': "Une erreur est survenue. Veuillez corriger les champs du formulaire."})

