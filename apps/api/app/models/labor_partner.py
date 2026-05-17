from __future__ import annotations

from sqlalchemy import Boolean, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from app.models.enums import PartnerStatus, build_enum
from app.models.mixins import IdMixin, TimestampMixin


class LaborPartner(IdMixin, TimestampMixin, Base):
    __tablename__ = "labor_partners"

    company_name: Mapped[str] = mapped_column(String(255), nullable=False)
    contact_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    phone: Mapped[str | None] = mapped_column(String(50), nullable=True)
    email: Mapped[str | None] = mapped_column(String(255), nullable=True)
    state: Mapped[str | None] = mapped_column(String(100), nullable=True)
    service_area: Mapped[str | None] = mapped_column(String(255), nullable=True)
    trade_type: Mapped[str | None] = mapped_column(String(255), nullable=True)
    license_number: Mapped[str | None] = mapped_column(String(100), nullable=True)
    license_status: Mapped[str | None] = mapped_column(String(100), nullable=True)
    insurance_status: Mapped[str | None] = mapped_column(String(100), nullable=True)
    bonding_status: Mapped[str | None] = mapped_column(String(100), nullable=True)
    workers_comp_status: Mapped[str | None] = mapped_column(String(100), nullable=True)
    public_housing_experience: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
        server_default="0",
    )
    multifamily_experience: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
        server_default="0",
    )
    prevailing_wage_experience: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
        server_default="0",
    )
    occupied_unit_experience: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
        server_default="0",
    )
    capacity_per_week: Mapped[int | None] = mapped_column(Integer, nullable=True)
    photos_portfolio_link: Mapped[str | None] = mapped_column(Text, nullable=True)
    references: Mapped[str | None] = mapped_column(Text, nullable=True)
    agreement_signed: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
        server_default="0",
    )
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    status: Mapped[PartnerStatus] = mapped_column(
        build_enum(PartnerStatus, name="partner_status"),
        nullable=False,
        default=PartnerStatus.PENDING,
        server_default=PartnerStatus.PENDING.value,
    )
