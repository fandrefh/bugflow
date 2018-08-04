from django.urls import path

from bugflow.accounts import views

app_name = 'accounts'

urlpatterns = [
    path('novo/', views.add_user, name='add-user'),
]