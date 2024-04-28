from fastapi import APIRouter
from .services import ClassificationService
from fastapi import File, UploadFile

router = APIRouter(
    prefix="/classifications",
    tags=["Classifications"],
    responses={404: {"description": "Not found"}},
)


@router.get("/{classification_id}")
def get_classification_by_id(classification_id: str):
    classification = ClassificationService.get_classification_by_id_service(classification_id)
    if classification.exists:
        classification_data = ClassificationService.format_classification_data(classification)
        return classification_data
    else:
        return {"error": "Classification not found"}

@router.post("/")
def create_classification(classification: dict):
    classification = ClassificationService.create_classification_service(classification)
    return classification

@router.patch("/{classification_id}")
def update_classification(classification_id: str, classification: dict):
    classification = ClassificationService.update_classification_service(classification_id, classification)
    if classification is False:
        return {"error": "Classification not found or invalid data"}
    else:
        return classification.get().to_dict()

# Seed Classification Method
@router.post("/predict")
async def classify_image(image: UploadFile = File(...)):
    classification = await ClassificationService.classify_image_service(image)
    return classification
