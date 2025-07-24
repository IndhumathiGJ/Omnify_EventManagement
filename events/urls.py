from django.urls import path
from .views import *

urlpatterns = [
    path('createevent', EventCreateView.as_view()),
    path('events/', EventListView.as_view()),
    path('events/<int:event_id>/register', RegisterAttendeeView.as_view()),
    path('events/<int:event_id>/attendees', AttendeeListView.as_view()),
]
