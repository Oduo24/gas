from flask import request, jsonify
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from schemas import UserSchema
from models.main_models import User
from werkzeug.security import generate_password_hash, check_password_hash
import traceback
from flask_jwt_extended import jwt_required, current_user

user_schema = UserSchema(exclude=("password",))
users_schema = UserSchema(many=True, exclude=("password",))

class UserResource(Resource):
    @jwt_required()
    def get(self, user_id=None):
        if user_id:
            user = request.db_session.query(User).filter_by(id=user_id).first()
            if not user:
                return {"message": "User not found"}, 404
            return user_schema.dump(user), 200
        else:
            users = request.db_session.query(User).all()
            return users_schema.dump(users), 200

    @jwt_required()
    def post(self):
        # Register a new user
        data = request.get_json()
        password_hash = generate_password_hash(data["password"])
        try:
            # Remove password from data before deserialization
            data.pop("password")
            user = user_schema.load(data, session=request.db_session)
            user.password = password_hash  # Set the hashed password
            request.db_session.add(user)
            request.db_session.commit()
            return {"message": "User added successfully"}, 200
        except Exception as e:
            traceback.print_exc()
            request.db_session.rollback()
            return {"message": "Failled to create user"}, 400

    # def delete(self, user_id):
    #     user = request.db_session.query(User).filter_by(id=user_id).first()
    #     if not user:
    #         return {"message": "User not found"}, 404
    #     request.db_session.delete(user)
    #     request.db_session.commit()
    #     return {"message": "User deleted successfully"}, 200
