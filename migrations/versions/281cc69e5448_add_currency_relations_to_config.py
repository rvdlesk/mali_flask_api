"""add currency relations to config

Revision ID: 281cc69e5448
Revises: 8060250c04f6
Create Date: 2024-06-03 20:32:16.689205

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '281cc69e5448'
down_revision = '8060250c04f6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('invoice_config', schema=None) as batch_op:
        batch_op.add_column(sa.Column('currency_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'currencies', ['currency_id'], ['id'])

    with op.batch_alter_table('invoices', schema=None) as batch_op:
        batch_op.add_column(sa.Column('currency_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'currencies', ['currency_id'], ['id'])

    with op.batch_alter_table('quotations', schema=None) as batch_op:
        batch_op.add_column(sa.Column('currency_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'currencies', ['currency_id'], ['id'])

    with op.batch_alter_table('quote_config', schema=None) as batch_op:
        batch_op.add_column(sa.Column('currency_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'currencies', ['currency_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('quote_config', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('currency_id')

    with op.batch_alter_table('quotations', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('currency_id')

    with op.batch_alter_table('invoices', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('currency_id')

    with op.batch_alter_table('invoice_config', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('currency_id')

    # ### end Alembic commands ###
