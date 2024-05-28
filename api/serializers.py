from rest_framework import serializers
from api import models

class BloqSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bloq
        fields = ['id', 'title', 'address']

class LockerSerializer(serializers.ModelSerializer):
    bloqId = serializers.PrimaryKeyRelatedField(source='pk', queryset=models.Bloq.objects.all())

    class Meta:
        model = models.Locker
        fields = ['id', 'status', 'isOccupied', 'bloqId']

class RentSerializer(serializers.ModelSerializer):
    lockerId = serializers.PrimaryKeyRelatedField(source='pk', queryset=models.Locker.objects.all())

    class Meta:
        model = models.Rent
        fields = ['id', 'weight', 'size', 'status', 'createdAt', 'droppedOffAt', 'pickedUpAt', 'lockerId']