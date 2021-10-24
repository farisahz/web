from . import views
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index, name="index"),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('login/', views.login, name='login'),
    path('signup/',views.signup, name='signup'),
    path('logout/', views.logout, name = 'logout'),
    
    
]