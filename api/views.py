from rest_framework import permissions, viewsets

from api.serializers import *
from api import models

class BloqViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = models.Bloq.objects.all()
    serializer_class = BloqSerializer
    permission_classes = [permissions.IsAuthenticated]

class LockerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = models.Locker.objects.all()
    serializer_class = LockerSerializer
    permission_classes = [permissions.IsAuthenticated]

class RentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = models.Rent.objects.all()
    serializer_class = RentSerializer
    permission_classes = [permissions.IsAuthenticated]