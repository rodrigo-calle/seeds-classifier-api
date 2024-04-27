import datetime
from firebase.config import db
from cnn.main import CNN_CLASSIFICATION_MODEL

class ClassificationModel:
    def __init__(self, classification_data: dict, user: dict, created_at: datetime.datetime, finished_at: datetime.datetime):
        """Classification Model Constructor"""
        self.classification_data = classification_data
        self.user = user
        self.created_at = created_at
        self.finished_at = finished_at

    @staticmethod
    def create_request_validation(request: dict):
        """Create Request Validation"""
        if not request.get("classification_data"):
            return False
        if not request.get("user"):
            return False
        return True
    
    def update_request_validation(request: dict):
        """Update Request Validation"""
        if not request.get("classification_data") or not request.get("user"):
            return False
        return True
    
    @staticmethod
    def get_collection():
        return db.collection("classification_sessions")
    
    def get_cnn_classification_model():
        return CNN_CLASSIFICATION_MODEL



