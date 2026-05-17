from __future__ import annotations

from sqlalchemy import Integer, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from app.models.mixins import IdMixin, TimestampMixin


class PricingBenchmark(IdMixin, TimestampMixin, Base):
    __tablename__ = "pricing_benchmarks"

    benchmark_name: Mapped[str] = mapped_column(String(255), nullable=False)
    source_agency: Mapped[str | None] = mapped_column(String(255), nullable=True)
    location: Mapped[str | None] = mapped_column(String(255), nullable=True)
    scope_type: Mapped[str | None] = mapped_column(String(255), nullable=True)
    published_amount: Mapped[float | None] = mapped_column(Numeric(12, 2), nullable=True)
    unit_count: Mapped[int | None] = mapped_column(Integer, nullable=True)
    estimated_price_per_unit: Mapped[float | None] = mapped_column(
        Numeric(12, 2),
        nullable=True,
    )
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    source_link: Mapped[str | None] = mapped_column(Text, nullable=True)
    confidence_level: Mapped[str | None] = mapped_column(String(100), nullable=True)
