from sqlalchemy import (
    Column, Integer, String, Float, ForeignKey, Date, Enum, Text)
from sqlalchemy.orm import relationship, declarative_base
from models.base_model import BaseModel
from werkzeug.security import generate_password_hash, check_password_hash

Base = declarative_base()

class User(BaseModel, Base):
    """Defines the User class"""
    __tablename__ = "users"

    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(250), nullable=False)
    role = Column(Enum('admin', 'attendant'), nullable=False)
    physical_stock_verifications = relationship("PhysicalStockVerification")

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __init__(self, **kwargs):
        """Initializes an instance
        """
        super().__init__(**kwargs)

# Products Table
class Product(BaseModel, Base):
    __tablename__ = 'products'
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=True)
    product_type = Column(String(100), nullable=False)
    brand = Column(String(100), nullable=True)
    size = Column(Float, nullable=True)
    unit_price = Column(Float, nullable=False)
    inventories = relationship("Inventory")
    sale_items = relationship("SaleItem")

    def __init__(self, **kwargs):
        """Initializes an instance
        """
        super().__init__(**kwargs)

# Inventory Table
class Inventory(BaseModel, Base):
    __tablename__ = 'inventory'
    product_id = Column(String(100), ForeignKey('products.id'), nullable=False)
    branch_id = Column(String(100), ForeignKey('branches.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    last_updated = Column(Date, nullable=False)

    def __init__(self, **kwargs):
        """Initializes an instance
        """
        super().__init__(**kwargs)

# Inventory Logs Table
class InventoryLog(BaseModel, Base):
    __tablename__ = 'inventory_logs'
    branch_id = Column(String(100), ForeignKey('branches.id'), nullable=False)
    product_id = Column(String(100), ForeignKey('products.id'), nullable=False)
    change_type = Column(String(100), nullable=False)
    quantity = Column(Integer, nullable=False)

    def __init__(self, **kwargs):
        """Initializes an instance
        """
        super().__init__(**kwargs)

# Physical Stock Verification Table
class PhysicalStockVerification(BaseModel, Base):
    __tablename__ = 'physical_stock_verifications'
    branch_id = Column(String(100), ForeignKey('branches.id'), nullable=False)
    verified_by = Column(String(100), ForeignKey('users.id'), nullable=False)
    verification_date = Column(Date, nullable=False)
    discrepancy = Column(Text, nullable=True)

    def __init__(self, **kwargs):
        """Initializes an instance
        """
        super().__init__(**kwargs)

# Sales Table
class Sale(BaseModel, Base):
    __tablename__ = 'sales'
    branch_id = Column(String(100), ForeignKey('branches.id'), nullable=False)
    customer_id = Column(String(100), ForeignKey('customers.id'), nullable=True)
    sale_date = Column(Date, nullable=False)
    total_amount = Column(Float, nullable=False)
    payment_method = Column(String(100), nullable=False)
    status = Column(String(100), nullable=False)
    items = relationship('SaleItem')

    def __init__(self, **kwargs):
        """Initializes an instance
        """
        super().__init__(**kwargs)

# Sale Items Table
class SaleItem(BaseModel, Base):
    __tablename__ = 'sale_items'
    sale_id = Column(String(100), ForeignKey('sales.id'), nullable=False)
    product_id = Column(String(100), ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    price_per_unit = Column(Float, nullable=False)

    def __init__(self, **kwargs):
        """Initializes an instance
        """
        super().__init__(**kwargs)

# Invoices Table
class Invoice(BaseModel, Base):
    __tablename__ = 'invoices'
    sale_id = Column(String(100), ForeignKey('sales.id'), nullable=False)
    invoice_date = Column(Date, nullable=False)
    due_date = Column(Date, nullable=False)
    total_amount = Column(Float, nullable=False)
    paid_amount = Column(Float, nullable=False)
    balance_due = Column(Float, nullable=False)
    receipts = relationship("Receipt")

    def __init__(self, **kwargs):
        """Initializes an instance
        """
        super().__init__(**kwargs)

# Receipts Table
class Receipt(BaseModel, Base):
    __tablename__ = 'receipts'
    invoice_id = Column(String(100), ForeignKey('invoices.id'), nullable=False)
    receipt_date = Column(Date, nullable=False)
    amount_received = Column(Float, nullable=False)
    receipt_method = Column(String(100), nullable=False)

    def __init__(self, **kwargs):
        """Initializes an instance
        """
        super().__init__(**kwargs)

# Suppliers Table
class Supplier(BaseModel, Base):
    __tablename__ = 'suppliers'
    name = Column(String(100), nullable=False)
    contact_person = Column(String(100), nullable=False)
    phone = Column(String(100), nullable=False)
    email = Column(String(100), nullable=True)
    address = Column(Text, nullable=True)
    account_balance = Column(Float, nullable=False)
    purchase_invoices = relationship("PurchaseInvoice")
    payments = relationship("SupplierPayment")

    def __init__(self, **kwargs):
        """Initializes an instance
        """
        super().__init__(**kwargs)

# Supplier Invoices Table
class PurchaseInvoice(BaseModel, Base):
    __tablename__ = 'purchase_invoices'
    supplier_id = Column(String(100), ForeignKey('suppliers.id'), nullable=False)
    invoice_date = Column(Date, nullable=False)
    total_amount = Column(Float, nullable=False)
    paid_amount = Column(Float, nullable=False)
    balance_due = Column(Float, nullable=False)
    status = Column(String(100), nullable=False)

    def __init__(self, **kwargs):
        """Initializes an instance
        """
        super().__init__(**kwargs)

# Purchase Invoice Items Table
class PurchaseInvoiceItem(BaseModel, Base):
    __tablename__ = 'purchase_invoice_items'
    purchase_invoice_id = Column(String(100), ForeignKey('purchase_invoices.id'), nullable=False)
    product_id = Column(String(100), ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Float, nullable=False)
    total_price = Column(Float, nullable=False)

    def __init__(self, **kwargs):
        """Initializes an instance
        """
        super().__init__(**kwargs)

# Supplier Payments Table
class SupplierPayment(BaseModel, Base):
    __tablename__ = 'supplier_payments'
    supplier_id = Column(String(100), ForeignKey('suppliers.id'), nullable=False)
    purchase_invoice_id = Column(String(100), ForeignKey('purchase_invoices.id'), nullable=False)
    payment_date = Column(Date, nullable=False)
    amount = Column(Float, nullable=False)
    payment_method = Column(String(100), nullable=False)

    def __init__(self, **kwargs):
        """Initializes an instance
        """
        super().__init__(**kwargs)

# Branches Table
class Branch(BaseModel, Base):
    __tablename__ = 'branches'
    branch_name = Column(String(100), nullable=False)
    location = Column(String(100), nullable=False)
    attendant = Column(String(100), ForeignKey('users.id'), nullable=True)
    capacity = Column(Integer, nullable=False)
    sales = relationship("Sale")
    inventory = relationship('Inventory')

    def __init__(self, **kwargs):
        """Initializes an instance
        """
        super().__init__(**kwargs)

# Branch Transfers Table
class BranchTransfer(BaseModel, Base):
    __tablename__ = 'branch_transfers'
    from_branch_id = Column(String(100), ForeignKey('branches.id'), nullable=False)
    to_branch_id = Column(String(100), ForeignKey('branches.id'), nullable=False)
    transfer_date = Column(Date, nullable=False)
    status = Column(String(100), nullable=False, default='pending')
    approved_by = Column(String(100), ForeignKey('users.id'), nullable=True)
    items = relationship('BranchTransferItem')

    def __init__(self, **kwargs):
        """Initializes an instance
        """
        super().__init__(**kwargs)

# Branch Transfer Items Table
class BranchTransferItem(BaseModel, Base):
    __tablename__ = 'branch_transfer_items'
    transfer_id = Column(String(100), ForeignKey('branch_transfers.id'), nullable=False)
    product_id = Column(String(100), ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)

    def __init__(self, **kwargs):
        """Initializes an instance
        """
        super().__init__(**kwargs)

# Customers Table
class Customer(BaseModel, Base):
    __tablename__ = 'customers'
    name = Column(String(100), nullable=False)
    phone = Column(String(100), nullable=False)
    email = Column(String(100), nullable=True)
    address = Column(Text, nullable=True)
    branch_id = Column(String(100), ForeignKey('branches.id'), nullable=True)
    account_balance = Column(Float, nullable=False)
    sales = relationship("Sale")

    def __init__(self, **kwargs):
        """Initializes an instance
        """
        super().__init__(**kwargs)

# Customer Preferences Table
class CustomerPreference(BaseModel, Base):
    __tablename__ = 'customer_preferences'
    customer_id = Column(String(100), ForeignKey('customers.id'), nullable=False)
    preferred_cylinder_size = Column(Float, nullable=False)

    def __init__(self, **kwargs):
        """Initializes an instance
        """
        super().__init__(**kwargs)


# Expenses Table
class Expense(BaseModel, Base):
    __tablename__ = 'expenses'
    branch_id = Column(String(100), ForeignKey('branches.id'), nullable=False)
    expense_type = Column(String(100), nullable=False)
    amount = Column(Float, nullable=False)
    expense_date = Column(Date, nullable=False)
    description = Column(Text, nullable=True)

    def __init__(self, **kwargs):
        """Initializes an instance
        """
        super().__init__(**kwargs)
