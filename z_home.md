{% extends "base.html" %}

{% block content %}
<!-- home.html -->
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Accueil - Événement Spécial</title>
</head>
<body>
    <h1>{{ special_event.title }}</h1>
    <p><strong>Code de l'événement :</strong> {{ special_event.event_code }}</p>
    
    <h2>Inclus dans l'événement</h2>
    {% if included_items %}
        <ul>
            {% for item in included_items %}
                <li>{{ item }}</li>
            {% endfor %}
        </ul>
    {% else %}
        <p>Aucun élément inclus.</p>
    {% endif %}

    <h2>Exclus de l'événement</h2>
    {% if excluded_items %}
        <ul>
            {% for item in excluded_items %}
                <li>{{ item }}</li>
            {% endfor %}
        </ul>
    {% else %}
        <p>Aucun élément exclu.</p>
    {% endif %}

    <!-- Programme quotidien (TourDay) -->
    <h2>Programme</h2>
    {% if special_event.tour_days.count > 0 %}
        <ul>
            {% for day in special_event.tour_days.all %}
                <li>
                    <h3>Jour {{ day.day_number }}</h3>
                    <p><strong>Activité du matin :</strong> {{ day.morning_activity }}</p>
                    <p><strong>Activité de l'après-midi :</strong> {{ day.afternoon_activity }}</p>
                    <p><strong>Activité du soir :</strong> {{ day.evening_activity }}</p>
                </li>
            {% endfor %}
        </ul>
    {% else %}
        <p>Pas de programme pour cet événement.</p>
    {% endif %}

    <!-- Section VIP Pack, Hotel Pack, Tent Pack comme précédemment -->
</body>
</html>





{% endblock content %}



