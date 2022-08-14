from typing import Any, Dict
from django.views.generic import TemplateView
from .models import RoomReservation


class PreviousReservationView(TemplateView):
    template_name = "reservations.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context['latest_reservations'] = RoomReservation.objects.all()
        return context
