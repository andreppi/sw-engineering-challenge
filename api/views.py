from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import *
from api import models
import datetime
        
class BloqViewSet(APIView):
    queryset = None
    permission_classes = [AllowAny]

    def get(self, request):
        data = models.Bloq.dbh.load_data()
        serializer = BloqSerializer(data, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = BloqSerializer(data=request.data)

        if serializer.is_valid():
            ret = models.Bloq.create_item(serializer.validated_data)
            
            if ret:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Unexpected error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class BloqResourceViewSet(APIView):
    queryset = None
    permission_classes = [AllowAny]

    def get(self, request, bloq_id):
        bloq = models.Bloq.get_item(bloq_id)

        if not bloq:
            return Response({'error': 'Bloq not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = BloqSerializer(data=bloq)

        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, bloq_id):
        instance = models.Bloq.get_item(bloq_id)

        if not instance:
            return Response({'error': 'Bloq not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = BloqSerializer(data=request.data)

        if serializer.is_valid():
            ret = models.Bloq.update_bloq(instance, serializer.validated_data)
            if ret:
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Unexpected error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, bloq_id):
        instance = models.Bloq.get_item(bloq_id)

        if not instance:
            return Response({'error': 'Bloq not found'}, status=status.HTTP_404_NOT_FOUND)

        ret = models.Bloq.delete_item(bloq_id)

        if ret:
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class LockerCreateViewSet(APIView):
    queryset = None
    permission_classes = [AllowAny]

    def get(self, request):
        data = models.Locker.dbh.load_data()
        serializer = LockerSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LockerSerializer(data=request.data)

        if serializer.is_valid():
            ret = models.Locker.create_item(serializer.validated_data)
            
            if ret:
                return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Unexpected error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class LockerResourceViewSet(APIView):
    queryset = None
    permission_classes = [AllowAny]

    def get(self, request, locker_id):
        instance = models.Locker.get_item(locker_id)

        if not instance:
            return Response({'error': 'Locker not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = LockerSerializer(data=instance)

        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, locker_id):
        instance = models.Locker.get_item(locker_id)

        if not instance:
            return Response({'error': 'Locker not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = LockerSerializer(data=request.data)

        if serializer.is_valid():
            models.Locker.update_locker(instance, serializer.validated_data)
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, locker_id):
        instance = models.Locker.get_item(locker_id)

        if not instance:
            return Response({'error': 'Locker not found'}, status=status.HTTP_404_NOT_FOUND)

        ret = models.Locker.delete_item(locker_id)

        if ret:
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class RentCreateViewSet(APIView):
    queryset = None
    permission_classes = [AllowAny]


    def get(self, request):
        data = models.Rent.dbh.load_data()
        serializer = RentSerializer(data, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = RentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.validated_data['createdAt'] = datetime.datetime.now(datetime.UTC).isoformat()

            ret = models.Rent.create_item(serializer.validated_data)
            
            if ret:
                return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Unexpected error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class RentResourceViewSet(APIView):
    queryset = None
    permission_classes = [AllowAny]

    def get(self, request, rent_id):
        instance = models.Rent.get_item(rent_id)

        if not instance:
            return Response({'error': 'Rent not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = RentSerializer(data=instance)

        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, rent_id):
        instance = models.Rent.get_item(rent_id)

        if not instance:
            return Response({'error': 'Rent not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = RentSerializer(data=request.data)

        if not serializer.is_valid():
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
    
    def delete(self, request, rent_id):
        instance = models.Rent.get_item(rent_id)

        if not instance:
            return Response({'error': 'Rent not found'}, status=status.HTTP_404_NOT_FOUND)

        ret = models.Rent.delete_item(rent_id)

        if ret:
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

