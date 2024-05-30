from rest_framework import serializers
from api import models
import uuid 

# The first element in each tuple is the actual value to be set on the model, 
# and the second element is the human-readable name. 

class LockerStatus:
    OPEN = "OPEN"
    CLOSED = "CLOSED"

    CHOICES = [
        (OPEN, 'Open'),
        (CLOSED, 'Closed'),
    ]

class RentSize:
    XS = "XS"
    S = "S"
    M = "M"
    L = "L"
    XL = "XL"

    CHOICES = [
        (XS, "XS"),
        (S, "S"),
        (M, "M"),
        (L, "L"),
        (XL, "XL"),
    ]

class RentStatus:
    CREATED = "CREATED"
    WAITING_DROPOFF = "WAITING_DROPOFF"
    WAITING_PICKUP = "WAITING_PICKUP"
    DELIVERED = "DELIVERED"

    CHOICES = [
        (CREATED, "Created"),
        (WAITING_DROPOFF, "Waiting Drop-off"),
        (WAITING_PICKUP, "Waiting Pick-up"),
        (DELIVERED, "Delivered"),
    ]

class BloqSerializer(serializers.Serializer):
    id = serializers.UUIDField(format='hex_verbose', read_only=True)
    title = serializers.CharField(max_length=100, allow_null=False, allow_blank=False)
    address = serializers.CharField(max_length=100, allow_null=False, allow_blank=False)

class LockerSerializer(serializers.Serializer):
    id = serializers.UUIDField(format='hex_verbose', read_only=True)
    bloqId = serializers.UUIDField(format='hex_verbose', required=False)
    status = serializers.ChoiceField(choices=LockerStatus.CHOICES)
    isOccupied = serializers.BooleanField(required=True)


class RentSerializer(serializers.Serializer):
    id = serializers.UUIDField(format='hex_verbose', read_only=True)
    lockerId = serializers.UUIDField(format='hex_verbose', required=False)
    weight = serializers.IntegerField(min_value=1, max_value=99, allow_null=False)
    size = serializers.ChoiceField(choices=RentSize.CHOICES)
    status = serializers.ChoiceField(choices=RentStatus.CHOICES)
    createdAt = serializers.DateTimeField(required=False, allow_null=True)
    droppedOffAt = serializers.DateTimeField(required=False, allow_null=True)
    pickedUpAt = serializers.DateTimeField(required=False, allow_null=True)