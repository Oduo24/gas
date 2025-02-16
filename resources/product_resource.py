from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required, current_user
from models.main_models import Product
from schemas import ProductSchema
from sqlalchemy.exc import IntegrityError

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

class ProductResource(Resource):
    @jwt_required()
    def get(self, product_id=None):
        try:
            if product_id:
                product = request.db_session.get(Product, product_id)
                if not product:
                    return {"message": "Product not found"}, 404
                return product_schema.dump(product), 200
            else:
                products = request.db_session.query(Product).all()
                return products_schema.dump(products), 200

        except Exception as e:
            return {"message": str(e)}, 500

    @jwt_required()
    def post(self):
        if current_user.role != 'admin':
            return {"message": "Admin access required"}, 403

        try:
            data = request.get_json()
            product = product_schema.load(data, session=request.db_session)
            request.db_session.add(product)
            request.db_session.commit()
            product_schema.dump(product), 201

        except IntegrityError:
            request.db_session.rollback()
            return {"message": "Product already exists"}, 400
        except Exception as e:
            request.db_session.rollback()
            return {"message": str(e)}, 400

    # @jwt_required()
    # def delete(self, product_id):
    #     if current_user.role != 'admin':
    #         return {"message": "Admin access required"}, 403

    #     product = request.db_session.get(Product, product_id)
    #     if not product:
    #         return {"message": "Product not found"}, 404
            
    #     try:
    #         request.db_session.delete(product)
    #         request.db_session.commit()
    #         return {"message": "Product deleted"}, 200
    #     except Exception as e:
    #         request.db_session.rollback()
    #         return {"message": str(e)}, 500