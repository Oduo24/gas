from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields, post_load, Schema
from datetime import datetime
import pytz
import uuid
import marshmallow_sqlalchemy
from models.base_model import BaseModel

from models.main_models import (
    User, Product, Inventory, InventoryLog, PhysicalStockVerification, Sale, 
    SaleItem, Invoice, Receipt, Supplier, PurchaseInvoice, PurchaseInvoiceItem, 
    SupplierPayment, Branch, BranchTransfer, BranchTransferItem, Customer
)

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        exclude = ("id", "created_at", "password")   # Exclude fields from deserialization

    # Use post_load to add the id and created_at fields after deserialization
    @post_load
    def add_default_fields(self, data, **kwargs):
        data["id"] = str(uuid.uuid4())
        data["created_at"] = datetime.now(pytz.utc)
        return data
    
class ProductSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        load_instance = True
        exclude = ("id", "created_at")   # Exclude fields from deserialization

    # Use post_load to add the id and created_at fields after deserialization
    @post_load
    def add_default_fields(self, data, **kwargs):
        data["id"] = str(uuid.uuid4())
        data["created_at"] = datetime.now(pytz.utc)
        return data

class InventorySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Inventory
        load_instance = True
        include_fk = True  # Critical for foreign keys

class InventoryLogSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = InventoryLog
        load_instance = True
        exclude = ("id", "created_at")
        include_fk = True

    @post_load
    def add_default_fields(self, data, **kwargs):
        data["id"] = str(uuid.uuid4())
        data["created_at"] = datetime.now(pytz.utc)
        return data


class PhysicalStockVerificationSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = PhysicalStockVerification
        load_instance = True

class SaleSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Sale
        load_instance = True
        include_relationships = True
        include_fk = True
        exclude = ("id", "created_at")
    items = marshmallow_sqlalchemy.fields.Nested('SaleItemSchema', many=True)
    @post_load
    def add_default_fields(self, data, **kwargs):
        data["id"] = str(uuid.uuid4())
        data["created_at"] = datetime.now(pytz.utc)
        return data

class SaleItemSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = SaleItem
        load_instance = True
        include_fk = True
        exclude = ("id", "created_at", "sale_id")
    
    @post_load
    def add_default_fields(self, data, **kwargs):
        data["id"] = str(uuid.uuid4())
        data["created_at"] = datetime.now(pytz.utc)
        return data

class InvoiceSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Invoice
        load_instance = True
    receipts = marshmallow_sqlalchemy.fields.Nested('ReceiptSchema', many=True)

class ReceiptSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Receipt
        load_instance = True

class SupplierSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Supplier
        load_instance = True
        include_fk = True
        exclude = ("id", "created_at")
    
    @post_load
    def add_default_fields(self, data, **kwargs):
        data["id"] = str(uuid.uuid4())
        data["created_at"] = datetime.now(pytz.utc)
        return data
    purchase_invoices = marshmallow_sqlalchemy.fields.Nested('PurchaseInvoiceSchema', many=True)
    payments = marshmallow_sqlalchemy.fields.Nested('SupplierPaymentSchema', many=True)

class PurchaseInvoiceSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = PurchaseInvoice
        load_instance = True
    items = marshmallow_sqlalchemy.fields.Nested('PurchaseInvoiceItemSchema', many=True)

class PurchaseInvoiceItemSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = PurchaseInvoiceItem
        load_instance = True

class SupplierPaymentSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = SupplierPayment
        load_instance = True

class BranchSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Branch
        load_instance = True
        include_fk = True
        exclude = ("id", "created_at")
    
    @post_load
    def add_default_fields(self, data, **kwargs):
        data["id"] = str(uuid.uuid4())
        data["created_at"] = datetime.now(pytz.utc)
        return data
    sales = marshmallow_sqlalchemy.fields.Nested('SaleSchema', many=True)
    inventory = marshmallow_sqlalchemy.fields.Nested('InventorySchema', many=True)

class BranchTransferSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = BranchTransfer
        load_instance = True
        include_fk = True
        exclude = ("id", "created_at")
    
    @post_load
    def add_default_fields(self, data, **kwargs):
        data["id"] = str(uuid.uuid4())
        data["created_at"] = datetime.now(pytz.utc)
        return data
    items = marshmallow_sqlalchemy.fields.Nested('BranchTransferItemSchema', many=True)

class BranchTransferItemSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = BranchTransferItem
        load_instance = True
        include_fk = True
        exclude = ("id", "created_at", "transfer_id")

class CustomerSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Customer
        load_instance = True
        include_fk = True
        exclude = ("id", "created_at")
    
    @post_load
    def add_default_fields(self, data, **kwargs):
        data["id"] = str(uuid.uuid4())
        data["created_at"] = datetime.now(pytz.utc)
        return data
    sales = marshmallow_sqlalchemy.fields.Nested('SaleSchema', many=True)

class LoginSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)
