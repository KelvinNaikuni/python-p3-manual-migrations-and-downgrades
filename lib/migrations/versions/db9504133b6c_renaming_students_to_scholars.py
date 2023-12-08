"""Renaming students to scholars

Revision ID: db9504133b6c
Revises: 791279dd0760
Create Date: 2023-12-08 14:15:48.533832

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db9504133b6c'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
