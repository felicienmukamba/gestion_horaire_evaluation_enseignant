from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from section.models import Departement, Secretaire_section, Section
from users.models import Enseignant
from .forms import Secretaire_sectionForm, Secretaire_sectionForm, SectionForm, DepartementForm

# section views.
def section_save(request):
    if request.method == 'POST':
        form = SectionForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True,  'message': 'Ajout de du section reussie!'}) 
    else:
        form = SectionForm()
    return JsonResponse({'success': False,  'message': 'POST only supported!'}, 400) 

def section_delete(request, id):
    try:
        section_on_database = Section.objects.get(pk=id) 
        section_on_database.delete() 
        return JsonResponse({'success': True,  'message': 'section supprimé avec succès!'}) 
    except Section.DoesNotExist:
        return JsonResponse({'success': False, 'message': "section non supprimé."}, status=404)

def section_edit(request,id ):
    section_to_edit = get_object_or_404(Section, pk=id)
    print(request.POST)
    if request.method == 'POST':
        designation = request.POST.get('designation') 
        section_to_edit.designation = designation
        section_to_edit.save()
        return JsonResponse({'success': True, 'message': "section modifiée avec succès."})
    else:
        return JsonResponse({'success': False, 'message': "Une erreur est survenue. Veuillez corriger les champs du formulaire."})


# secretaire_section cours views.
def secretaire_section_save(request):
    if request.method == 'POST':
        form = Secretaire_sectionForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True,  'message': 'secretaire_section de du cours reussie!'}) 
    else:
        form = Secretaire_sectionForm()
    return JsonResponse({'success': False,  'message': 'POST only supported!'}, 400) 

def secretaire_section_delete(request, id):
    try:
        secretaire_section_on_database = Secretaire_section.objects.get(pk=id) 
        secretaire_section_on_database.delete() 
        return JsonResponse({'success': True,  'message': 'secretaire_section supprimé avec succès!'}) 
    except Departement.DoesNotExist:
        return JsonResponse({'success': False, 'message': "secretaire_section non supprimé."}, status=404)
    
def secretaire_section_edit(request, id):
    secretaire_section_to_edit = get_object_or_404(secretaire_section, pk=id)
    print(request.POST)
    if request.method == 'POST':
        section = request.POST.get('section')
        enseignant = request.POST.get('enseignant')
        secretaire_section = get_object_or_404(secretaire_section, pk=request.POST.get('secretaire_section'))
        secretaire_section_to_edit.enseignant = enseignant
        secretaire_section_to_edit.section = section
        secretaire_section_to_edit.secretaire_section = secretaire_section
        secretaire_section_to_edit.save()
        return JsonResponse({'success': True, 'message': "secretaire_section cours modifiée avec succès."})
    else:
        return JsonResponse({'success': False, 'message': "Une erreur est survenue. Veuillez corriger les champs du formulaire."})



# Departement cours views.
def departement_save(request):
    if request.method == 'POST':
        form = DepartementForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True,  'message': 'Departement de du cours reussie!'}) 
    else:
        form = DepartementForm()
    return JsonResponse({'success': False,  'message': 'POST only supported!'}, 400) 

def departement_delete(request, id):
    try:
        departement_on_database = Departement.objects.get(pk=id) 
        departement_on_database.delete() 
        return JsonResponse({'success': True,  'message': 'departement supprimé avec succès!'}) 
    except Departement.DoesNotExist:
        return JsonResponse({'success': False, 'message': "departement non supprimé."}, status=404)
    
def departement_edit(request, id):
    departement_to_edit = get_object_or_404(Departement, pk=id)
    print(request.POST)
    if request.method == 'POST':
        designation = request.POST.get('designation')
        section = get_object_or_404(section, pk=request.POST.get('section'))
        departement_to_edit.designation = designation
        departement_to_edit.section = section
        departement_to_edit.save()
        return JsonResponse({'success': True, 'message': "Departement cours modifiée avec succès."})
    else:
        return JsonResponse({'success': False, 'message': "Une erreur est survenue. Veuillez corriger les champs du formulaire."})


def section_list(request):
    context = {
        'sections': Section.objects.all(),
    }

    return render(request, 'sections/list.html', context)


def departement_list(request):
    context = {
        'departements': Departement.objects.all(),
        'sections': Section.objects.all(),
    }

    return render(request, 'sections/departement/list.html', context)


def secretaire_section_list(request):
    context = {
        'sections': Section.objects.all(),
        'secretaire_sections': Secretaire_section.objects.all(),
        'enseignants': Enseignant.objects.all(),
    }

    return render(request, 'sections/secretaire_section/list.html', context)
