from django.test import TestCase
from django.urls import reverse

from rental.models import Room, RoomReservation



class ViewTests(TestCase):
    def test_latest_reservations(self):
        room = Room.objects.create(ref="Room-1")
        reservation1 = RoomReservation.objects.create(
            reservation_ref="res-1",
            checkin_date="2022-01-01",
            checkout_date="2022-01-13",
            room=room,
        )
        response = self.client.get(reverse("previous-reservation"))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context["latest_reservations"], [reservation1])
