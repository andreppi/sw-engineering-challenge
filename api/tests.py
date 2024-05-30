from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from api import models
from api import serializers

#
# Model tests (create, retrieve and update). checks the read/write methods of JSON files
# Bloqs
# Lockers
# Rents
# 

class BloqModelTest(TestCase):
    def setUp(self):
        self.bloq_data = {'title': 'Test Bloq', 'address': '123 Test Street'}
        self.bloq = models.Bloq.create_item(self.bloq_data)

    def test_model_create_bloq(self):
        bloq = models.Bloq.get_item(self.bloq['id'])
        self.assertIsNotNone(bloq)
        self.assertEqual(bloq['title'], 'Test Bloq')

    def test_model_update_bloq(self):
        updated_data = {'title': 'Updated Title', 'address': '123 Updated Street'}
        models.Bloq.update_bloq(self.bloq, updated_data)
        updated_bloq = models.Bloq.get_item(self.bloq['id'])
        self.assertEqual(updated_bloq['title'], 'Updated Title')

class LockerModelTest(TestCase):
    def setUp(self):
        self.bloq_data = {'title': 'Test Bloq', 'address': '123 Test Street'}
        self.bloq = models.Bloq.create_item(self.bloq_data)
        self.locker_data = {'bloqId': self.bloq['id'], 'status': serializers.LockerStatus.OPEN, 'isOccupied': False}
        self.locker = models.Locker.create_item(self.locker_data)

    def test_model_create_locker(self):
        locker = models.Locker.get_item(self.locker['id'])
        self.assertIsNotNone(locker)
        self.assertEqual(locker['status'], serializers.LockerStatus.OPEN)

    def test_model_update_locker(self):
        updated_data = {'status': serializers.LockerStatus.CLOSED, 'isOccupied': True}
        models.Locker.update_locker(self.locker, updated_data)
        updated_locker = models.Locker.get_item(self.locker['id'])
        self.assertEqual(updated_locker['status'], serializers.LockerStatus.CLOSED)

class RentModelTest(TestCase):
    def setUp(self):
        self.bloq_data = {'title': 'Test Bloq', 'address': '123 Test Street'}
        self.bloq = models.Bloq.create_item(self.bloq_data)
        self.locker_data = {'bloqId': self.bloq['id'], 'status': serializers.LockerStatus.OPEN, 'isOccupied': False}
        self.locker = models.Locker.create_item(self.locker_data)
        self.rent_data = {'lockerId': self.locker['id'], 'weight': 10, 'size': serializers.RentSize.M, 'status': serializers.RentStatus.CREATED, 'createdAt': '2023-01-01T00:00:00Z'}
        self.rent = models.Rent.create_item(self.rent_data)

    def test_model_create_rent(self):
        rent = models.Rent.get_item(self.rent['id'])
        self.assertIsNotNone(rent)
        self.assertEqual(rent['weight'], 10)

    def test_model_update_rent(self):
        updated_data = {'status': serializers.RentStatus.DELIVERED, 'weight': 12}
        models.Rent.update_rent(self.rent, updated_data)
        updated_rent = models.Rent.get_item(self.rent['id'])
        self.assertEqual(updated_rent['status'], serializers.RentStatus.DELIVERED)

#
# API tests (create, retrieve and update). Checks the HTTP GET, POST and PUT methods and its status codes
# Bloqs
# Lockers
# Rents
# 

class BloqAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.bloq_data = {'title': 'Test Bloq', 'address': '123 Test Street'}
        self.updated_bloq_data = {'title': 'Updated Bloq', 'address': '456 Updated Street'}

    def test_api_create_bloq(self):
        response = self.client.post('/api/bloqs/', self.bloq_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_api_get_bloqs(self):
        response = self.client.get('/api/bloqs/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_update_bloqs(self):
        self.client.post('/api/bloqs/', self.bloq_data, format='json')

        created_response = self.client.get('/api/bloqs/', format='json')
        
        bloq = next((x for x in created_response.data if x['title'] == self.bloq_data['title']), None)
        bloq_id = bloq.get('id', None)

        response = self.client.put(f'/api/bloqs/{bloq_id}/', self.updated_bloq_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.updated_bloq_data['title'])

class LockerAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.bloq_data = {'title': 'Test Bloq', 'address': '123 Test Street'}
        self.bloq_response = self.client.post('/api/bloqs/', self.bloq_data, format='json')
        self.locker_data = {'bloqId': self.bloq_response.data['id'], 'status': serializers.LockerStatus.OPEN, 'isOccupied': False}
        self.updated_locker_data = {'bloqId': self.bloq_response.data['id'], 'status': serializers.LockerStatus.CLOSED, 'isOccupied': True}

    def test_api_create_locker(self):
        response = self.client.post('/api/lockers/', self.locker_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_api_get_lockers(self):
        response = self.client.get('/api/lockers/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_update_lockers(self):
        self.client.post('/api/lockers/', self.locker_data, format='json')

        created_response = self.client.get('/api/lockers/', format='json')
    
        locker = next((x for x in created_response.data if x['bloqId'] == self.locker_data['bloqId']), None)
        locker_id = locker.get('id', None)

        response = self.client.put(f'/api/lockers/{locker_id}/', self.updated_locker_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], self.updated_locker_data['status'])

class RentAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.bloq_data = {'title': 'Test Bloq', 'address': '123 Test Street'}
        self.bloq_response = self.client.post('/api/bloqs/', self.bloq_data, format='json')
        self.locker_data = {'bloqId': self.bloq_response.data['id'], 'status': serializers.LockerStatus.OPEN, 'isOccupied': False}
        self.locker_response = self.client.post('/api/lockers/', self.locker_data, format='json')
        self.rent_data = {'lockerId': self.locker_response.data['id'], 'weight': 10, 'size': serializers.RentSize.M, 'status': serializers.RentStatus.CREATED, 'createdAt': '2023-01-01T00:00:00Z'}
        self.updated_rent_data = {'lockerId': self.locker_response.data['id'], 'weight': 15, 'size': serializers.RentSize.L, 'status': serializers.RentStatus.CREATED}

    def test_api_create_rent(self):
        response = self.client.post('/api/rents/', self.rent_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_api_get_rents(self):
        response = self.client.get('/api/rents/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_api_update_rents(self):
        self.client.post('/api/rents/', self.rent_data, format='json')

        created_response = self.client.get('/api/rents/', format='json')

        rent = next((x for x in created_response.data if x['lockerId'] == self.rent_data['lockerId']), None)
        rent_id = rent.get('id', None)

        response = self.client.put(f'/api/rents/{rent_id}/', self.updated_rent_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['weight'], self.updated_rent_data['weight'])