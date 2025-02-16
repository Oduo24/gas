import traceback
from flask_restful import Resource
from flask_jwt_extended import jwt_required, current_user
from models.main_models import Sale, SaleItem, Inventory, Product, InventoryLog
from schemas import SaleSchema, SaleItemSchema, InventoryLogSchema
from datetime import date
from flask import request


sale_schema = SaleSchema()
sales_schema = SaleSchema(many=True)
log_schema = InventoryLogSchema()

class SaleResource(Resource):
    @jwt_required()
    def post(self):
        try:
            session = request.db_session
            data = request.get_json()
            # Let the nested schema automatically handle the items
            sale = sale_schema.load(data, session=session)
            
            # Performing business logic such as inventory checks and total calculations
            total = 0
            for item in sale.items:
                product = session.query(Product).filter_by(id=item.product_id).first()
                if not product:
                    raise ValueError(f"Product {item.product_id} not found")
                
                # Verify inventory
                inventory = session.query(Inventory).filter_by(
                    branch_id=sale.branch_id,
                    product_id=item.product_id
                ).with_for_update().first()  # Lock inventory row

                if not inventory or inventory.quantity < item.quantity:
                    raise ValueError(f"Insufficient stock for product {product.name}")

                # Update inventory and calculate total
                inventory.quantity -= item.quantity
                total += item.quantity * product.unit_price
                # Add sale_id field for each item
                item.sale_id = sale.id

                # Create inventory log entry
                log_data = {
                    "branch_id": sale.branch_id,
                    "product_id": item.product_id,
                    "change_type": 'sale',
                    "quantity": -item.quantity,
                }
                log = log_schema.load(log_data, session=session)
                session.add(log)
            
            sale.total_amount = total
            session.add(sale)
            session.commit()
            return sale_schema.dump(sale), 201
        except Exception as e:
            traceback.print_exc()
            session.rollback()
            return {"message": str(e)}, 400
        

    @jwt_required()
    def get(self, branch_id=None, sale_id=None):
        try:
            if branch_id and sale_id:
                sale = request.db_session.query(Sale).filter_by(
                    branch_id=branch_id,
                    id=sale_id
                ).first()
                if not sale:
                    return {"message": "Sale not found"}, 404
                return sale_schema.dump(sale), 200
            
            elif branch_id:
                sales = request.db_session.query(Sale).filter_by(
                    branch_id=branch_id
                ).all()
                return sales_schema.dump(sales), 200
            
            else:
                sales = request.db_session.query(Sale).all()
                return sales_schema.dump(sales), 200

        except Exception as e:
            return {"message": str(e)}, 500