"""coleccion

Revision ID: 68bdcc429679
Revises: de699c3e8daf
Create Date: 2023-03-09 01:49:54.363883

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68bdcc429679'
down_revision = 'de699c3e8daf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('coleccion',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('usuario_id', sa.Integer(), nullable=True),
    sa.Column('pokemon_id', sa.Integer(), nullable=True),
    sa.Column('estado', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['pokemon_id'], ['pokemon.id'], ),
    sa.ForeignKeyConstraint(['usuario_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('coleccion')
    # ### end Alembic commands ###