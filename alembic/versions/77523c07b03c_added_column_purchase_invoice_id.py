"""Added column: purchase_invoice_id

Revision ID: 77523c07b03c
Revises: 43e3c7025d73
Create Date: 2025-01-29 17:43:25.759625

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '77523c07b03c'
down_revision: Union[str, None] = '43e3c7025d73'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'password',
               existing_type=mysql.VARCHAR(length=100),
               type_=sa.String(length=250),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'password',
               existing_type=sa.String(length=250),
               type_=mysql.VARCHAR(length=100),
               existing_nullable=False)
    # ### end Alembic commands ###
