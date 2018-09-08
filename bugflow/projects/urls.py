from django.urls import path

app_name = 'projects'

from . import views

urlpatterns = [
    path('', views.add_project, name="new_project"),
]