import traceback
from flask_restful import Resource
from flask_jwt_extended import jwt_required, current_user
from models.main_models import BranchTransfer, BranchTransferItem, Inventory
from schemas import BranchTransferSchema
from sqlalchemy.exc import IntegrityError
from datetime import date
from flask import request

transfer_schema = BranchTransferSchema()
transfers_schema = BranchTransferSchema(many=True)

class TransferResource(Resource):
    @jwt_required()
    def get(self, transfer_id=None, from_branch_id=None):
        try:
            if transfer_id and from_branch_id:
                transfer = request.db_session.query(BranchTransfer).filter_by(id=transfer_id, from_branch_id=from_branch_id).first()
                if not transfer:
                    return {"message": "Transfer not found"}, 404
                return transfer_schema.dump(transfer), 200
            elif from_branch_id is not None:
                transfers = request.db_session.query(BranchTransfer).filter(BranchTransfer.from_branch_id==from_branch_id).all()
                return transfers_schema.dump(transfers), 200
            else:
                transfers = request.db_session.query(BranchTransfer).all()
                return transfers_schema.dump(transfers), 200

        except Exception as e:
            traceback.print_exc()
            return {"message": str(e)}, 500

    @jwt_required()
    def post(self):
        def post(self):
            if current_user.role != 'admin':
                return {"message": "Admin access required"}, 403

        try:
            transfer = transfer_schema.load(request.get_json(), session=request.db_session)
            request.db_session.add(transfer)
            request.db_session.commit()
            return transfer_schema.dump(transfer), 201

        except IntegrityError:
            traceback.print_exc()
            request.db_session.rollback()
            return {"message": "transfer already exists"}, 400
        except Exception as e:
            traceback.print_exc()
            request.db_session.rollback()
            return {"message": str(e)}, 400