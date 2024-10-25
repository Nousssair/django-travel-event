# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # La page d'accueil affiche maintenant l'événement unique
]
