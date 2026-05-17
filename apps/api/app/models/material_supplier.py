from __future__ import annotations

from sqlalchemy import Boolean, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from app.models.enums import PartnerStatus, SupplierType, build_enum
from app.models.mixins import IdMixin, TimestampMixin


class MaterialSupplier(IdMixin, TimestampMixin, Base):
    __tablename__ = "material_suppliers"

    supplier_name: Mapped[str] = mapped_column(String(255), nullable=False)
    contact_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    phone: Mapped[str | None] = mapped_column(String(50), nullable=True)
    email: Mapped[str | None] = mapped_column(String(255), nullable=True)
    location: Mapped[str | None] = mapped_column(String(255), nullable=True)
    supplier_type: Mapped[SupplierType] = mapped_column(
        build_enum(SupplierType, name="supplier_type"),
        nullable=False,
    )
    product_categories: Mapped[str | None] = mapped_column(Text, nullable=True)
    service_area: Mapped[str | None] = mapped_column(String(255), nullable=True)
    ships_nationwide: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
        server_default="0",
    )
    minimum_order: Mapped[str | None] = mapped_column(String(255), nullable=True)
    lead_time: Mapped[str | None] = mapped_column(String(255), nullable=True)
    certifications: Mapped[str | None] = mapped_column(Text, nullable=True)
    warranty: Mapped[str | None] = mapped_column(Text, nullable=True)
    sample_availability: Mapped[str | None] = mapped_column(String(255), nullable=True)
    bulk_pricing: Mapped[str | None] = mapped_column(Text, nullable=True)
    delivery_terms: Mapped[str | None] = mapped_column(Text, nullable=True)
    payment_terms: Mapped[str | None] = mapped_column(Text, nullable=True)
    government_experience: Mapped[str | None] = mapped_column(Text, nullable=True)
    product_catalog_link: Mapped[str | None] = mapped_column(Text, nullable=True)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    status: Mapped[PartnerStatus] = mapped_column(
        build_enum(PartnerStatus, name="material_supplier_status"),
        nullable=False,
        default=PartnerStatus.PENDING,
        server_default=PartnerStatus.PENDING.value,
    )
