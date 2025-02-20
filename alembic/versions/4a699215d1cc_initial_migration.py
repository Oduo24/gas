"""Initial migration

Revision ID: 4a699215d1cc
Revises: 
Create Date: 2025-01-28 10:50:34.703549

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '4a699215d1cc'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('purchase_invoices',
    sa.Column('id', sa.String(length=100), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('supplier_id', sa.String(length=100), nullable=False),
    sa.Column('invoice_date', sa.Date(), nullable=False),
    sa.Column('total_amount', sa.Float(), nullable=False),
    sa.Column('paid_amount', sa.Float(), nullable=False),
    sa.Column('balance_due', sa.Float(), nullable=False),
    sa.Column('status', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['supplier_id'], ['suppliers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('purchase_invoice_items',
    sa.Column('id', sa.String(length=100), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('purchase_invoice_id', sa.String(length=100), nullable=False),
    sa.Column('product_id', sa.String(length=100), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('unit_price', sa.Float(), nullable=False),
    sa.Column('total_price', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.ForeignKeyConstraint(['purchase_invoice_id'], ['purchase_invoices.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('supplier_invoices')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('supplier_invoices',
    sa.Column('id', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('supplier_id', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('invoice_date', sa.DATE(), nullable=False),
    sa.Column('total_amount', mysql.FLOAT(), nullable=False),
    sa.Column('paid_amount', mysql.FLOAT(), nullable=False),
    sa.Column('balance_due', mysql.FLOAT(), nullable=False),
    sa.Column('status', mysql.VARCHAR(length=100), nullable=False),
    sa.ForeignKeyConstraint(['supplier_id'], ['suppliers.id'], name='supplier_invoices_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('purchase_invoice_items')
    op.drop_table('purchase_invoices')
    # ### end Alembic commands ###
