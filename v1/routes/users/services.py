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
        
    @staticmethod
    def get_user_by_email(user_email: str):
        """Get User By Email Service"""
        user = UsersModel.get_collection().where("email", "==", user_email).stream()
        return [user.to_dict() for user in user]

    
    @staticmethod
    def get_technical_users_service():
        """Get Technical Users Service"""
        users = UsersModel.get_collection().where("role", "==", "technical").stream()
        return users
    
    def get_users_service():
        """Get Users Service"""
        users = UsersModel.get_collection().stream()
        return [user.to_dict() for user in users]

