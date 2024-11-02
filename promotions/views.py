from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from promotions.models import Promotion
from .forms import PromotionForm

# promotion views.

def promotion_list(request):
    context = {
        'promotions': Promotion.objects.all(),
    }

    return render(request, 'promotions/list.html', context)

def promotion_save(request):
    if request.method == 'POST':
        form = PromotionForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True,  'message': 'Ajout de du promotion reussie!'}) 
    else:
        form = PromotionForm()
    return JsonResponse({'success': False,  'message': 'POST only supported!'}, 400) 

def promotion_delete(request, id):
    try:
        promotion_on_database = Promotion.objects.get(pk=id) 
        promotion_on_database.delete() 
        return JsonResponse({'success': True,  'message': 'promotion supprimé avec succès!'}) 
    except Promotion.DoesNotExist:
        return JsonResponse({'success': False, 'message': "promotion non supprimé."}, status=404)

def promotion_edit(request,id ):
    promotion_to_edit = get_object_or_404(Promotion, pk=id)
    print(request.POST)
    if request.method == 'POST':
        designation = request.POST.get('designation') 
        promotion_to_edit.designation = designation
        promotion_to_edit.save()
        return JsonResponse({'success': True, 'message': "promotion modifiée avec succès."})
    else:
        return JsonResponse({'success': False, 'message': "Une erreur est survenue. Veuillez corriger les champs du formulaire."})

