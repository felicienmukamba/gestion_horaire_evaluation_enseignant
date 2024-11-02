from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.urls import reverse
from django.http import JsonResponse
from .models import Evaluation, Enseignant
from .forms import EvaluationForm
from datetime import datetime

@login_required
def soumettre_evaluation(request, enseignant_id):
    enseignant = get_object_or_404(Enseignant, id=enseignant_id)
    etudiant = request.user.etudiant

    if request.method == 'POST':
        form = EvaluationForm(request.POST)
        if form.is_valid():
            evaluation = form.save(commit=False)
            evaluation.etudiant = etudiant
            evaluation.enseignant = enseignant
            evaluation.save()
            return redirect('evaluation_detail', evaluation_id=evaluation.id)
    else:
        form = EvaluationForm()

    return render(request, 'evaluation/soumettre_evaluation.html', {'form': form, 'enseignant': enseignant})

@login_required
def evaluation_detail(request, evaluation_id):
    evaluation = get_object_or_404(Evaluation, id=evaluation_id)
    return render(request, 'evaluation/evaluation_detail.html', {'evaluation': evaluation})

@login_required
def evaluation_list(request):
    evaluations = Evaluation.objects.all().order_by('-date')
    paginator = Paginator(evaluations, 10)  # 10 evaluations per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    form = EvaluationForm()  

    context = {
        'evaluations': page_obj,
        'current_date': datetime.now(),
        'form': form,  # Add the form to the context
    }
    
    return render(request, 'evaluation/evaluation_list.html', context)

@login_required
def delete_evaluation(request, evaluation_id):
    if request.method == 'DELETE':
        evaluation = get_object_or_404(Evaluation, id=evaluation_id)
        evaluation.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'message': 'Invalid request'})
