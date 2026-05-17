from __future__ import annotations

from datetime import datetime

from sqlalchemy import Boolean, DateTime, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from app.models.enums import BidStatus, BidType, build_enum
from app.models.mixins import IdMixin, TimestampMixin


class BidOpportunity(IdMixin, TimestampMixin, Base):
    __tablename__ = "bid_opportunities"

    bid_name: Mapped[str] = mapped_column(String(255), nullable=False)
    agency: Mapped[str] = mapped_column(String(255), nullable=False)
    location: Mapped[str | None] = mapped_column(String(255), nullable=True)
    due_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    bid_link: Mapped[str | None] = mapped_column(Text, nullable=True)
    bid_type: Mapped[BidType] = mapped_column(
        build_enum(BidType, name="bid_type"),
        nullable=False,
    )
    scope_summary: Mapped[str | None] = mapped_column(Text, nullable=True)
    material_required: Mapped[bool | None] = mapped_column(Boolean, nullable=True)
    labor_required: Mapped[bool | None] = mapped_column(Boolean, nullable=True)
    license_required: Mapped[bool | None] = mapped_column(Boolean, nullable=True)
    bond_required: Mapped[bool | None] = mapped_column(Boolean, nullable=True)
    insurance_required: Mapped[bool | None] = mapped_column(Boolean, nullable=True)
    workers_comp_required: Mapped[bool | None] = mapped_column(Boolean, nullable=True)
    prevailing_wage: Mapped[bool | None] = mapped_column(Boolean, nullable=True)
    site_visit_required: Mapped[bool | None] = mapped_column(Boolean, nullable=True)
    estimated_contract_size: Mapped[str | None] = mapped_column(String(255), nullable=True)
    estimated_kitchens_units: Mapped[int | None] = mapped_column(Integer, nullable=True)
    suggested_bid_range: Mapped[str | None] = mapped_column(String(255), nullable=True)
    opportunity_score: Mapped[int | None] = mapped_column(Integer, nullable=True)
    status: Mapped[BidStatus] = mapped_column(
        build_enum(BidStatus, name="bid_status"),
        nullable=False,
        default=BidStatus.NEW,
        server_default=BidStatus.NEW.value,
    )
