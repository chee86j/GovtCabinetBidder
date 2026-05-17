"""create_pricing_benchmarks

Revision ID: fac4ee6c6163
Revises: 7081042367e0
Create Date: 2026-05-17 06:06:53.000000
"""
from __future__ import annotations

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'fac4ee6c6163'
down_revision: Union[str, Sequence[str], None] = '7081042367e0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'pricing_benchmarks',
        sa.Column('benchmark_name', sa.String(length=255), nullable=False),
        sa.Column('source_agency', sa.String(length=255), nullable=True),
        sa.Column('location', sa.String(length=255), nullable=True),
        sa.Column('scope_type', sa.String(length=255), nullable=True),
        sa.Column('published_amount', sa.Numeric(precision=12, scale=2), nullable=True),
        sa.Column('unit_count', sa.Integer(), nullable=True),
        sa.Column('estimated_price_per_unit', sa.Numeric(precision=12, scale=2), nullable=True),
        sa.Column('notes', sa.Text(), nullable=True),
        sa.Column('source_link', sa.Text(), nullable=True),
        sa.Column('confidence_level', sa.String(length=100), nullable=True),
        sa.Column('id', sa.Uuid(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )


def downgrade() -> None:
    op.drop_table('pricing_benchmarks')
