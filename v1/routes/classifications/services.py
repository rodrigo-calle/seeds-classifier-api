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

# Classification Service
class ClassificationService:
    @staticmethod
    def format_classification_data(classification: dict):
        """Format Classification Data"""
        finish_date = None
        if classification._data["finishedAt"] is not None:
            finish_date = datetime.datetime.fromtimestamp(classification._data["finishedAt"].timestamp())
        
        return {
            "classification_data": classification._data["classificationData"],
            "created_at": datetime.datetime.fromtimestamp(classification._data["createdAt"].timestamp()),
            "finished_at": finish_date,
            "user": classification._data["user"].get().to_dict(),
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
    def get_classification_by_id_service(classification_id: str):
        """Get Classification By ID Service"""
        classification = ClassificationModel.get_collection().document(classification_id).get()
        return classification

    @staticmethod
    def create_classification_service(classification: dict):
        """Create Classification Service"""
        print(classification)
        if ClassificationModel.create_request_validation(classification):
            classification_ref = ClassificationModel.get_collection().add(classification)
            print(classification_ref)
            return classification_ref
        else:
            return False
        
    @staticmethod
    def update_classification_service(classification_id: str, classification_data: dict):
        """Update Classification Service"""
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
    