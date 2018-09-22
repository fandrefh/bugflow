from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib.auth.models import User

from .forms import ProjectForm, ProjectUpdateForm
from .models import Project

# Create your views here.

@login_required
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.status = 'EE'
            f.save()
            messages.success(request, 'Projeto criado com sucesso.')
            return redirect('projects:projects_list')
        else:
            print(form.errors)
    form = ProjectForm()
    return render(request, 'projects/new_project.html', {'form': form})

@login_required
def projects_list(request):
    template_name = 'projects/projects_list.html'
    projects = Project.objects.filter(user__username=request.user)
    number_projects = Project.objects.count()
    context = {
        'projects': projects,
        'number_projects': number_projects,
    }
    return render(request, template_name, context)

@login_required
def confirm_and_delete_project(request, pk):
    template_name = 'projects/confirm_and_delete_project.html'
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        raise Http404()

    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Registro excluído.')
        return redirect('projects:projects_list')
    
    context = {
        'project': project,
    }
    
    return render(request, template_name, context)

@login_required
def update_project(request, pk):
    template_name = 'projects/new_project.html'
    try:
        project = get_object_or_404(Project, pk=pk)
    except Project.DoesNotExist:
        raise Http404()

    if request.user == project.user:
        if request.method == 'POST':
            form = ProjectUpdateForm(request.POST, instance=project)
            if form.is_valid():
                f = form.save(commit=False)
                f.user = project.user
                f.save()
                messages.success(request, 'Projeto editado com sucesso.')
                return redirect('projects:projects_list')
            else:
                print(form.errors)
    else:
        messages.info(request, 'Você não tem permissão acessar o projeto.')
        return redirect('projects:projects_list')
    
    form = ProjectUpdateForm(instance=project)
    
    context = {
        'form': form,
    }

    return render(request, template_name, context)
