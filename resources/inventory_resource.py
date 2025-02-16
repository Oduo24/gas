from flask_restful import Resource
from flask_jwt_extended import jwt_required
from flask import request
from models.main_models import Inventory, Branch, Product
from schemas import InventorySchema

inventory_schema = InventorySchema()
inventories_schema = InventorySchema(many=True)

class InventoryResource(Resource):
    @jwt_required()
    def get(self, branch_id=None, product_id=None):
        try:
            if branch_id and product_id:
                inventory = request.db_session.query(Inventory).filter_by(
                    branch_id=branch_id,
                    product_id=product_id
                ).first()
                if not inventory:
                    return {"message": "Inventory not found"}, 404
                return inventory_schema.dump(inventory), 200
            
            elif branch_id:
                inventories = request.db_session.query(Inventory).filter_by(
                    branch_id=branch_id
                ).all()
                return inventories_schema.dump(inventories), 200
            
            else:
                inventories = request.db_session.query(Inventory).all()
                return inventories_schema.dump(inventories), 200

        except Exception as e:
            return {"message": str(e)}, 500

    @jwt_required()
    def patch(self, branch_id, product_id):
        try:
            inventory = request.db_session.query(Inventory).filter_by(
                branch_id=branch_id,
                product_id=product_id
            ).first()

            if not inventory:
                return {"message": "Inventory not found"}, 404

            data = request.get_json()
            if 'quantity' in data:
                inventory.quantity = data['quantity']
            
            request.db_session.commit()
            return inventory_schema.dump(inventory), 200

        except Exception as e:
            request.db_session.rollback()
            return {"message": str(e)}, 400