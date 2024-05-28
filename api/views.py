from rest_framework import permissions, viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import *
from api import models
import datetime

class BloqCreateViewSet(APIView):
    queryset = None
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = BloqSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            ret = models.Bloq.set_bloq(serializer.validated_data)
            
            if ret:
                return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Unexpected error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class BloqRetrieveUpdateViewSet(APIView):
    queryset = None
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, bloqId):
        instance = models.Bloq.get_bloq(bloqId)

        if not instance:
            return Response({'error': 'Bloq not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = BloqSerializer(data=instance)

        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, bloqId):
        instance = models.Bloq.get_bloq(bloqId)

        if not instance:
            return Response({'error': 'Bloq not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = BloqSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            models.Bloq.update_bloq(instance, serializer.validated_data)
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LockerCreateViewSet(APIView):
    queryset = None
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = LockerSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            ret = models.Locker.set_locker(serializer.validated_data)
            
            if ret:
                return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Unexpected error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class LockerRetrieveUpdateViewSet(APIView):
    queryset = None
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, lockerId):
        instance = models.Locker.get_locker(lockerId)

        if not instance:
            return Response({'error': 'Locker not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = LockerSerializer(data=instance)

        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, lockerId):
        instance = models.Locker.get_locker(lockerId)

        if not instance:
            return Response({'error': 'Locker not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = LockerSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            models.Locker.update_locker(instance, serializer.validated_data)
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class RentCreateViewSet(APIView):
    queryset = None
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = RentSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.validated_data['createdAt'] = datetime.datetime.now(datetime.UTC).isoformat()

            ret = models.Rent.set_rent(serializer.validated_data)
            
            if ret:
                return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Unexpected error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class RentRetrieveUpdateViewSet(APIView):
    queryset = None
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, rentId):
        instance = models.Rent.get_rent(rentId)

        if not instance:
            return Response({'error': 'Rent not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = RentSerializer(data=instance)

        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, rentId):
        instance = models.Rent.get_rent(rentId)

        if not instance:
            return Response({'error': 'Rent not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = RentSerializer(data=request.data)

        if not serializer.is_valid(raise_exception=True):
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        now_ts = str(datetime.datetime.now(datetime.UTC).isoformat())

        # handle existing records without a creation date
        if instance['createdAt'] is None:
            serializer.validated_data['createdAt'] = now_ts

        # handle status changes and set timestamps accordingly
        if instance['status'] != serializer.validated_data['status']:
            if serializer.validated_data['status'] == RentStatus.WAITING_PICKUP:
                serializer.validated_data['droppedOffAt'] = now_ts

            elif serializer.validated_data['status'] == RentStatus.DELIVERED:
                serializer.validated_data['pickedUpAt'] = now_ts

        models.Rent.update_rent(instance, serializer.validated_data)
        
        
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

