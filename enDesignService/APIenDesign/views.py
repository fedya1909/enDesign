from rest_framework import generics
from . import serializers
from django.contrib.auth.models import User
from .models import Ticket

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class TicketList(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = serializers.TicketSerializer

    def perform_create(self, serializer):
        serializer.save(id=self.request.user)

class TicketDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = serializers.TicketSerializer