from .models import ReportClassModel
from v1.routes.classifications.services import ClassificationService
from datetime import datetime

class ReportClassService:
    @staticmethod
    def generateReport(worker_id):
        """Create Report Service"""
        if not worker_id:
            classification_list = ClassificationService.get_classification_service()
            return classification_list

        else:
            classification_list = ClassificationService.get_classification_service()
            return classification_list