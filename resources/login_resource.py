from flask_restful import Resource
from flask_jwt_extended import create_access_token
from flask import request
from schemas import LoginSchema
from models.main_models import User
from werkzeug.security import generate_password_hash, check_password_hash

class LoginResource(Resource):
    def post(self):
        schema = LoginSchema()
        errors = schema.validate(request.get_json())
        if errors:
            return {"message": "Validation error", "errors": errors}, 400
            
        data = schema.load(request.get_json())
        user = request.db_session.query(User).filter_by(username=data['username']).first()

        if user and user.check_password(data['password']):
            access_token = create_access_token(identity=user.username)
            return {"access_token": access_token}, 200
            
        return {"message": "Invalid credentials"}, 401
