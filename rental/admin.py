from django.contrib import admin
from .models import Room, RoomReservation

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass

@admin.register(RoomReservation)
class ReservationAdmin(admin.ModelAdmin):
    pass