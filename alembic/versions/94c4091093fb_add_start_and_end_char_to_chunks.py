"""add start and end char to chunks

Revision ID: 94c4091093fb
Revises: 53f1140934c5
Create Date: 2026-06-21 10:00:05.095142
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '94c4091093fb'
down_revision: Union[str, Sequence[str], None] = '53f1140934c5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.add_column(
        'chunks',
        sa.Column(
            'start_char',
            sa.Integer(),
            nullable=True
        )
    )

    op.add_column(
        'chunks',
        sa.Column(
            'end_char',
            sa.Integer(),
            nullable=True
        )
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_column('chunks', 'start_char')
    op.drop_column('chunks', 'end_char')