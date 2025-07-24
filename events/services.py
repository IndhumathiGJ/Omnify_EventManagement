from .models import Event, Attendee
from django.core.exceptions import ValidationError

def register_attendee(event_id, name, email):
    event = Event.objects.get(id=event_id)
    if event.attendees.count() >= event.max_capacity:
        raise ValidationError("Event is fully booked.")

    if Attendee.objects.filter(event=event, email=email).exists():
        raise ValidationError("This email is already registered for the event.")

    attendee = Attendee.objects.create(event=event, name=name, email=email)
    return attendee
