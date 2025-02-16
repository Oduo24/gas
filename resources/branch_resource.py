import traceback
from flask_restful import Resource
from flask_jwt_extended import jwt_required, current_user
from models.main_models import Branch
from schemas import BranchSchema
from sqlalchemy.exc import IntegrityError
from flask import request


branch_schema = BranchSchema()
branches_schema = BranchSchema(many=True)

class BranchResource(Resource):
    @jwt_required()
    def get(self, branch_id=None):
        try:
            if branch_id:
                branch = request.db_session.get(Branch, branch_id)
                if not branch:
                    return {"message": "Branch not found"}, 404
                return branch_schema.dump(branch), 200
            else:
                branches = request.db_session.query(Branch).all()
                return branches_schema.dump(branches), 200

        except Exception as e:
            return {"message": str(e)}, 500

    @jwt_required()
    def post(self):
        if current_user.role != 'admin':
            return {"message": "Admin access required"}, 403

        try:
            branch = branch_schema.load(request.get_json(), session=request.db_session)
            request.db_session.add(branch)
            request.db_session.commit()
            return branch_schema.dump(branch), 201

        except IntegrityError:
            traceback.print_exc()
            request.db_session.rollback()
            return {"message": "Branch already exists"}, 400
        except Exception as e:
            traceback.print_exc()
            request.db_session.rollback()
            return {"message": str(e)}, 400

    # @jwt_required()
    # def delete(self, branch_id):
    #     if current_user.role != 'admin':
    #         return {"message": "Admin access required"}, 403

    #     branch = request.db_session.get(Branch, branch_id)
    #     if not branch:
    #         return {"message": "Branch not found"}, 404
            
    #     try:
    #         request.db_session.delete(branch)
    #         request.db_session.commit()
    #         return {"message": "Branch deleted"}, 200
    #     except Exception as e:
    #         request.db_session.rollback()
    #         return {"message": str(e)}, 500