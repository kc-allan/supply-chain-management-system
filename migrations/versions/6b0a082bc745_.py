"""empty message

Revision ID: 6b0a082bc745
Revises: 1e54a636e209
Create Date: 2024-07-14 16:06:24.592220

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b0a082bc745'
down_revision = '1e54a636e209'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('address', sa.String(length=64), nullable=True))
        batch_op.add_column(sa.Column('city', sa.String(length=64), nullable=True))
        batch_op.add_column(sa.Column('state', sa.String(length=64), nullable=True))
        batch_op.add_column(sa.Column('zipcode', sa.String(length=64), nullable=True))
        batch_op.add_column(sa.Column('two_factor', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('sms_notifications', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('email_notifications', sa.Boolean(), nullable=True))
        batch_op.drop_column('location')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('location', sa.VARCHAR(length=64), nullable=True))
        batch_op.drop_column('email_notifications')
        batch_op.drop_column('sms_notifications')
        batch_op.drop_column('two_factor')
        batch_op.drop_column('zipcode')
        batch_op.drop_column('state')
        batch_op.drop_column('city')
        batch_op.drop_column('address')

    # ### end Alembic commands ###
