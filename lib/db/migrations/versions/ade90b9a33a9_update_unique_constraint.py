"""update unique constraint

Revision ID: ade90b9a33a9
Revises: 32ced0e99842
Create Date: 2023-08-27 22:23:36.940850

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ade90b9a33a9'
down_revision: Union[str, None] = '32ced0e99842'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('inventory', schema=None) as batch_op:
        batch_op.drop_constraint('add_unit', type_='unique')

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('inventory', schema=None) as batch_op:
        batch_op.create_unique_constraint('add_unit', ['unit'])

    # ### end Alembic commands ###
