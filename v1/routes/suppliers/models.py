from firebase.config import db

class SupplierModel:
    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    @staticmethod
    def get_collection():
        return db.collection('suppliers')
    
    @staticmethod
    def create_request_validation(request: dict):
        if not request.get('harvestMethod') or not request.get('name') or not request.get('phone') or not request.get('seedOrigin'):
            return False
        return True
    
    @staticmethod
    def update_request_validation(request: dict):
        if not request.get('harvestMethod') or not request.get('name') or not request.get('phone') or not request.get('seedOrigin'):
            return False
        return True
