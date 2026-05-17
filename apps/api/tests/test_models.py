from __future__ import annotations

import uuid

from sqlalchemy.sql.schema import Column

from app.db.base import Base
from app.models import BidStatus, BidType, IdMixin, PartnerStatus, SupplierType, TimestampMixin


class ExampleModel(IdMixin, TimestampMixin, Base):
    __tablename__ = "example_model"


def get_column(name: str) -> Column[object]:
    return ExampleModel.__table__.c[name]


def test_shared_model_mixins_define_expected_columns() -> None:
    id_column = get_column("id")
    created_at_column = get_column("created_at")
    updated_at_column = get_column("updated_at")

    assert id_column.primary_key is True
    assert ExampleModel.id.type.python_type is uuid.UUID
    assert created_at_column.nullable is False
    assert created_at_column.server_default is not None
    assert updated_at_column.nullable is False
    assert updated_at_column.server_default is not None
    assert updated_at_column.onupdate is not None


def test_shared_enums_expose_expected_values() -> None:
    assert [member.value for member in BidType] == [
        "material_only",
        "labor_only",
        "supply_and_install",
        "full_rehab_unit_turnover",
        "commercial_casework_millwork",
        "unknown",
    ]
    assert [member.value for member in BidStatus] == [
        "new",
        "reviewing",
        "need_partner",
        "pricing",
        "submitted",
        "won",
        "lost",
        "skipped",
    ]
    assert [member.value for member in PartnerStatus] == [
        "active",
        "inactive",
        "pending",
        "rejected",
    ]
    assert [member.value for member in SupplierType] == [
        "local_cabinet_wholesaler",
        "rta_supplier",
        "imported_manufacturer",
        "countertop_fabricator",
        "vanity_supplier",
        "hardware_supplier",
        "plumbing_appliance_supplier",
        "other",
    ]
