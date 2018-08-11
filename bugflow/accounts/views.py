from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import UserForm

# Create your views here.

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conta criada com sucesso!')
            return redirect('accounts:add-user')
        else:
            print(form.errors)
    else:
        form = UserForm()
    return render(request, 'accounts/add_user.html', {'form': form})
