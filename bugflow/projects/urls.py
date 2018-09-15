from django.urls import path

app_name = 'projects'

from . import views

urlpatterns = [
    path('', views.projects_list, name="projects_list"),
    path('novo/', views.add_project, name="new_project"),
    path('excluir/<int:pk>/', views.confirm_and_delete_project, name="delete_project"),
    path('editar/<int:pk>/', views.update_project, name="update_project"),
]
