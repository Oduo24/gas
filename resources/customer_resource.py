import traceback
from flask_restful import Resource
from flask_jwt_extended import jwt_required, current_user
from models.main_models import Customer
from schemas import CustomerSchema
from sqlalchemy.exc import IntegrityError
from flask import request

customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)

class CustomerResource(Resource):
    @jwt_required()
    def get(self, customer_id=None, branch_id=None):
        try:
            if customer_id and branch_id:
                customer = request.db_session.query(Customer).filter_by(branch_id=branch_id, id=customer_id).first()
                if not customer:
                    return {"message": "Customer not found"}, 404
                return customer_schema.dump(customer), 200
            elif branch_id:
                customers = request.db_session.query(Customer).filter_by(branch_id=branch_id).all()
                return customers_schema.dump(customers), 200
            else:
                customers = request.db_session.query(Customer).all()
                return customers_schema.dump(customers), 200

        except Exception as e:
            traceback.print_exc()
            return {"message": str(e)}, 500

    @jwt_required()
    def post(self):
        try:
            customer = customer_schema.load(request.get_json(), session=request.db_session)
            request.db_session.add(customer)
            request.db_session.commit()
            return customer_schema.dump(customer), 201

        except IntegrityError:
            traceback.print_exc()
            request.db_session.rollback()
            return {"message": "Customer already exists"}, 400
        except Exception as e:
            traceback.print_exc()
            request.db_session.rollback()
            return {"message": str(e)}, 400

    # @jwt_required()
    # def delete(self, customer_id):
    #     if current_user.role != 'admin':
    #         return {"message": "Admin access required"}, 403

    #     customer = request.db_session.get(Customer, customer_id)
    #     if not customer:
    #         return {"message": "Customer not found"}, 404
            
    #     try:
    #         request.db_session.delete(customer)
    #         request.db_session.commit()
    #         return {"message": "Customer deleted"}, 200
    #     except Exception as e:
    #         request.db_session.rollback()
    #         return {"message": str(e)}, 500