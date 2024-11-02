from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.http import JsonResponse ,HttpResponse
from django.shortcuts import redirect 
from django.contrib.auth.models import Group
from users.models import User
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def group_required(*group_names):
    def decorator(view_func):
        @login_required
        def wrapper(request, *args, **kwargs):
            if not request.user.groups.filter(name__in=group_names).exists():
                return redirect('not_found')
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator

def create_user(request):
    login = request.POST.get('login')
    password = request.POST.get('password')
    groups = request.POST.getlist('groups[]')  
    fonction = request.POST.getlist('fonction')  

    # Create the user
    user = User.objects.create_user(login=login, password=password, fonction=fonction)  # Replace with your password generation logic

    # Set user attributes
    user.fonction = fonction
    user.save()

    # Assign user to groups
    for group_id in groups:
        group = Group.objects.get(pk=group_id)
        user.groups.add(group)

    # Redirect or return a success message
    return JsonResponse({'success': True, 'message': 'Utilisateur créé avec succès'})



def login(request):

    if request.user.is_authenticated: 
            return redirect('home')
    
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')
        user = authenticate(request, login=login, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('dashbord')
        else:
            error_message = 'Utilisateur ou mot de passe incorrect'
            return render(request, 'user/auth/login/login.html', {'error_message': error_message})
    return render(request, "user/auth/login/login.html")

def logout_view(request):
    logout(request) 
    return  redirect('user-auth-login')
