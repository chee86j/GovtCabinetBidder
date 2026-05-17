from __future__ import annotations

import uuid

from sqlalchemy import Enum
from sqlalchemy.sql.schema import Column

from app.db.base import Base
from app.models import (
    BidOpportunity,
    BidStatus,
    BidType,
    IdMixin,
    LaborPartner,
    LaborMaterialMatch,
    MaterialSupplier,
    PartnerStatus,
    PricingBenchmark,
    SupplierType,
    TimestampMixin,
)


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


def test_bid_opportunity_model_uses_shared_enums_and_defaults() -> None:
    status_column = BidOpportunity.__table__.c["status"]
    bid_type_column = BidOpportunity.__table__.c["bid_type"]

    assert BidOpportunity.__tablename__ == "bid_opportunities"
    assert isinstance(status_column.type, Enum)
    assert isinstance(bid_type_column.type, Enum)
    assert list(status_column.type.enums) == [member.value for member in BidStatus]
    assert list(bid_type_column.type.enums) == [member.value for member in BidType]
    assert status_column.nullable is False
    assert status_column.default is not None


def test_labor_partner_model_defaults_match_expected_values() -> None:
    agreement_signed_column = LaborPartner.__table__.c["agreement_signed"]
    status_column = LaborPartner.__table__.c["status"]

    assert LaborPartner.__tablename__ == "labor_partners"
    assert agreement_signed_column.nullable is False
    assert agreement_signed_column.default is not None
    assert status_column.nullable is False
    assert list(status_column.type.enums) == [member.value for member in PartnerStatus]
    assert status_column.default is not None


def test_material_supplier_model_uses_expected_enums_and_defaults() -> None:
    supplier_type_column = MaterialSupplier.__table__.c["supplier_type"]
    status_column = MaterialSupplier.__table__.c["status"]
    ships_nationwide_column = MaterialSupplier.__table__.c["ships_nationwide"]

    assert MaterialSupplier.__tablename__ == "material_suppliers"
    assert isinstance(supplier_type_column.type, Enum)
    assert isinstance(status_column.type, Enum)
    assert list(supplier_type_column.type.enums) == [member.value for member in SupplierType]
    assert list(status_column.type.enums) == [member.value for member in PartnerStatus]
    assert ships_nationwide_column.nullable is False
    assert ships_nationwide_column.default is not None
    assert status_column.nullable is False
    assert status_column.default is not None


def test_labor_material_match_model_uses_expected_foreign_keys() -> None:
    bid_column = LaborMaterialMatch.__table__.c["bid_id"]
    labor_partner_column = LaborMaterialMatch.__table__.c["labor_partner_id"]
    supplier_column = LaborMaterialMatch.__table__.c["supplier_id"]

    assert LaborMaterialMatch.__tablename__ == "labor_material_matches"
    assert list(bid_column.foreign_keys)[0].target_fullname == "bid_opportunities.id"
    assert list(labor_partner_column.foreign_keys)[0].target_fullname == "labor_partners.id"
    assert list(supplier_column.foreign_keys)[0].target_fullname == "material_suppliers.id"


def test_pricing_benchmark_model_exposes_reference_storage_fields() -> None:
    benchmark_name_column = PricingBenchmark.__table__.c["benchmark_name"]
    published_amount_column = PricingBenchmark.__table__.c["published_amount"]

    assert PricingBenchmark.__tablename__ == "pricing_benchmarks"
    assert benchmark_name_column.nullable is False
    assert published_amount_column.nullable is True
