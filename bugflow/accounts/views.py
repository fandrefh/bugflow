from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

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
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        messages.success(request, 'Login feito com sucesso.')
        return redirect('accounts:user-profile')
    else:
        print('Deu caca!!!!')
        messages.error(request, 'Login não realizado.')
    return render(request, 'home/index.html')

def user_logout(request):
    logout(request)
    return redirect('/')


def user_profile(request):
    user = User.objects.get(username=request.user)
    return render(request, 'accounts/user_profile.html', {'user': user})
