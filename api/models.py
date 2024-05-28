from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
import json
import os

class Bloq:
    file_path = os.path.join(os.path.dirname(__file__), '../data/bloqs.json')

    @staticmethod
    def load_data():
        with open(Bloq.file_path, 'r') as file:
            return json.load(file)

    @staticmethod
    def save_data(data):
        try:
            json_object = json.loads(json.dumps(data))
        except ValueError as e:
            return False
        else:
            with open(Bloq.file_path, 'w') as file:
                json.dump(data, file, indent=4, default=str)
                return True

    @classmethod
    def get_bloq(cls, bloqId):
        data = cls.load_data()

        for r in data:
            idField = r.get('id')

            if str(idField) == str(bloqId):
                return r
            
        return None

    @classmethod
    def set_bloq(cls, validated_data):
        data = cls.load_data()

        validated_data['id'] = str(uuid.uuid4())
        data.append(validated_data)
        
        return cls.save_data(data)
    
    @classmethod
    def update_bloq(cls, instance, validated_data):
        data = cls.load_data()

        for r in data:
            idField = r.get('id')

            if str(idField) == str(instance.get('id')):
                r['title'] = validated_data.get('title', instance.get('title'))
                r['address'] = validated_data.get('address', instance.get('address'))
        
        return cls.save_data(data)


class Locker:
    file_path = os.path.join(os.path.dirname(__file__), '../data/lockers.json')

    @staticmethod
    def load_data():
        with open(Locker.file_path, 'r') as file:
            return json.load(file)

    @staticmethod
    def save_data(data):
        try:
            json_object = json.loads(json.dumps(data))
        except ValueError as e:
            return False
        else:
            with open(Locker.file_path, 'w') as file:
                json.dump(data, file, indent=4, default=str)
                return True

    @classmethod
    def get_locker(cls, lockerId):
        data = cls.load_data()

        for r in data:
            idField = r.get('id')

            if str(idField) == str(lockerId):
                return r
            
        return None

    @classmethod
    def set_locker(cls, validated_data):
        data = cls.load_data()

        validated_data['id'] = str(uuid.uuid4())
        validated_data['bloqId'] = str(validated_data['bloqId'])
        data.append(validated_data)
        
        return cls.save_data(data)
    
    @classmethod
    def update_locker(cls, instance, validated_data):
        data = cls.load_data()

        for r in data:
            idField = r.get('id')

            if str(idField) == str(instance.get('id')):
                r['bloqId'] = str(validated_data.get('bloqId', instance.get('bloqId')))
                r['status'] = validated_data.get('status', instance.get('status'))
                r['isOccupied'] = validated_data.get('isOccupied', instance.get('isOccupied'))
        
        return cls.save_data(data)


class Rent:
    file_path = os.path.join(os.path.dirname(__file__), '../data/rents.json')

    @staticmethod
    def load_data():
        with open(Rent.file_path, 'r') as file:
            return json.load(file)

    @staticmethod
    def save_data(data):
        try:
            json_object = json.loads(json.dumps(data))
        except ValueError as e:
            return False
        else:
            with open(Rent.file_path, 'w') as file:
                json.dump(data, file, indent=4, default=str)
                return True

    @classmethod
    def get_rent(cls, rentId):
        data = cls.load_data()

        for r in data:
            idField = r.get('id')

            if str(idField) == str(rentId):
                return r
            
        return None

    @classmethod
    def set_rent(cls, validated_data):
        data = cls.load_data()

        validated_data['id'] = str(uuid.uuid4())
        validated_data['lockerId'] = str(validated_data['lockerId'])

        data.append(validated_data)
        
        return cls.save_data(data)
    
    @classmethod
    def update_rent(cls, instance, validated_data):
        data = cls.load_data()

        for r in data:
            idField = r.get('id')

            if str(idField) == str(instance.get('id')):
                r['lockerId'] = str(validated_data.get('lockerId'))
                r['weight'] = validated_data.get('weight')
                r['size'] = validated_data.get('size')
                r['status'] = validated_data.get('status')
                r['createdAt'] = validated_data.get('createdAt', instance.get('createdAt'))
                r['droppedOffAt'] = validated_data.get('droppedOffAt', instance.get('droppedOffAt'))
                r['pickedUpAt'] = validated_data.get('pickedUpAt', instance.get('pickedUpAt'))
        
        return cls.save_data(data)

