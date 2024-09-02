"""create users table

Revision ID: 423303349a6d
Revises: 
Create Date: 2024-09-01 22:11:27.546445

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import uuid


# revision identifiers, used by Alembic.
revision: str = '423303349a6d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Ensure the uuid-ossp extension is enabled
    op.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";')

    op.create_table(
        'users',
        sa.Column('id', sa.UUID(as_uuid=True), primary_key=True, server_default=sa.text('uuid_generate_v4()')),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('email', sa.String, unique=True, nullable=False),
        sa.Column('password', sa.String, nullable=False),
        sa.Column('created_at', sa.TIMESTAMP, nullable=True, server_default=sa.func.now()),
        sa.Column('updated_at', sa.TIMESTAMP, nullable=True, server_default=sa.func.now()),
        sa.Column('deleted_at', sa.TIMESTAMP, nullable=True, server_default=sa.func.now()),
        schema='public'
    )


def downgrade() -> None:
    op.drop_table('users')
