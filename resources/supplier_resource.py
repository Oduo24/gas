import traceback
from flask_restful import Resource
from flask_jwt_extended import jwt_required, current_user
from models.main_models import Supplier
from schemas import SupplierSchema
from sqlalchemy.exc import IntegrityError
from flask import request


supplier_schema = SupplierSchema()
suppliers_schema = SupplierSchema(many=True)

class SupplierResource(Resource):
    @jwt_required()
    def get(self, supplier_id=None):
        try:
            if supplier_id:
                supplier = request.db_session.get(Supplier, supplier_id)
                if not supplier:
                    return {"message": "Supplier not found"}, 404
                return supplier_schema.dump(supplier), 200
            else:
                suppliers = request.db_session.query(Supplier).all()
                return suppliers_schema.dump(suppliers), 200

        except Exception as e:
            return {"message": str(e)}, 500

    @jwt_required()
    def post(self):
        if current_user.role != 'admin':
            return {"message": "Admin access required"}, 403

        try:
            supplier = supplier_schema.load(request.get_json(), session=request.db_session)
            request.db_session.add(supplier)
            request.db_session.commit()
            return supplier_schema.dump(supplier), 201

        except IntegrityError:
            traceback.print_exc()
            request.db_session.rollback()
            return {"message": "Supplier already exists"}, 400
        except Exception as e:
            traceback.print_exc()
            request.db_session.rollback()
            return {"message": str(e)}, 400

    # @jwt_required()
    # def delete(self, supplier_id):
    #     if current_user.role != 'admin':
    #         return {"message": "Admin access required"}, 403

    #     supplier = request.db_session.get(Supplier, supplier_id)
    #     if not supplier:
    #         return {"message": "Supplier not found"}, 404
            
    #     try:
    #         request.db_session.delete(supplier)
    #         request.db_session.commit()
    #         return {"message": "Supplier deleted"}, 200
    #     except Exception as e:
    #         request.db_session.rollback()
    #         return {"message": str(e)}, 500