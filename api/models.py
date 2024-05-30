"""
DatabaseHandler: Manages JSON file operations.
ModelBase: Base class with common CRUD operations.
Bloq, Locker, Rent: Inherit from ModelBase and define specific methods if needed.
Error Handling: Added a try-except block in save_data for JSON validation.
"""


import uuid
import json
import os
import json

# workaround to avoid "Object of type UUID is not JSON serializable" error for storing UUIDs
class UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, uuid.UUID):
            # if the obj is uuid, we simply return the value of uuid
            return obj.hex
        return json.JSONEncoder.default(self, obj)


class DatabaseHandler:
    def __init__(self, file_name):
        self.file_path = os.path.join(os.path.dirname(__file__), file_name)

    def load_data(self):
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def save_data(self, data):
        try:
            json_object = json.loads(json.dumps(data, cls=UUIDEncoder))
        except ValueError as e:
            return False
        else:
            with open(self.file_path, 'w') as file:
                json.dump(data, file, indent=4, default=str)
                return True
            
class ModelBase:
    dbh: DatabaseHandler

    @classmethod
    def get_item(self, item_id):
        data = self.dbh.load_data()
        for item in data:
            if str(item.get('id')) == str(item_id):
                return item
        return None

    @classmethod
    def create_item(self, validated_data) :
        data = self.dbh.load_data()

        validated_data['id'] = str(uuid.uuid4())

        data.append(validated_data)

        if self.dbh.save_data(data):
            return validated_data
        
        return None
    
    @classmethod
    def delete_item(self, item_id):
        data = self.dbh.load_data()

        copy = [r for r in data if str(r.get('id')) != str(item_id)]

        return self.dbh.save_data(copy)
    

class Bloq(ModelBase):
    dbh = DatabaseHandler('../data/bloqs.json')

    @classmethod
    def update_bloq(self, instance, resource) -> bool:
        data = self.dbh.load_data()

        for r in data:
            if str(r.get('id')) == instance.get('id'):
                r['title'] = resource.get('title', instance.get('title'))
                r['address'] = resource.get('address', instance.get('address'))

        return self.dbh.save_data(data)

class Locker(ModelBase):
    dbh = DatabaseHandler('../data/lockers.json')
    
    @classmethod
    def update_locker(self, instance, resource) -> bool:
        data = self.dbh.load_data()

        for r in data:
            idField = r.get('id')

            if str(idField) == str(instance.get('id')):
                r['bloqId'] = str(resource.get('bloqId', instance.get('bloqId')))
                r['status'] = resource.get('status', instance.get('status'))
                r['isOccupied'] = resource.get('isOccupied', instance.get('isOccupied'))
        
        return self.dbh.save_data(data)

class Rent(ModelBase):
    dbh = DatabaseHandler('../data/rents.json')
    
    @classmethod
    def update_rent(self, instance, resource) -> bool:
        data = self.dbh.load_data()

        for r in data:
            idField = r.get('id')

            if str(idField) == str(instance.get('id')):
                r['lockerId'] = str(resource.get('lockerId'))
                r['weight'] = resource.get('weight')
                r['size'] = resource.get('size')
                r['status'] = resource.get('status')
                r['createdAt'] = resource.get('createdAt', instance.get('createdAt'))
                r['droppedOffAt'] = resource.get('droppedOffAt', instance.get('droppedOffAt'))
                r['pickedUpAt'] = resource.get('pickedUpAt', instance.get('pickedUpAt'))
        
        return self.dbh.save_data(data)
