from __future__ import annotations

import uuid

from sqlalchemy import Boolean, ForeignKey, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from app.models.mixins import IdMixin, TimestampMixin


class LaborMaterialMatch(IdMixin, TimestampMixin, Base):
    __tablename__ = "labor_material_matches"

    bid_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("bid_opportunities.id"),
        nullable=False,
    )
    labor_partner_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("labor_partners.id"),
        nullable=False,
    )
    supplier_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("material_suppliers.id"),
        nullable=False,
    )
    recommended_role: Mapped[str | None] = mapped_column(String(255), nullable=True)
    can_bid_as_prime: Mapped[bool | None] = mapped_column(Boolean, nullable=True)
    can_bid_as_sub: Mapped[bool | None] = mapped_column(Boolean, nullable=True)
    material_only_possible: Mapped[bool | None] = mapped_column(Boolean, nullable=True)
    supply_and_install_possible: Mapped[bool | None] = mapped_column(Boolean, nullable=True)
    risk_notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    estimated_margin: Mapped[float | None] = mapped_column(Numeric(10, 2), nullable=True)
    next_action: Mapped[str | None] = mapped_column(Text, nullable=True)
