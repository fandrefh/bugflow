from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import ( 
    authenticate, login, logout,
    update_session_auth_hash
)
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm

from .forms import UserForm, EditUserForm

# Create your views here.

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            u = form.save()
            u.set_password(u.password)
            u.save()
            messages.success(request, 'Conta criada com sucesso!')
            return redirect('accounts:add-user')
        else:
            print(form.errors)
    else:
        form = UserForm()
    return render(request, 'accounts/add_user.html', {'form': form})

@login_required
def edit_user(request):
    user = get_object_or_404(User, username=request.user)
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil alterado com sucesso.')
            return redirect('accounts:user-profile')
    form = EditUserForm(instance=user)
    return render(request, 'accounts/edit_user.html', {'form': form})

def user_login(request):
    next_url = request.GET.get('next')
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login feito com sucesso.')
            print('Próxima URL:', next_url)
            return redirect(request.GET.get(next_url, 'accounts:user-profile'))
        else:
            messages.error(request, 'Login não realizado. Usuário ou senha inválido.')
            return redirect('accounts:error-login')
    
    return render(request, 'accounts/user_login.html')

def error_login(request):
    return render(request, 'accounts/user_login.html', {})

def user_logout(request):
    logout(request)
    return redirect('/')

def user_profile(request):
    user = User.objects.get(username=request.user)
    return render(request, 'accounts/user_profile.html', {'user': user})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Senha alterada com sucesso.')
            return redirect('accounts:user-profile')
        else:
            messages.error(request, 'Alteração não realizada.')
            
    form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {'form': form})
