import numpy as np
from PIL import Image
from io import BytesIO
from fastapi import File, UploadFile
import tensorflow as tf
from .models import ClassificationModel
import datetime


CLASS_NAMES = ["oocarpa", "psegoutrobus", "tecunumanii"]

def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image

business_id = 'vivero-santo-domingo'

# Classification Service
class ClassificationService:
    @staticmethod
    def format_classification_data(classification: dict):
        """Format Classification Data"""

        return {
            "classificationData": classification._data["classificationData"],
            "createdAt": classification._data["createdAt"],
            "finishedAt": classification._data["finishedAt"],
            "user": classification._data["user"],
            "id": classification.id,
            "task": classification._data["task"] if classification._data.get("task") else None,
        }

    @staticmethod
    async def classify_image_service(imageFile: UploadFile = File(...)):
        """Classify Pine Seeds Image Service"""
        image = read_file_as_image(await imageFile.read())
        image_resized = tf.image.resize(image, (256, 256))

        image_batch = np.expand_dims(image_resized, 0)

        predictions = ClassificationModel.get_cnn_classification_model().predict(image_batch)

        predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
        confidence = round(100 * (np.max(predictions[0])), 2)

        return {
            'class': predicted_class,
            'confidence': float(confidence),
        }
    
    @staticmethod
    def get_classification_service():
        """Get Classification Service"""
        classifications = ClassificationModel.get_collection().stream()
        return [ClassificationService.format_classification_data(classification) for classification in classifications]

    @staticmethod
    def get_classification_by_id_service(classification_id: str):
        """Get Classification By ID Service"""
        classification = ClassificationModel.get_collection().document(classification_id).get()
        return classification

    @staticmethod
    def get_classification_by_user_service(user_id: str):
        """Get Classification By User Service"""
        classifications = ClassificationModel.get_collection().where("user", "==", user_id).stream()
        return [ClassificationService.format_classification_data(classification) for classification in classifications]


    @staticmethod
    def create_classification_service(classification: dict):
        """Create Classification Service"""
        print(classification)
        if ClassificationModel.create_request_validation(classification):
            classification["businessId"] = business_id
            classification_ref = ClassificationModel.get_collection().add(classification)
            print(classification_ref)
            return classification_ref
        else:
            return False
        
    @staticmethod
    def update_classification_service(classification_id: str, classification_data: dict):
        """Update Classification Service"""
        print(classification_data)
        if ClassificationModel.update_request_validation(classification_data) and ClassificationModel.get_collection().document(classification_id).get().exists:
            classification = ClassificationModel.get_collection().document(classification_id)
            classification.update(classification_data)
            return classification
        else:
            return False
    
    @staticmethod
    def delete_classification_service(classification_id: str):
        """Delete Classification Service"""
        classification = ClassificationModel.get_collection().document(classification_id)
        classification.delete()
        return True
    
    @staticmethod
    def get_classification_by_technical_service(technical_id: str):
        """Get Classifications By Technical Assigned Service"""
        print(technical_id)
        classifications = ClassificationModel.get_collection().where("task.technical", "==", technical_id).stream()
        return [ClassificationService.format_classification_data(classification) for classification in classifications]

    @staticmethod
    def finish_classification_service(classification_id: str):
        """Finish Classification Service"""
        classification = ClassificationModel.get_collection().document(classification_id)
        classification.update({"finishedAt": datetime.datetime.now().timestamp()})
        return classification
    