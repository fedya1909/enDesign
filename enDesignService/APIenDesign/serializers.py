from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='id.username')

    class Meta:
        model = Ticket
        fields = ['id', 'text', 'date', 'exp_date']

class UserSerializer(serializers.ModelSerializer):
    tickets = serializers.PrimaryKeyRelatedField(many=True,read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username','tickets']
