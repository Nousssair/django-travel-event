# views.py
from django.shortcuts import render
from .models import SpecialEvent

def home(request):
    special_event = SpecialEvent.objects.first()  # Assurez-vous d'obtenir un événement spécial

    # Diviser et nettoyer le champ include
    if special_event and special_event.include:
        included_items = [item.strip() for item in special_event.include.split(",")]
    else:
        included_items = []

    # Diviser et nettoyer le champ exclude
    if special_event and special_event.exclude:
        excluded_items = [item.strip() for item in special_event.exclude.split(",")]
    else:
        excluded_items = []

    return render(request, 'home.html', {
        'special_event': special_event,
        'included_items': included_items,  # Passer les éléments inclus à la template
        'excluded_items': excluded_items,    # Passer les éléments exclus à la template
    })
