import os
import traceback
from datetime import timedelta
from flask import Flask, jsonify, request, render_template, redirect, url_for, make_response, flash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt, get_jwt_identity, verify_jwt_in_request, set_access_cookies, unset_jwt_cookies
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from flask_restful import Api, Resource

from models.main_models import Base, User
from db_storage import engine, Session
from resources.user_resource import UserResource
from resources.login_resource import LoginResource
from resources.product_resource import ProductResource
from resources.inventory_resource import InventoryResource
from resources.sale_resource import SaleResource
from resources.branch_resource import BranchResource
from resources.supplier_resource import SupplierResource
from resources.customer_resource import CustomerResource
from resources.transfer_resource import TransferResource

# Load environment variables from .env file
load_dotenv()

# Initialize database
Base.metadata.create_all(engine)


app = Flask(__name__)
api = Api(app)

# Setup JWT
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
jwt = JWTManager(app)

# Extend Access Token Expiration Time (e.g., 7 days)
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 30 * 24 * 60 * 60  # 30 days in seconds

# If true this will only allow the cookies that contain your JWTs to be sent
# over https. In production, this should always be set to True
app.config["JWT_COOKIE_SECURE"] = False

# Load user object
@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return request.db_session.query(User).filter_by(username=identity).first()

@app.before_request
def create_session():
    # This ensures that each request gets its own session
    request.db_session = Session()

@app.teardown_request
def teardown_request(exception=None):
    if exception:
        request.db_session.rollback()
    Session.remove()

# Add routes
api.add_resource(UserResource, "/api/v1/users", "/api/v1/users/<string:user_id>")
api.add_resource(LoginResource, "/api/v1/login")
api.add_resource(ProductResource, "/api/v1/products", "/api/v1/products/<string:product_id>")
api.add_resource(
    InventoryResource,
    "/api/v1/inventories",
    "/api/v1/inventories/<string:branch_id>/<string:product_id>",
    "/api/v1/inventories/<string:branch_id>"
)
api.add_resource(
    SaleResource,
    "/api/v1/sales",
    "/api/v1/sales/<string:branch_id>/<string:sale_id>",
    "/api/v1/sales/<string:branch_id>"
)

api.add_resource(
    BranchResource,
    "/api/v1/branches",
    "/api/v1/branches/<string:branch_id>",
)

api.add_resource(
    SupplierResource,
    "/api/v1/suppliers",
    "/api/v1/suppliers/<string:supplier_id>",
)

api.add_resource(
    CustomerResource,
    "/api/v1/customers",
    "/api/v1/customers/<string:customer_id>/<string:branch_id>",
    "/api/v1/customers/<string:branch_id>",
)

api.add_resource(
    TransferResource,
    "/api/v1/transfers",
    "/api/v1/transfers/<string:from_branch_id>",
    "/api/v1/transfers/<string:transfer_id>/<string:from_branch_id>",
)



if __name__ == "__main__":
    app.run(debug=True)