"""add currency

Revision ID: 8060250c04f6
Revises: 1da8bd9ba65e
Create Date: 2024-06-03 20:29:29.792645

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8060250c04f6'
down_revision = '1da8bd9ba65e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('invoices', schema=None) as batch_op:
        batch_op.add_column(sa.Column('subtotal', sa.Numeric(), nullable=False))
        batch_op.add_column(sa.Column('itbis_percentage', sa.Numeric(), nullable=True))
        batch_op.add_column(sa.Column('itbis_amount', sa.Numeric(), nullable=True))
        batch_op.add_column(sa.Column('total', sa.Numeric(), nullable=False))
        batch_op.add_column(sa.Column('tax_reference_number', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('issued_with_tax_reference', sa.Boolean(), nullable=False))
        batch_op.add_column(sa.Column('is_void', sa.Boolean(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('invoices', schema=None) as batch_op:
        batch_op.drop_column('is_void')
        batch_op.drop_column('issued_with_tax_reference')
        batch_op.drop_column('tax_reference_number')
        batch_op.drop_column('total')
        batch_op.drop_column('itbis_amount')
        batch_op.drop_column('itbis_percentage')
        batch_op.drop_column('subtotal')

    # ### end Alembic commands ###
