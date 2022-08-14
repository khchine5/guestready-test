from django.db import models


class Room(models.Model):

    ref = models.CharField("Ref", max_length=50)

    def __str__(self) -> str:
        return self.ref


class RoomReservation(models.Model):

    reservation_ref = models.CharField("Reservation Ref", max_length=50)
    checkin_date = models.DateField("Checkin date")
    checkout_date = models.DateField("Checkout date")
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, related_name="reservations"
    )

    property
    def preview_reservation(self):
        return self.room.reservations.filter(checkin_date__lt=self.checkin_date).last()

    def __str__(self) -> str:
        return f"({self.room.pk}, {self.checkin_date}, {self.checkout_date})"

    class Meta:
        ordering = ("room", "checkin_date")
