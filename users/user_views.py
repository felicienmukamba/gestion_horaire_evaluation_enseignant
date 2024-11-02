from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Etudiant, Enseignant, Disponibilite
from .forms import UserRegistrationForm, UserUpdateForm, EtudiantForm, EnseignantForm, DisponibiliteForm
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required



# Vues pour les étudiants
class EtudiantListView(ListView):
    model = Etudiant
    context_object_name = "etudiants"
    template_name = 'user/etudiant/list.html'


class EtudiantCreateView(CreateView):
    model = Etudiant
    form_class = EtudiantForm
    template_name = 'user/etudiant/add.html'
    success_url = reverse_lazy('etudiant-list')

class EtudiantUpdateView(UpdateView):
    model = Etudiant
    form_class = EtudiantForm
    template_name = 'user/etudiant/edit.html'
    success_url = reverse_lazy('etudiant-list')

# Vues pour les enseignants
class EnseignantListView(ListView):
    model = Enseignant
    context_object_name = "enseignants"
    template_name = 'user/enseignant/list.html'



class EnseignantCreateView(CreateView):
    model = Enseignant
    form_class = EnseignantForm
    template_name = 'user/enseignant/add.html'
    success_url = reverse_lazy('enseignant-list')
    

class EnseignantUpdateView(UpdateView):
    model = Enseignant
    form_class = EnseignantForm
    template_name = 'user/enseignant/edit.html'
    success_url = reverse_lazy('enseignant-list')


# Vues pour les disponibilités
class DisponibiliteListView(ListView):
    model = Disponibilite
    context_object_name = "disponibilites"
    template_name = 'user/disponibilite/list.html'

class DisponibiliteCreateView(CreateView):
    model = Disponibilite
    form_class = DisponibiliteForm
    template_name = 'user/disponibilite/add.html'
    success_url = reverse_lazy('disponibilite-list')

class DisponibiliteUpdateView(UpdateView):
    model = Disponibilite
    form_class = DisponibiliteForm
    template_name = 'user/disponibilite/edit.html'
    success_url = reverse_lazy('disponibilite-list')

class DisponibiliteDeleteView(DeleteView):
    model = Disponibilite
    success_url = reverse_lazy('disponibilite_list')

# Vues pour les utilisateurs
class UserListView(ListView):
    model = User
    template_name = 'user_list.html'

class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'

class UserCreateView(CreateView):
    model = User
    form_class = UserRegistrationForm
    success_url = reverse_lazy('user_list')

class UserUpdateView(UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('user_list')

class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('user_list')




def login(request):
    if request.user.is_authenticated: 
        return redirect('home')
    
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('dashbord')
        else:
            error_message = 'Utilisateur ou mot de passe incorrect'
            return render(request, 'user/auth/login/login.html', {'error_message': error_message})
        
    return render(request, "user/auth/login/login.html")

@login_required(login_url='user-auth-login')
def logout(request):
    auth.logout(request)
    return redirect('user-auth-login')