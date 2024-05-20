from .services import ReportClassService
from fastapi import APIRouter, Response
import random
import csv

router = APIRouter(
    prefix="/reports",
    tags=["Reports"],
    responses={404: {"description": "Not found"}},
)

@router.get("/download-csv/{worker_id}")
def download_csv(worker_id: str, response: Response):
    classifications = []
    if worker_id:
        classifications = ReportClassService.generateReport(worker_id)
    else:
        classifications = ReportClassService.generateReport()
    
    # Define CSV file name classification plus readable date
    random_key = random.randint(10000, 99999)
    csv_file_name = f"classifications_{random_key}.csv"

    # Set response headers for file download
    response.headers["Content-Disposition"] = f"attachment; filename={csv_file_name}"
    response.headers["Content-Type"] = "text/csv"

    # Write classification data to CSV
    with open(csv_file_name, "w", newline="") as csvfile:
        fieldnames = ["user", "createdAt", "classificationData", "task", "startedAt", "finishedAt"]  # Define field names based on your classification data
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for classification in classifications:
            writer.writerow(classification)  # Assuming classification is a dictionary

    # Read the CSV file and return as response
    with open(csv_file_name, "rb") as csv_file:
        csv_content = csv_file.read()
        return Response(content=csv_content, media_type="text/csv")
