from django.contrib import admin
from .models import *

@admin.register(VIPPack)
class VIPPackAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'vip_access', 'private_driver')
    list_filter = ('vip_access', 'private_driver')
    search_fields = ('name',)

@admin.register(HotelPack)
class HotelPackAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'room_type', 'hotel_rating')
    list_filter = ('room_type', 'meal_plan')
    search_fields = ('name',)

@admin.register(TentPack)
class TentPackAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'tent_size', 'camp_location')
    list_filter = ('camp_location',)
    search_fields = ('name',)

@admin.register(SpecialEvent)
class SpecialEventAdmin(admin.ModelAdmin):
    list_display = ('event_code', 'title', 'location', 'price', 'start_date', 'end_date')
    list_filter = ('currency', 'start_date', 'end_date')
    search_fields = ('title', 'location', 'event_code')

@admin.register(TourDay)
class TourDayAdmin(admin.ModelAdmin):
    list_display = ('event', 'day_number', 'morning_activity', 'afternoon_activity', 'evening_activity')
    list_filter = ('event',)
    search_fields = ('event__title', 'day_number')
