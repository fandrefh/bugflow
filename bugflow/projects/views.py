from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ProjectForm

# Create your views here.

def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Projeto criado com sucesso.')
            return redirect('projects:new_project')
        
    form = ProjectForm()
    return render(request, 'projects/new_project.html', {'form': form})