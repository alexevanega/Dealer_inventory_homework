"""empty message

Revision ID: c36efb4fd46a
Revises: d0612ab33937
Create Date: 2021-12-14 15:55:39.029037

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c36efb4fd46a'
down_revision = 'd0612ab33937'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('inventory',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image', sa.String(length=300), nullable=True),
    sa.Column('vin_num', sa.String(length=16), nullable=False),
    sa.Column('year', sa.String(length=4), nullable=True),
    sa.Column('make', sa.String(length=25), nullable=True),
    sa.Column('model', sa.String(length=75), nullable=False),
    sa.Column('description', sa.String(length=300), nullable=True),
    sa.Column('date_added', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('vin_num')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('inventory')
    # ### end Alembic commands ###
