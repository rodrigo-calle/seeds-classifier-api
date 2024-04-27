from firebase.config import db
from .models import UsersModel


class UserService:
    @staticmethod
    def create_user_service(user: dict):
        """Create User Service"""
        if UsersModel.request_validation(user):
            return UsersModel.get_collection().add(user)
        else:
            return False
        
    @staticmethod
    def get_user_by_id_service(user_id: str):
        """Get User By ID Service"""
        user = UsersModel.get_collection().document(user_id).get()
        return user
