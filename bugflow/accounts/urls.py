from django.urls import path

from bugflow.accounts import views

app_name = 'accounts'

urlpatterns = [
    path('novo/', views.add_user, name='add-user'),
    path('login/', views.user_login, name='user-login'),
    path('logout/', views.user_logout, name='user-logout'),
    path('profile/', views.user_profile, name='user-profile'),
]