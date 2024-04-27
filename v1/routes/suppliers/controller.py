from fastapi import File, UploadFile, APIRouter
from .services import SupplierService

router = APIRouter(
    prefix="/suppliers",
    tags=["Suppliers"],
    responses={404: {"description": "Not found"}},
)

@router.get("/{supplier_id}")
def get_supplier_by_id(supplier_id: str):
    supplier = SupplierService.get_supplier_by_id_service(supplier_id)
    if supplier.exists:
        supplier_data = SupplierService.format_supplier_data(supplier)
        return supplier_data
    else:
        return {"error": "Supplier not found"}
    
@router.post("/")
def create_supplier(supplier: dict):
    supplier = SupplierService.create_supplier_service(supplier)
    return supplier

@router.patch("/{supplier_id}")
def update_supplier(supplier_id: str, supplier: dict):
    supplier = SupplierService.update_supplier_service(supplier_id, supplier)
    if supplier is False:
        return {"error": "Supplier not found or invalid data"}
    else:
        return supplier.get().to_dict()

