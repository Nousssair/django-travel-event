from django.db import models


class VIPPack(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nom du package")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix")
    vip_access = models.BooleanField(default=False, verbose_name="Accès VIP")
    private_driver = models.BooleanField(default=False, verbose_name="Chauffeur privé")
    luxury_amenities = models.TextField(verbose_name="Services de luxe", blank=True, null=True)
    exclusive_experience = models.TextField(verbose_name="Expérience exclusive", blank=True, null=True)
    special_requests = models.TextField(verbose_name="Demandes spéciales", blank=True, null=True)

    class Meta:
        verbose_name = "Package VIP"
        verbose_name_plural = "Packages VIP"

    def __str__(self):
        return self.name
    
    
class HotelPack(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nom du package")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix")
    room_type = models.CharField(max_length=255, verbose_name="Type de chambre", choices=[('single', 'Simple'), ('double', 'Double'), ('suite', 'Suite')])
    number_of_rooms = models.PositiveIntegerField(verbose_name="Nombre de chambres")
    hotel_rating = models.DecimalField(max_digits=2, decimal_places=1, verbose_name="Évaluation de l'hôtel")
    meal_plan = models.CharField(max_length=255, verbose_name="Type de pension", choices=[('half_board', 'Demi-pension'), ('full_board', 'Pension complète'), ('all_inclusive', 'Tout inclus')])
    facilities = models.TextField(verbose_name="Installations de l'hôtel", blank=True, null=True)

    # Nouveaux champs
    number_of_adults = models.PositiveIntegerField(verbose_name="Nombre d'adultes")
    number_of_children = models.PositiveIntegerField(verbose_name="Nombre d'enfants", blank=True, null=True)
    children_ages = models.CharField(max_length=255, verbose_name="Âge des enfants", help_text="Séparer les âges des enfants par des virgules", blank=True, null=True)

    class Meta:
        verbose_name = "Package Hôtel"
        verbose_name_plural = "Packages Hôtel"

    def __str__(self):
        return self.name
    
class TentPack(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nom du package")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix")
    tent_size = models.CharField(max_length=255, verbose_name="Taille de la tente")
    number_of_tents = models.PositiveIntegerField(verbose_name="Nombre de tentes")
    tent_amenities = models.TextField(verbose_name="Équipements de la tente", blank=True, null=True)
    camp_location = models.CharField(max_length=255, verbose_name="Lieu du campement")

    class Meta:
        verbose_name = "Package Tente"
        verbose_name_plural = "Packages Tente"

    def __str__(self):
        return self.name
    
    

class SpecialEvent(models.Model):
    # Champs principaux (comme déjà définis)
    event_code = models.CharField(max_length=100, unique=True, verbose_name="Code de l'événement")
    title = models.CharField(max_length=200, verbose_name="Titre de l'événement")
    location = models.CharField(max_length=255, verbose_name="Lieu de l'événement")
    duration = models.PositiveIntegerField(verbose_name="Nombre de jours de l'événement")
    group_size = models.PositiveIntegerField(verbose_name="Taille du groupe")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix")

    CURRENCY_CHOICES = [
        ('USD', 'USD'),
        ('EUR', 'EUR'),
        ('TND', 'TND'),
    ]
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, verbose_name="Devise")
    start_date = models.DateField(verbose_name="Date de début")
    end_date = models.DateField(verbose_name="Date de fin")
    start_time = models.TimeField(verbose_name="Heure de début")
    end_time = models.TimeField(verbose_name="Heure de fin")
    description = models.TextField(verbose_name="Description de l'événement", blank=True, null=True)
    include = models.TextField(verbose_name="Inclus dans l'événement", blank=True, null=True)
    exclude = models.TextField(verbose_name="Exclus de l'événement", blank=True, null=True)

    # Informations sur l'organisateur
    contact_email = models.EmailField(verbose_name="Email de contact", blank=True, null=True)
    contact_phone = models.CharField(max_length=15, verbose_name="Téléphone de contact", blank=True, null=True)
    organizer = models.CharField(max_length=200, verbose_name="Organisateur", blank=True, null=True)
    website = models.URLField(verbose_name="Site Web de l'événement", blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Dernière mise à jour")
    
    vip_pack = models.ForeignKey(VIPPack, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Package VIP")
    hotel_pack = models.ForeignKey(HotelPack, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Package Hôtel")
    tent_pack = models.ForeignKey(TentPack, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Package Tente")
    def __str__(self):
        return f"{self.title} - {self.event_code}"

class TourDay(models.Model):
    event = models.ForeignKey(SpecialEvent, related_name="tour_days", on_delete=models.CASCADE, verbose_name="Événement")
    day_number = models.PositiveIntegerField(verbose_name="Numéro du jour")
    morning_activity = models.TextField(verbose_name="Activités du matin", blank=True, null=True)
    afternoon_activity = models.TextField(verbose_name="Activités de l'après-midi", blank=True, null=True)
    evening_activity = models.TextField(verbose_name="Activités du soir", blank=True, null=True)

    def __str__(self):
        return f"Jour {self.day_number} - {self.event.title}"
    

    class Meta:
        unique_together = ['event', 'day_number']
        ordering = ['day_number']