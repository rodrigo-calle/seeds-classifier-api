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
    if classification is False:
        return {"error": "Invalid data"}
    else:
        newClassification = classification[1].get().to_dict()
        newClassification["id"] = classification[1].id
        return newClassification

@router.patch("/{classification_id}")
def update_classification(classification_id: str, classification: dict):
    classification = ClassificationService.update_classification_service(classification_id, classification)
    if classification is False:
        return {"error": "Classification not found or invalid data"}
    else:
        result = classification.get().to_dict()
        print(result)
        return result

@router.patch("/{classification_id}/{update_kind}")
def update_classification_by_kind(classification_id: str, update_kind: str, classification_data: dict):
    classification = ClassificationService.update_classification_by_kind(classification_id, update_kind, classification_data)
    if classification is False:
        return {"error": "Classification not found or invalid data"}
    else:
        result = classification.get().to_dict()
        result["id"] = classification.id
        return result    

# Seed Classification Method
@router.post("/predict")
async def classify_image(image: UploadFile = File(...)):
    classification = await ClassificationService.classify_image_service(image)
    return classification

@router.get("/")
def get_classifications():
    classifications = ClassificationService.get_classification_service()
    return classifications

@router.get("/user/{user_id}")
def get_classifications_by_user(user_id: str):
    classifications = ClassificationService.get_classification_by_user_service(user_id)
    return classifications

@router.get("/technical/{technical_id}")
def get_classifications_by_technical(technical_id: str):
    classifications = ClassificationService.get_classification_by_technical_service(technical_id)
    return classifications

@router.delete("/{classification_id}")
def delete_classification(classification_id: str):
    classification = ClassificationService.delete_classification_service(classification_id)
    return classification

@router.patch("/finish/{classification_id}")
def finish_classification(classification_id: str):
    classification = ClassificationService.finish_classification_service(classification_id)
    return classification
