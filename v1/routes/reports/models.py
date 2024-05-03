from firebase.config import db

class ReportClassModel:
    def __init__(self, report_id: int, report_name: str, report_description: str):
        self.report_id = report_id
        self.report_name = report_name
        self.report_description = report_description
    
    @staticmethod
    def create_request_validation(request: dict):
        if not request.get("reportName"):
            return False
        if not request.get("reportDescription"):
            return False
        return True
    
    @staticmethod
    def get_collection():
        return db.collection("reports")
   
