from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from anneeAcademiques.models import AnneeAcademique
from cours.models import Attribuer, Cours, Dispenser
from section.models import Departement
from promotions.models import Promotion
from salles.models import Salle
from users.models import Enseignant
from .forms import CoursForm, AttribuerForm, DispenserForm

# Cours views.
def cours_save(request):
    if request.method == 'POST':
        form = CoursForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True,  'message': 'Ajout de du cours reussie!'}) 
    else:
        form = CoursForm()
    return JsonResponse({'success': False,  'message': 'POST only supported!'}, 400) 

def cours_delete(request, id):
    try:
        Cours_on_database = Cours.objects.get(pk=id) 
        Cours_on_database.delete() 
        return JsonResponse({'success': True,  'message': 'cours supprimé avec succès!'}) 
    except Cours.DoesNotExist:
        return JsonResponse({'success': False, 'message': "cours non supprimé."}, status=404)

def cours_edit(request,id ):
    cours_to_edit = get_object_or_404(Cours, pk=id)
    print(request.POST)
    if request.method == 'POST':
        designation = request.POST.get('designation') 
        cours_to_edit.designation = designation
        cours_to_edit.save()
        return JsonResponse({'success': True, 'message': "Cours modifiée avec succès."})
    else:
        return JsonResponse({'success': False, 'message': "Une erreur est survenue. Veuillez corriger les champs du formulaire."})


# Attribuer cours views.
def attribuer_cours_save(request):
    if request.method == 'POST':
        form = AttribuerForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True,  'message': 'Attribuer de du cours reussie!'}) 
    else:
        form = AttribuerForm()
    return JsonResponse({'success': False,  'message': 'POST only supported!'}, 400) 

def attribuer_cours_delete(request, id):
    try:
        Attribuer_cours_on_database = Attribuer.objects.get(pk=id) 
        Attribuer_cours_on_database.delete() 
        return JsonResponse({'success': True,  'message': 'Attribuer_cours supprimé avec succès!'}) 
    except Cours.DoesNotExist:
        return JsonResponse({'success': False, 'message': "Attribuer_cours non supprimé."}, status=404)
    
def attribuer_cours_edit(request,id):
    attribuer_cours_to_edit = get_object_or_404(Attribuer, pk=id)
    print(request.POST)
    if request.method == 'POST':
        nbreHeure = request.POST.get('nbreHeure')
        cours = get_object_or_404(Cours, pk=request.POST.get('cours'))
        anneeAcademique = get_object_or_404(AnneeAcademique, pk=request.POST.get('anneeAcademique'))
        promotion = get_object_or_404(Promotion, pk=request.POST.get('promotion'))
        departement = get_object_or_404(Departement, pk=request.POST.get('departement'))
        enseignant = get_object_or_404(Enseignant, pk=request.POST.get('enseignant'))
        attribuer_cours_to_edit.nbreHeure = int(nbreHeure)
        attribuer_cours_to_edit.cours = cours
        attribuer_cours_to_edit.anneeAcademique = anneeAcademique
        attribuer_cours_to_edit.promotion = promotion
        attribuer_cours_to_edit.departement = departement
        attribuer_cours_to_edit.enseignant = enseignant
        attribuer_cours_to_edit.save()
        return JsonResponse({'success': True, 'message': "Attribuer cours modifiée avec succès."})
    else:
        return JsonResponse({'success': False, 'message': "Une erreur est survenue. Veuillez corriger les champs du formulaire."})


# Disppenser cours views.
def dispenser_cours_save(request):
    if request.method == 'POST':
        form = DispenserForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True,  'message': 'Dispenser du cours reussie!'}) 
    else:
        form = DispenserForm()
    return JsonResponse({'success': False,  'message': 'POST only supported!'}, 400) 

def dispenser_cours_delete(request, id):
    try:
        Dispenser_cours_on_database = Dispenser.objects.get(pk=id) 
        Dispenser_cours_on_database.delete() 
        return JsonResponse({'success': True,  'message': 'Dispenser_cours supprimé avec succès!'}) 
    except Cours.DoesNotExist:
        return JsonResponse({'success': False, 'message': "Dispenser_cours non supprimé."}, status=404)

def dispenser_cours_edit(request,id):
    dispenser_cours_to_edit = get_object_or_404(Dispenser, pk=id)
    print(request.POST)
    if request.method == 'POST':
        nbreHeure = request.POST.get('nbreHeure')
        cours = get_object_or_404(Cours, pk=request.POST.get('cours'))
        anneeAcademique = get_object_or_404(AnneeAcademique, pk=request.POST.get('anneeAcademique'))
        promotion = get_object_or_404(Promotion, pk=request.POST.get('promotion'))
        departement = get_object_or_404(Departement, pk=request.POST.get('departement'))
        salle = get_object_or_404(Salle, pk=request.POST.get('salle'))
        dispenser_cours_to_edit.nbreHeure = int(nbreHeure)
        dispenser_cours_to_edit.cours = cours
        dispenser_cours_to_edit.anneeAcademique = anneeAcademique
        dispenser_cours_to_edit.promotion = promotion
        dispenser_cours_to_edit.departement = departement
        dispenser_cours_to_edit.salle = salle
        dispenser_cours_to_edit.save()
        return JsonResponse({'success': True, 'message': "Dispenser cours modifiée avec succès."})
    else:
        return JsonResponse({'success': False, 'message': "Une erreur est survenue. Veuillez corriger les champs du formulaire."})

def cours_list(request):
    context = {
        'cours': Cours.objects.all(),
        'attribuers': Attribuer.objects.all(),
        'dispensers': Dispenser.objects.all(),
    }

    return render(request, 'cours/list.html', context)


def attribuer_cours_list(request):
    context = {
        'cours': Cours.objects.all(),
        'attribuers': Attribuer.objects.all(),
        'anneeAcademiques': AnneeAcademique.objects.all(),
        'enseignants': Enseignant.objects.all(),
        'promotions': Promotion.objects.all(),
        'departements': Departement.objects.all(),
    }

    return render(request, 'cours/attribuer-cours/list.html', context)


def dispenser_cours_list(request):
    context = {
        'cours': Cours.objects.all(),
        'attribuers': Attribuer.objects.all(),
        'salles': Salle.objects.all(),
        'dispensers': Dispenser.objects.all(),
        'promotions': Promotion.objects.all(),
        'departements': Departement.objects.all(),
        'anneeAcademiques': AnneeAcademique.objects.all(),

    }

    return render(request, 'cours/dispenser-cours/list.html', context)
