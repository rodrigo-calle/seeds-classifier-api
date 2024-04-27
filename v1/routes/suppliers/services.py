from .models import SupplierModel

class SupplierService:
    @staticmethod
    def format_supplier_data(supplier: dict):
        """Format Supplier Data"""
        return {
            "name": supplier._data["name"],
            "email": supplier._data["email"],
            "phone": supplier._data["phone"],
            "address": supplier._data["address"],
        }

    @staticmethod
    def get_supplier_by_id_service(supplier_id: str):
        """Get Supplier By ID Service"""
        supplier = SupplierModel.get_collection().document(supplier_id).get()
        return supplier

    @staticmethod
    def create_supplier_service(supplier: dict):
        """Create Supplier Service"""
        if SupplierModel.create_request_validation(supplier):
            supplier_ref = SupplierModel.get_collection().add(supplier)
            return supplier_ref
        else:
            return False

    @staticmethod
    def update_supplier_service(supplier_id: str, supplier: dict):
        """Update Supplier Service"""
        if SupplierModel.update_request_validation(supplier):
            supplier_ref = SupplierModel.get_collection().document(supplier_id).update(supplier)
            return supplier_ref
        else:
            return False

    @staticmethod
    def delete_supplier_service(supplier_id: str):
        """Delete Supplier Service"""
        supplier_ref = SupplierModel.get_collection().document(supplier_id).delete()
        return supplier_ref

