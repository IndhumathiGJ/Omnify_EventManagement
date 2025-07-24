from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Event, Attendee
from .serializers import EventSerializer, AttendeeSerializer
from .services import register_attendee
from django.utils.timezone import now
from django.core.paginator import Paginator

class EventCreateView(generics.CreateAPIView):
    serializer_class = EventSerializer


class EventListView(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.all().order_by('start_time')


class RegisterAttendeeView(APIView):
    def post(self, request, event_id):
        try:
            attendee = register_attendee(
                event_id,
                name=request.data.get("name"),
                email=request.data.get("email")
            )
            return Response({"message": "Registration successful"}, status=201)
        except Exception as e:
            return Response({"error": str(e)}, status=400)


class AttendeeListView(APIView):
    def get(self, request, event_id):
        page = int(request.GET.get("page", 1))
        limit = int(request.GET.get("limit", 10))
        attendees = Attendee.objects.filter(event_id=event_id)
        paginator = Paginator(attendees, limit)
        page_data = paginator.get_page(page)
        serializer = AttendeeSerializer(page_data, many=True)
        return Response({
            "count": paginator.count,
            "page": page,
            "results": serializer.data
        })
