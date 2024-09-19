"""matches table

Revision ID: 5faab0cd4d6c
Revises: c727ae553324
Create Date: 2024-09-20 00:17:27.866419

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5faab0cd4d6c'
down_revision = 'c727ae553324'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('match',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('team_a', sa.String(length=64), nullable=False),
    sa.Column('team_b', sa.String(length=64), nullable=False),
    sa.Column('goals_a', sa.Integer(), nullable=False),
    sa.Column('goals_b', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['team_a'], ['team.name'], ),
    sa.ForeignKeyConstraint(['team_b'], ['team.name'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('team', schema=None) as batch_op:
        batch_op.add_column(sa.Column('registration_date', sa.DateTime(), nullable=False))
        batch_op.drop_index('ix_team_name')
        batch_op.drop_column('id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('team', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.INTEGER(), nullable=False))
        batch_op.create_index('ix_team_name', ['name'], unique=1)
        batch_op.drop_column('registration_date')

    op.drop_table('match')
    # ### end Alembic commands ###
