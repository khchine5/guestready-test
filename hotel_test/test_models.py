from rental.models import Room, RoomReservation
import pytest


@pytest.mark.django_db
def test_create_room():
    room = Room.objects.create(ref="Room-1")
    assert room.ref == "Room-1"


@pytest.mark.django_db
def test_create_reservation():
    room = Room.objects.create(ref="Room-1")
    reservation1 = RoomReservation.objects.create(
        reservation_ref="res-1",
        checkin_date="2022-01-01",
        checkout_date="2022-01-13",
        room=room,
    )
    assert room.ref == "Room-1"
    assert reservation1.room == room
