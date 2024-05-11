from firebase.config import db

class UsersModel:
    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = password

    @staticmethod
    def request_validation(request: dict):
        if not request.get("name") or not request.get("email") or not request.get("role"):
            return False
        return True
    
    @staticmethod
    def get_collection():
        return db.collection("users")
    